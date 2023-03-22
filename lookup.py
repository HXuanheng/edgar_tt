from resources.parameters import *
import pandas as pd
import re
import os
import numpy as np 
from tqdm import tqdm
from datetime import datetime


# Count words for a given file
def count(word, file_contents):
    # Count the number of occurrences of the word
    word_count = file_contents.lower().count(word.lower())
    # Print the number of occurrences of the word
    return word_count 

def get_date(file_contents):
    conf_str = file_contents.split("CONFORMED PERIOD OF REPORT:")[1].split()[0]
    conf = datetime.strptime(conf_str, "%Y%m%d")
    filed_str = file_contents.split("FILED AS OF DATE:")[1].split()[0]
    filed = datetime.strptime(filed_str, "%Y%m%d")
    try:
        change_str = file_contents.split("DATE AS OF CHANGE:")[1].split()[0]
        change = datetime.strptime(change_str, "%Y%m%d")
    except:
        change = pd.NaT
    return conf, filed, change

def main():
    df = pd.DataFrame({'cik': [],
                        'conformed_period': [],
                        'filed_date': [],
                        'date_as_of_change': [],
                        'filing_type': [],
                        'file_path': []})
    for cik in tqdm(cik_list):
        path = r"results\sec-edgar-filings\{}\{}\\".format(cik, filing_type)
        for folder in [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]:
                filename = path + folder + r"\full-submission.txt"
                # Open the file in read mode
                with open(filename, 'r') as f:
                    # Read the contents of the file into a variable
                    file_contents = f.read()
                # Get dates
                conf_date, filed_date, change_date = get_date(file_contents)
                # New row data
                new_row = pd.DataFrame({'cik': cik, 'conformed_period': conf_date, 'filed_date': filed_date, 'date_as_of_change': change_date, 'filing_type': filing_type, 'file_path': filename}, index=[0])
                # Initialize word count vector
                word_count = np.zeros(len(word_list))
                # Count for each key word
                for word in word_list:
                    # Count
                    word_count = count(word, file_contents)
                    new_row['count_' + word] = word_count
                # Concat with the rest of the dataset
                df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(results + 'lookup_output_{}.csv'.format(filing_type), index=False)

if __name__ == "__main__":
    main()
    