from resources.parameters import *
import pandas as pd
import re
import os
import numpy as np 


# Count words for a given file
def count(word, filename):
    # Open the file in read mode
    with open(filename, 'r') as f:
        # Read the contents of the file into a variable
        file_contents = f.read()
    # Count the number of occurrences of the word
    word_count = file_contents.lower().count(word.lower())
    # Print the number of occurrences of the word
    return word_count 

def main():
    df = pd.DataFrame({'cik': [],
                        'year': [],
                        'filing_type': []})
    for cik in cik_list:
        path = r"results\sec-edgar-filings\{}\{}\\".format(cik, filing_type)
        for folder in [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]:
                filename = path + folder + r"\full-submission.txt"
                match = re.search('\-(.*?)\-', folder)
                year = "20" + match.group(1)
                word_count = np.zeros(len(word_list))
                new_row = pd.DataFrame({'cik': cik, 'year': year, 'filing_type': filing_type}, index=[0])
                for word in word_list:
                    word_count = count(word, filename)
                    new_row['count_' + word] = word_count
                df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(results + 'lookup_output.csv', index=False)

if __name__ == "__main__":
    main()
    