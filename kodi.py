import urllib.request as urllib2
from email_properties import HOST, PORT, USER, PASS

KODI_CONN_STRING = 'http://' + HOST +":" + str(PORT)

message_rpc =


def _send_to_kodi(json_rpc_data):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, KODI_CONN_STRING, USER, PASS)
    urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))
    conn = urllib2.Request(KODI_CONN_STRING + '/jsonrpc', headers={"Content-Type": "application/json"})
    res = urllib2.urlopen(conn, data=json_rpc_data).read()
    return res


def display_message(title, message):
    data = ('{"jsonrpc": "2.0",'
            ' "method": "GUI.ShowNotification",'
            ' "params": {"title": "%s", "message": "%s"},'
            ' "id": 1}'
            % (title, message)).encode()
    res = _send_to_kodi(data)
    return res


def refresh_video_library():
    _send_to_kodi('{"jsonrpc": "2.0", "method": "VideoLibrary.Scan", "id": "1"}'.encode())


if __name__ == '__main__':
    r = display_message("Test", "This is a test")
    print(r)
    r = display_message("Test", "This is a test")
    print(r)
