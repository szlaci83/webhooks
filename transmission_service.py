import transmissionrpc as t
from datetime import datetime, timedelta
from properties import Transmission as transmission_properties

DEFAULT_LOOKBACK_MINS = 15
tc = t.Client(**transmission_properties)


def get_latest_finished(lookback_min=DEFAULT_LOOKBACK_MINS):
    return [t for t in tc.get_torrents() if t.date_done > datetime.now() - timedelta(minutes=lookback_min)]


if __name__ == '__main__':
    for t in get_latest_finished(4880):
        print(t.name)

