from flask import Flask, jsonify, request, make_response
from mail_service import send_cp_mail_to_all
from imdb_service import get_poster
import kodi_service as kodi

app = Flask(__name__)

IMDB = "https://www.imdb.com/title/%s"


@property
def OK():
    response = jsonify("OK", 200)
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['content-type'] = "application/json"
    return response


def _send_notification(message, imdb_id):
    add_poster = False
    link = ""
    if imdb_id:
        link = IMDB % imdb_id
        get_poster(link)
        add_poster = True
    send_cp_mail_to_all(message, link, add_poster)


@app.route('/cp2mail', methods=['POST'])
def cp2mail():
    message = request.form.get('message', "")
    imdb_id = request.form.get('imdb_id', None)
    _send_notification(message, imdb_id)
    kodi.display_message("Couchpotato Event", message)
    return OK


@app.route('/sonarr2mail', methods=['POST'])
def sonarr2mail():
    print(request.json)
    print(request.form)
    return OK


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)







