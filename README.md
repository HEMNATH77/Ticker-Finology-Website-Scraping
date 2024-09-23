# Ticker-Finology-Website-Scraping


## Introduction
This project demonstrates how to scrape stock market data from the Finology website using Python. By leveraging `requests`, `BeautifulSoup`, and `pandas`, the project extracts stock market data from a web table, organizes it into a DataFrame, and then exports it to a CSV file. It is an excellent example of web scraping and data manipulation for financial data.

## Table of Contents

- Requirements
- Project Workflow
- Code Explanation
  - 1. Fetching the Web Page
  - 2. Parsing the HTML
  - 3. Extracting Table Headers
  - 4. Scraping Table Data
  - 5. Saving Data to CSV


## Requirements
To run this project, you'll need the following Python libraries:
- `pandas`
- `requests`
- `beautifulsoup4`

    You can install them using:
    ```bash
   pip install pandas requests beautifulsoup4 

## Project Workflow
- Send a GET request to the URL of the Finology stock screener.
- Parse the returned HTML using BeautifulSoup.
- Extract table headers (stock data categories).
- Extract stock data row by row.
- Store the data in a Pandas DataFrame and save it as a CSV file.








