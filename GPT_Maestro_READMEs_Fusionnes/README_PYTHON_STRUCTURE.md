# 📘 README PYTHON STRUCTURE



---

## 📄 01_Python_PEP8_Guide.md

# Guide PEP8 Python

- Indentation: 4 espaces
- Nommage: snake_case
- Longueur max ligne: 79 caractères
- Commentaires: Utiliser # pour commentaires simples
- Docstrings: Triple guillemets """

> Respecter les standards pour un code lisible et maintenable.


---

## 📄 01b_PEP8_Conventions_Avance.md

# Conventions Avancées Python

- Annotations de type
- Gestion des imports avec isort
- Utilisation de `black` pour formatter
- Convention des tests avec `pytest`
- Gestion mémoire et performance (profiling)

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```


---

## 📄 08_Modular_Project_Structure.txt

mon_projet/
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── requirements.txt
└── README.md


---

## 📄 08b_Structure_Modulaire_Projets_Complexes.txt

mon_projet/
├── core/
│   └── services/
├── interfaces/
│   └── cli.py
├── data/
│   └── csv_handler.py
├── tests/
│   └── test_services.py
├── .env
├── setup.py
├── README.md
├── .github/workflows/
│   └── ci.yml
