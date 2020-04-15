from flask import Flask, jsonify, request, make_response
from mail_service import send_report_to_all

app = Flask(__name__)


@app.route('/cp2mail', methods=['POST'])
def cp2mail():
    IMDB = "https://www.imdb.com/title/%s"
    message = request.form.get('message', '')
    link = IMDB % request.form.get('imdb_id', '')
    send_report_to_all(message, link)
    response = jsonify("OK", 200)
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['content-type'] = "application/json"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)







