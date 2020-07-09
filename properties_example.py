import os

FROM_ADDR  = os.environ.get('EMAIL_ADDRESS')
PW = os.environ.get('EMAIL_PASSWORD')
TEST_EMAIL =os.environ.get('MY_EMAIL') 
ADDRESSES=os.environ.get('NOTIFICATION_ADDRESSES', '').split(',')

# KODI
KODI_PORT = 8080
KODI_HOST = os.environ.get('KODI_HOST')

Kodi_conn = {
    'realm': None,
    'uri': 'http://' + KODI_HOST + ":" + str(KODI_PORT),
    'user': 'kodi',
    'passwd':'' 
}

# Transmission
Transmission = {
    'address': 'localhost',
    'port': 9091,
    'user': os.environ.get('TRANSMISSION_USER'),
    'password': os.environ.get('TRANSMISSION_PASSWORD')
}

HEADER_TR ="Transmission Event"
SUBJECT_TR_STOP = "Stopped seeding"
SUBJECT_TR_DOWNLOADED = "Downloaded torrent"

HEADER_CP = "Couchpotato event"
SUBJECT_CP = "Webhook"

HEADER_SONARR = "Sonarr event"
SUBJECT_SONARR= "Webhook"


if __name__ == '__main__':
    from pprint import pprint as p
    p(globals())


