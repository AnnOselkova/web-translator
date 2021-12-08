from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

en_translator = Translator(from_lang='en', to_lang='ru')
fr_translator = Translator(from_lang='fr', to_lang='ru')
it_translator = Translator(from_lang='it', to_lang='ru')



@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        if 'a' <= word[-1] <= 'z':
            en_word = en_translator.translate(word)
            fr_word = fr_translator.translate(word)
            it_word = it_translator.translate(word)
            return render_template('result.html', word=it_word, word1=fr_word, word2=en_word)

    return render_template('dict.html')


if __name__ == '__main__':
    app.run(port=5002)
