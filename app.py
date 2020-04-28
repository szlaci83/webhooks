from flask import Flask, jsonify, request, make_response
from mail_service import send_cp_mail_to_all, send_sonarr_mail_to_all
from imdb_service import get_poster
import kodi_service as kodi
import logging

app = Flask(__name__)

IMDB = "https://www.imdb.com/title/%s"


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
    return OK()


@app.route('/sonarr2mail', methods=['POST'])
def sonarr2mail():
    data = request.json
    with open("data.json", "a") as f:
        f.write(data)
    event = data["eventType"]
    series = data.get("series", {})
    episodes = data.get("episodes", [])
    msg = ""
    for ep in episodes:
        msg = msg + "%s : S%sE%s-%s %s\n" % \
              (series.get("title", ""),
               ep.get("seasonNumber", ""),
               ep.get("episodeNumber", ""),
               ep.get("title", ""),
               event
               )
    send_sonarr_mail_to_all(msg)
    return OK()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)

# {
#   'eventType': 'Test',
#   'series': {
#              'title': 'Test Title',
#              'tvdbId': 1234,
#              'id': 1,
#              'path': 'C:\\testpath'}
#    , 'episodes': [{'qualityVersion': 0, 'title': 'Test title', 'seasonNumber': 1, 'id': 123, 'episodeNumber': 1}]}





