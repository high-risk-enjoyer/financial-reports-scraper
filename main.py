import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://strefainwestorow.pl/dane/raporty/lista-publikacji-raportow-okresowych/all"
response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")

headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

rows = []
for tr in table.find("tbody").find_all("tr"):
    cells = [td.get_text(strip=True) for td in tr.find_all("td")]
    rows.append(cells)

df = pd.DataFrame(rows, columns=headers)

print(df.head)

df.to_csv("financial_report.csv", index=False, encoding="utf-8-sig")
