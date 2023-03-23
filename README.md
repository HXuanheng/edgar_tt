# EDGAR Downloader and lookup key words

## Step: 1 - download the required packages (if not already done)
run in the terminal: `pip install -r requirements.txt`

## Step: 2 - specify the list of parameters (list of firms, sample period, type of filing)
specify the list of cik in *resources/cik.csv*<br />
specify the parameters in *resources/parameters.py*

## Step: 3 - download the files
run in the terminal: `python downloader.py`<br />
output: *results/sec-edgar-filings/*

## Step: 4 - set the list of key words you want count
specify the list of key words in *resources/key_words.csv*

## Step: 5 - produce a panel data with cik, year, filing type, count_word1, count word2, ...
run in the terminal: `python lookup.py`<br />
output: *results/*