from resources.parameters import *
from sec_edgar_downloader import Downloader

dl = Downloader(results)

# Loop over each CIK in the list and download the most recent 10-K filing
for cik in cik_list:
    # Download the 10-K filing and save it in a folder named after the CIK
    # dl.get(filing_type, cik, after=start_date, before=end_date, download_details=True) 
    # Get all 8-K filings including filing amends (8-K/A)
    dl.get(filing_type, cik, after=start_date, before=end_date, include_amends=True, download_details=True) 