import requests
import time
from Display_translation import display_translation
from Loading_bar import loading_bar_simulation

def translate_lyrics(text, target_lang):
    print(target_lang)
    url = 'https://api-free.deepl.com/v2/translate'
    auth_key = 'MY_API_KEY'  # Replace 'API_KEY_HERE' with actual API key
    params = {
        'auth_key': auth_key,
        'text': text,
        'target_lang': target_lang
    }

    try:
        response = requests.post(url, data=params)
        if response.status_code == 200:
            translation_data = response.json()
            translated_text = translation_data['translations'][0]['text']
            loading_bar_simulation()
            time.sleep(5) 
            display_translation(translated_text)
        else:
            print('Error:', response.status_code, response.text)
            return None
    except Exception as e:
        print('Error:', str(e))
        return None
