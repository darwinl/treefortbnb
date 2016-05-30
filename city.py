import numpy as np
import csv

pricemap = {}

with open("puzzle.csv", "r") as prices:
    reader = csv.reader(prices)
    next(reader, None) # skip the headers
    for priceline in reader:
        city = priceline[1].lower()

        if city not in pricemap:
            # repeat frequeuncy of this price
            pricemap[city] = []

        a = []
        for idx in range(int(priceline[4])):
            a.append(int(priceline[3]))

        pricemap[city] = pricemap[city] + a

median = {}

with open("out.csv","w") as csvfile:

    fieldnames = ['city', 'units', 'median']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for city in pricemap:
        if len(pricemap[city]) > 0:
            data = np.array(pricemap[city])
            median[city] = np.median(data)
            writer.writerow({'city': city, 'units' : len(pricemap[city]), 'median' : median[city]})






