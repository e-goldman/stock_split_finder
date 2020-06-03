# stock_split_finder
Integrates data from two csv files for quantitative analysis purposes


--- Description ---

To analyze time series data for stock prices over time, you need to adjust historical prices for stock splits, if any. 
This program can read a file containing a history of stock splits for multiple companies and constructs a dictionary of the 
essential information. 

Next it will lines from a file containing closing stock prices by date for any number of companies, locate the correct 
stock split ratio in the dictionary, if any, and write a new file with all of the information from the old prices file 
plus the splits. If no splits are found, a line gets a split ratio of 1.


--- Input file assumptions ---

'splits.csv'
- must fit in memory
- contains at least columns: 'NextSplitDate', 'SplitDate', 'cumulativeSplitFactor', 'latestSplitFactor', 'tradingItemId'
- ordered by tradingItemId and then by SplitDate
- date format: %Y-%m-%d

'prices.csv'
- contains at least columns: pricingDate, tradingItemId
- ordered by tradingItemId and then by pricingDate
- date format must match format of splits.csv for string comparison


--- Notes ---

For the sake of this exercise, the program assumes complete, ordered files. If I'm able to revisit this later, I'd like 
to expand it to accept files that aren't so nice and tidy and sort them first.

