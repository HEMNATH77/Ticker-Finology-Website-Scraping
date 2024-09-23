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

## Code Explanation
 1. Fetching the Web Page
 We use the requests library to get the HTML content from the website.
    ```bash
    url = "https://ticker.finology.in/"
    r = requests.get(url)

2. Parsing the HTML
The HTML content is parsed using BeautifulSoup to navigate and search for the table element.
    ```bash
      headers = table.find_all("th")
      ts = [i.text for i in headers]
     df = pd.DataFrame(columns=ts)
    
3. Extracting Table Headers
We extract the column headers (like stock name, price, etc.) by finding all the <th> tags in the table.
   ```bash
   headers = table.find_all("th")
   ts = [i.text for i in headers]
   df = pd.DataFrame(columns=ts)

4. Scraping Table Data
Next, we loop through all the rows in the table and scrape the data from each <td> tag.
     ```bash
     rows = table.find_all("tr")
    for i in rows[1:]:
    dr = i.find_all("td")
    row = [tr.text for tr in dr]
    l = len(df)
    df.loc[l] = row
     
5. Saving Data to CSV
Finally, the DataFrame is exported to a CSV file for further analysis.
     ```bash
     df.to_csv("stock_market.csv")


## Conclusion
This project serves as a foundational example of how to efficiently collect stock market data from the web using Python. Web scraping is a crucial skill, particularly for financial analysts, data scientists, and developers who want to gather real-time or periodic data from public websites. By extracting data from the Finology website, this project demonstrates how to convert raw HTML content into structured data that can be analyzed, visualized, or stored for future use.






