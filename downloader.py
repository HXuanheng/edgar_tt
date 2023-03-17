import pandas as pd
from resources.parameters import *
from sec_edgar_downloader import Downloader

dl = Downloader(results)

# Loop over each CIK in the list and download the most recent 10-K filing
for cik in cik_list:
    # Download the 10-K filing and save it in a folder named after the CIK
    dl.get(filing_type, cik, after=start_date, end=end_date, download_details=True) 