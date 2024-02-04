import requests

def translate_lyrics(text, target_lang):
    print(target_lang)
    url = 'https://api-free.deepl.com/v2/translate'
    auth_key = '488429b0-e145-a15e-2c38-b6609b995eb4:fx'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
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
            print(translated_text)
            return translated_text
        else:
            print('Error:', response.status_code, response.text)
            return None
    except Exception as e:
        print('Error:', str(e))
        return None
