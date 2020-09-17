from flask import Flask, request, jsonify, json
from flask_cors import CORS
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/text', methods=['post'])
def zy():
    if request.method == "POST":
        data = json.loads(request.form.get('data'))
        text = data['value']
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=str(text), lower=True, source='all_filters')
        for item in tr4s.get_key_sentences(num=1):
            return item.sentence


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8989)
