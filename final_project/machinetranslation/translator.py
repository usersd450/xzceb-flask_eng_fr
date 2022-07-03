import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('qUUBvjyDgZyrdwb0RFz4euhQsidNid5DDcyl_XOe4O2H')
translator = LanguageTranslatorV3(
    version='2018-05-01', authenticator=authenticator)

translator.set_service_url(
    'https://api.au-syd.language-translator.watson.cloud.ibm.com/'
    'instances/4fa71f0b-139f-4cf0-9a1a-7f27cfbff4f6')

def english_to_french(english_text):
    """Translate english to french"""
    french_text= translator.translate(english_text, model_id='en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    """Translate french to english"""
    english_text= translator.translate(french_text, model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")