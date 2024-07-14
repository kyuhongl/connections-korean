import translators as ts
from googletrans import Translator

def translate_to_korean(text):
    try: 
        result = ts.translate_text(text, to_language='ko')
        return result
    except Exception as e:
        print("Error in TRANSLATION", e)
        return None

