# Specify the type of file
filing_type = "8-K"

# Define start and end dates
start_date = '2022-01-01'           #YYYY-MM-DD
end_date = '2023-03-22'             #YYYY-MM-DD

# File position (do not change)
import pandas as pd
resources="resources/"
results="results/"
dtypes = {"cik": str}
df = pd.read_csv(resources + "/cik.csv", dtype=dtypes)
cik_list = df.cik.values
dtypes = {"keywords": str}
df = pd.read_csv(resources + "/key_words.csv", dtype=dtypes)
word_list = df.keywords.values