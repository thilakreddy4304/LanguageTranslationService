from flask import Flask, request, render_template
from MarianMT_Romanian_to_English import translate_sentence
from MarianMT_French_to_English import translate_sentence_from_french_to_english
from googletrans import Translator

app = Flask(__name__)

def translate_with_googletrans(input_text, english_language):
    textaftertranslation = Translator().translate(input_text, dest=english_language).text
    return textaftertranslation

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translateToEnglish():
    input_text = request.form['input_text']
    language = Translator().detect(input_text).lang
    try:
        if language == 'ro':
            translated_text = translate_sentence(input_text)
        elif language == 'fr':
            translated_text = translate_sentence_from_french_to_english(input_text)
        else:
            translated_text = "Please enter only French or Romanian"
            
        if translated_text == input_text:
                raise KeyError
    except Exception as e:
        translated_text = f"Exception: {str(e)}"
    except KeyError:
        translated_text = translate_with_googletrans(input_text, 'en')

    return translated_text


if __name__ == '__main__':
    app.run(debug=True)
