
import csv

splitDict = {}

with open('splits.csv') as splits:
    reader = csv.DictReader(splits)

    for row in reader:
        nextSplitDate = row['NextSplitDate']
        splitDate = row['SplitDate']
        cumulativeSplitFactor = float(row['cumulativeSplitFactor'])
        latestSplitFactor = float(row['latestSplitFactor'])
        tradingItemId = row['tradingItemId'].split(sep='.')[0]

        if tradingItemId in splitDict:
            splitDict[tradingItemId][nextSplitDate] = str(cumulativeSplitFactor)
        else:
            splitDict[tradingItemId] = {splitDate: str(cumulativeSplitFactor * latestSplitFactor),
                                        nextSplitDate: str(cumulativeSplitFactor)}

with open('prices.csv') as infile, open('prices_with_adjustments.csv', 'w') as outfile:
    reader = csv.DictReader(infile)
    headers = ['close', 'closeUsd', 'pricingDate', 'tradingItemId', 'volume', 'adjustmentFactor']
    writer = csv.DictWriter(outfile, fieldnames=headers)
    writer.writeheader()

    for row in reader:
        pricingDate = row['pricingDate']
        tradingItemId = row['tradingItemId'].split(sep='.')[0]

        if tradingItemId not in splitDict:
            row['adjustmentFactor'] = '1.0'
            writer.writerow(row)
        else:
            for key in splitDict[tradingItemId]:
                if pricingDate < key:
                    row['adjustmentFactor'] = splitDict[tradingItemId][key]
                    writer.writerow(row)
                    break


