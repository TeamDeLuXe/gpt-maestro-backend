import logging
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def operation():
    try:
        raise ValueError("Erreur simulée")
    except Exception as e:
        logging.error("Exception capturée: %s", traceback.format_exc())

operation()