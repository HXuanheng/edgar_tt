# Specify the type of file
filing_type = "10-K"

# Define start and end dates
start_date = '2002-02-01'           #YYYY-MM-DD
end_date = '2023-03-17'             #YYYY-MM-DD

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