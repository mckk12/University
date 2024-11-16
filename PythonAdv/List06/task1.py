import re
import urllib.request
from collections import defaultdict as dd
import threading, queue

def worker(shared_queue, res, action):
    while True:

        item = shared_queue.get()
        if item is None:
            break

        try:
            with urllib.request.urlopen(item) as f:
                tekst = f.read().decode('utf-8')
                res[item] = action(tekst)
        except urllib.error.HTTPError:
            res[item] = "Error accesing website occured"

        shared_queue.task_done()

def crawl(start_page, distance, action):
    shared_queue = queue.Queue()
    result = dd(lambda: None)

    with urllib.request.urlopen(start_page) as f:
        adres = '([a-zA-Z]+.)*[a-zA-Z0-9]+'
        automat = re.compile('http://' + adres)

        tekst = f.read().decode('utf-8')
        links = set([url.group() for url in automat.finditer(tekst)][:(distance-1)])

        shared_queue.put(start_page)
        for link in links:
            shared_queue.put(link)

    watki = [ threading.Thread(target=worker, args=(shared_queue, result, action)) for _ in range(4) ]
    [shared_queue.put(None) for _ in watki]
    [ w.start() for w in watki ]
    [ w.join() for w in watki ]

    return result.items()

for url, wynik in crawl('http://www.ii.uni.wroc.pl', 2, lambda tekst: 'Python' in tekst):
    print(f"{url}: {wynik}")
