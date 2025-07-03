import datetime
import requests
import xml.etree.ElementTree as ET

ID_EURO = 'R01239'
ID_US_DOLLAR = 'R01235'

current_date = datetime.date.today().strftime('%d.%m.%Y')
url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'

response = requests.get(url)

root = ET.fromstring(response.content)
valute_dict = {}
for valute in root.iter('Valute'):
    valute_dict[valute[3].text] = valute[4].text

print(valute_dict['Евро'])