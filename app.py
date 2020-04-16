from flask import Flask, jsonify, request, make_response
from mail_service import send_report_to_all
from imdb_service import get_poster

app = Flask(__name__)


@app.route('/cp2mail', methods=['POST'])
def cp2mail():
    IMDB = "https://www.imdb.com/title/%s"
    message = request.form.get('message', "")
    imdb_id = request.form.get('imdb_id', None)
    add_poster = False
    if imdb_id:
        link = IMDB % imdb_id
        get_poster(link)
        add_poster = True
    send_report_to_all(message, link, add_poster)
    response = jsonify("OK", 200)
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['content-type'] = "application/json"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)







