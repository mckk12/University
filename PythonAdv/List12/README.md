
## Przeprowadzanie testów

Stworzyłem plik taskA.py zawierający przykładowe testy, wykorzystując PyUnit

### Wywoałanie testów:
```bash
python -m unittest discover -s tests
```

## Formatowanie kodu zgodnie z PEP 8

Do sprawdzania zgodności kodu z wytycznymi PEP 8 wykorzystano:
- **`pycodestyle`** do analizy kodu,
- **`autopep8`** do automatycznego poprawiania stylu.

### Sprawdzenie zgodności kodu:
```bash
pycodestyle src/ tests/
```

### Automatyczne poprawienie kodu:
```bash
autopep8 --in-place --recursive --aggressive src/ tests/
```

## Automatyczna generacja dokumentacji

Do automatycznego generowania dokumentacji wykorzystałem moduł **`pdoc`**

### Generacja dokumentacji:
```bash
pdoc --output-dir docs/html src/
```
