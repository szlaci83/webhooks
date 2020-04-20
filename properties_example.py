FROM_ADDR  = ""
PW = ""
SUBJECT =""
TEST_EMAIL = ""


# KODI
KODI_PORT = 8080
KODI_HOST = ''

Kodi_conn = {
    'realm': None,
    'uri': 'http://' + KODI_HOST + ":" + str(KODI_PORT),
    'user': 'kodi',
    'passwd': ''
}

# Transmission
Transmission = {
    'host': 'localhost',
    'port': 9091,
    'user': '',
    'password': ''
}
