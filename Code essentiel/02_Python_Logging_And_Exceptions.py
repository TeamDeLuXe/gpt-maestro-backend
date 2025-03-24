import logging

logging.basicConfig(level=logging.INFO)

try:
    # Code sensible
    pass
except Exception as e:
    logging.error(f"Erreur détectée : {e}")