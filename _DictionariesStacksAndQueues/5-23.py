import requests
import json

# Krok 1: Pobieranie danych o kursach euro z API NBP
url = "https://api.nbp.pl/api/exchangerates/rates/A/EUR/last/10?format=json"
response = requests.get(url)

# Sprawdzamy, czy zapytanie do API zakończyło się sukcesem
if response.status_code == 200:
    data = response.json()
    
    # Krok 2: Zapisanie danych do pliku euro.json
    with open('euro.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("Data has been saved to euro.json")
else:
    print("Failed to fetch data from API. Status code:", response.status_code)

# Krok 3: Odczyt danych z pliku euro.json i wyświetlenie ich w żądanym formacie
with open('euro.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    print("Date            Buying Rate     Selling Rate")
    print("============================================")
    
    for rate in data['rates']:
        date = rate['effectiveDate']
        buying_rate = rate['bid']
        selling_rate = rate['ask']
        print(f"{date}      {buying_rate:>10}          {selling_rate:>10}")
