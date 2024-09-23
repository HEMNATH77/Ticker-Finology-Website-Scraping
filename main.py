import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas

url = "https://ticker.finology.in/"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text,"html.parser")

table = soup.find("table",class_="table table-sm table-hover screenertable")

headers = table.find_all("th")

ts = []

for i in headers:
    title=i.text
    ts.append(title)

df = pd.DataFrame(columns=ts)
#print(df)

rows = table.find_all("tr")
#print(rows)
for i in rows[1:]:
  dr = i.find_all("td")
  #print(dr)
  row=[tr.text for tr in dr]
 # print(row)
  l=len(df)
  df.loc[l]=row

print(df)

df.to_csv("stock market.csv")



















