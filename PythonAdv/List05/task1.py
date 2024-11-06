import re
import urllib.request
from collections import defaultdict as dd


def crawl(start_page, distance, action):
    adres = '([a-zA-Z]+.)*[a-zA-Z0-9]+'
    automat = re.compile('http://' + adres)
    
    result = dd(lambda: None)

    with urllib.request.urlopen(start_page) as f:
        tekst = f.read().decode('utf-8')
        links = [url.group(0) for url in automat.finditer(tekst)][:(distance-1)]
        print(links)
    
    result[start_page] = action(tekst)

    for link in links:
        try:
            with urllib.request.urlopen(link) as g:
                tekst = g.read().decode('utf-8')
                result[link] = action(tekst)
        except urllib.error.HTTPError as e:
            result[link] = "Error accesing website occured"
    return result.items()

for url, wynik in crawl('http://www.ii.uni.wroc.pl', 2, lambda tekst: 'Python' in tekst):
    print(f"{url}: {wynik}")
