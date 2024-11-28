import asyncio
import aiohttp
import csv
import numpy as np
import matplotlib.pyplot as plt

async def fetch_gold(session):
    data = {'2022' : [],
            '2023' : []}
    async with session.get('https://api.nbp.pl/api/cenyzlota/2022-01-01/2022-12-31/') as response:
        data['2022'] = await response.json()
    async with session.get('https://api.nbp.pl/api/cenyzlota/2023-01-01/2023-12-31/') as response:
        data['2023'] = await response.json()
    return data
    

async def get():
    data = {'2022' : {},
            '2023' : {}}
    async with aiohttp.ClientSession() as session:
        gold_price = await fetch_gold(session)
        for year in gold_price:
            month_cumulative = [[0, 0] for _ in range(12)]
            for day in gold_price[year]:
                month_cumulative[int(day['data'][5:7])-1][0] += float(day['cena'])
                month_cumulative[int(day['data'][5:7])-1][1] += 1
            for i in range(12):
                data[year][i+1] = month_cumulative[i][0] / month_cumulative[i][1]
    return data
    
def getInflation():
    data = {'2022' : {},
            '2023' : {}}
    with open('inflacja.csv', 'r', encoding='utf-8') as f:
        spamreader = csv.reader(f, delimiter=';')
        for row in spamreader:
            row[5] = row[5].replace(',', '.')
            data[row[3]][int(row[4])] = float(row[5])
    return data
    

def predict_next_year(data):
    prediction = {}
    for year in data:
        values = list(data[year].values())
        z = np.polyfit(values[1:], values[:11], 12)
        p = np.poly1d(z)
        prediction[year] = {i : 0 for i in range(1, 13)}
        prediction[year][1] = values[11]
        for i in range(2, 13):
            prediction[year][i] = p(prediction[year][i-1])
    return prediction

gold = asyncio.run(get())
inflation = getInflation()

fig, (axs, axss) = plt.subplots(2, 2, figsize=(15, 8))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Comparing plot for 2022
axs[0].plot(list(gold['2022'].keys()), list(gold['2022'].values()), label='Gold price')
axs[0].plot(list(inflation['2022'].keys()), list(inflation['2022'].values()), label='Inflation')
axs[0].set_xlabel('Month')
axs[0].set_ylabel('Price')
axs[0].set_title('Gold Price vs Inflation in 2022')
axs[0].set_xticks(range(1, 13))
axs[0].set_xticklabels(months)
axs[0].legend()

# Comparing plot for 2023
axs[1].plot(list(gold['2023'].keys()), list(gold['2023'].values()), label='Gold price')
axs[1].plot(list(inflation['2023'].keys()), list(inflation['2023'].values()), label='Inflation')
axs[1].set_xlabel('Month')
axs[1].set_ylabel('Price')
axs[1].set_title('Gold Price vs Inflation in 2023')
axs[1].set_xticks(range(1, 13))
axs[1].set_xticklabels(months)
axs[1].legend()

gold_prediction = predict_next_year(gold)
inflation_prediction = predict_next_year(inflation)

# Prediction plot for 2024
axss[0].plot(list(gold_prediction['2023'].keys()), list(gold_prediction['2023'].values()), label='Gold price prediction')
axss[0].plot(list(inflation_prediction['2023'].keys()), list(inflation_prediction['2023'].values()), label='Inflation prediction')
axss[0].set_xlabel('Month')
axss[0].set_ylabel('Price')
axss[0].set_title('Gold Price vs Inflation Prediction in 2024')
axss[0].set_xticks(range(1, 13))
axss[0].set_xticklabels(months)
axss[0].legend()

# Prediction plot for 2023
axss[1].plot(list(gold_prediction['2022'].keys()), list(gold_prediction['2022'].values()), label='Gold price prediction')
axss[1].plot(list(inflation_prediction['2022'].keys()), list(inflation_prediction['2022'].values()), label='Inflation prediction')
axss[1].set_xlabel('Month')
axss[1].set_ylabel('Price')
axss[1].set_title('Gold Price vs Inflation Prediction in 2023')
axss[1].set_xticks(range(1, 13))
axss[1].set_xticklabels(months)
axss[1].legend()

plt.tight_layout()
plt.show()
