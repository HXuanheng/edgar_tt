from datetime import datetime

# the file path of the 10-K filing
file_path = "results\\sec-edgar-filings\\0000042582\\10-K\\0000950123-10-014004\\full-submission.txt"

# read the filing text from the file
with open(file_path, 'r') as f:
    filing = f.read()

# extract the date of issue from the filing text
date_str = filing.split("CONFORMED PERIOD OF REPORT:")[1].split()[0]
date = datetime.strptime(date_str, "%Y%m%d")

# print the date of issue
print(date)
