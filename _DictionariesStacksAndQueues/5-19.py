import json

# Otwórz plik JSON i wczytaj dane
with open('reservations.json', 'r', encoding='utf-8') as file:
    reservations = json.load(file)

# Sprawdzamy, czy reservations jest listą słowników
print(reservations)  # To pomoże ci zobaczyć, co zawiera

# Liczymy pokoje opłacone i nieopłacone
paid_reservations = sum(1 for res in reservations if isinstance(res, dict) and res.get('paid', False))
unpaid_reservations = len(reservations) - paid_reservations

# Całkowita wartość opłaconych i nieopłaconych rezerwacji
total_paid = sum(res['price'] for res in reservations if isinstance(res, dict) and res.get('paid', False))
total_unpaid = sum(res['price'] for res in reservations if isinstance(res, dict) and not res.get('paid', False))

# Wyświetlanie wyników
print(f"Total rooms: {len(reservations)}")
print(f"Paid reservations: {paid_reservations}")
print(f"Unpaid reservations: {unpaid_reservations}")
print(f"Total paid amount: {total_paid}")
print(f"Total unpaid amount: {total_unpaid}")
