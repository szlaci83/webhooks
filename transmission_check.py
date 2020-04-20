import transmissionrpc as t
from email_properties import Transmission as transmission_properties

tc = t.Client(**transmission_properties)
torrents = tc.get_torrents()
for t in torrents:
#    print(dict(__builtins__))
    print(t.name, t.date_added, t._status(), t.date_done)

