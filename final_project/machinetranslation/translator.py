"""
A module to connect with the IBM Watson Language Translator Model.
It can perform translation between English and French.
"""
import os
import json
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

language_translator: LanguageTranslatorV3
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    #write the code here
    french_text: str
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        french_text = translation['translations'][0]['translation']  # type: ignore
    except (ApiException, ValueError):
        return ""
    return french_text

def french_to_english(french_text):
    #write the code here
    english_text: str
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        english_text = translation['translations'][0]['translation']  # type: ignore
    except (ApiException, ValueError):
        return ""
    return english_text
