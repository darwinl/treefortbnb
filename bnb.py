import numpy as np
import csv

pricemap = {}

with open("in.csv", "r") as prices:
    reader = csv.reader(prices)
    next(reader, None) # skip the headers
    for priceline in reader:
        state = priceline[2]
        if state not in pricemap:
            # repeat frequeuncy of this price
            pricemap[state] = []

        a = []
        for idx in range(int(priceline[4])):
            a.append(int(priceline[3]))

        pricemap[state] = pricemap[state] + a

median = {}
maxstate = ""
maxmedian = 0

for state in pricemap:
    data = np.array(pricemap[state])
    median[state] = np.median(data)
    if median[state] > maxmedian:
        maxmedian_state = state
        maxmedian = median[state]

print maxmedian_state,maxmedian



