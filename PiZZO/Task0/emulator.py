import json

# Funkcja wczytująca automat z pliku JSON
with open(testowy.aut, 'r') as f:
    automat = json.load(f)