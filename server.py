from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

translator= Translator(to_lang="en", from_lang='ru')

@app.route('/post', methods=['POST'])
def post():
    res = {
        'session': request.json['session'],
        'version': request.json['version'],
        'response': {
            'end_session': False
        }
    }
    req = request.json
    if req['session']['new']:
        res['response']['text'] = 'Привет! Я могу перевести любое слово'
        return jsonify(res)
    words = req['request']['original_utterance'].split()
    if len(words) != 3:
        res['response']['text'] = 'Некорректный запрос. Введи сообщение по шаблону: "Переведи слово <твоё слово>"'
        return jsonify(res)
    word = words[-1]
    translated = str(translator.translate(word))
    res['response']['text'] = translated
    return jsonify(res)

if __name__ == '__main__':
    app.run(port = 8080, host='127.0.0.1')