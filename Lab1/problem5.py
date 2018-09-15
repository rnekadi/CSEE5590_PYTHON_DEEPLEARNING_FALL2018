# Python Program to write Webpage Table tag contents into text file using Beautiful Soup


import requests
from bs4 import BeautifulSoup
import codecs

# Defining the url and doing parse operation from request response

url = "https://www.fantasypros.com/nfl/reports/leaders/qb.php?year=2015"

source = requests.get(url)

plan_txt = source.text

soup = BeautifulSoup(plan_txt, "html.parser")

# logic to extract table header(Column Name) from thead tag

table_head = soup.table.thead

table_head_rows = table_head.findAll('tr')


header = []  # list to hold all the head column name using

for tr in table_head_rows:
    th = tr.find_all('th')
    head = [h.text for h in th]
    header.extend(head)

# Logic to write header(Column Name) using utf8 coding encoding from Codec registry base classes

fl = codecs.open('output.txt', 'wb', 'utf8')
head_line = ','.join(header)
fl.write(head_line + u'\r\n')
fl.close()

# logic to extract table data from within tbody tag


table_data = soup.table.tbody


table_data_rows = table_data.findAll('tr')

rows_data = []  # list to hold table data from tbody

for tr in table_data_rows:
    td = tr.find_all('td')
    data = [d.text for d in td]
    rows_data.append(data)

# logic to append  data record one by from list rows_data
for row in rows_data:
    fl = codecs.open('output.txt', 'ab', 'utf8')
    data_line = ','.join(row)
    fl.write(data_line + u'\r\n')
fl.close()








