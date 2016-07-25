#!/usr/bin/env python2
'''
API Outline:
Using the language and stack of your choice, please create a secure web service
that takes a block of text as input and returns the total count of words and a
case-insensitive count of the occurrence of each word in the text. Counting
punctuation is not required.

Expected behavior:
- Given the input "Welcome to Slack!"
- Produce this output: {"count":3, "words": {"welcome": 1, "to":1, "slack":1}}

Requirements:
- The service is HTTPS only and answers on port 443.
- The certificate and key are correctly installed.
- All API requests must be authenticated. (This service is not publicly available.)
- Requests and replies are json.
- All passwords are stored securely.
- The word counter can handle at least 2 megabytes of input text.

Not requirements:
- Speed. A reasonable solution will be relatively fast, but does not need to be fully optimized.
- You do not need to trust our test certificate authority on your client machine.
'''


from flask import Flask
from flask import request
from flask import jsonify

from libs.auth import requires_auth
from libs.utils import count_words

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {'status': 404, 'message': request.url + ' is hiding by the keys'}
    response = jsonify(message)
    response.status_code = 404
    return response


@app.errorhandler(500)
def internal_error(error=None):
    message = {'status': 500, 'message': request.url + ' has a stomach ache'}
    response = jsonify(message)
    response.status_code = 404
    return response


@app.route('/', methods=['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
@requires_auth
def words():
    if request.method != 'POST':
        message = {'status': 405, 'message': 'Method not supported'}
        response = jsonify(message)
        response.status_code = 405
        return response

    data = request.get_json(force=True, silent=True)
    if data is None or 'text' not in data:
        message = {
            'status': 400,
            'message': 'POST data must be valid JSON containing a text key.'
        }
        response = jsonify(message)
        response.status_code = 400
        return response

    count = count_words(data['text'])
    return jsonify(count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
