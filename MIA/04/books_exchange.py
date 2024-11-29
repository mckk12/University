def books_exchange(books, passSeq):
    books_temp = [0] * (len(books))
    for i in range(len(books)):
        books_temp.pop(passSeq[i]-1)
        books_temp.insert(passSeq[i]-1, books[i])
    #print(books_temp)
    return books_temp

def day_check(books, passSeq):
    days = [-1]*(len(books))
    day = 1
    books_changed = books_exchange(books, passingSequence)
    while -1 in days:
        for i in range(len(books)):
            if books_changed[i] == books[i] and days[i] == -1:
                days[i] = day
        books_changed = books_exchange(books_changed, passingSequence)
        day += 1
    return days
days = []
queries = int(input())
for i in range(queries):
    n = int(input())
    books = [x for x in range(1, n+1)]
    passingSequence = list(map(int, input().split()))
    days.append(day_check(books, passingSequence))

for i in days:    
    print(*i)