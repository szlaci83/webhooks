import transmissionrpc as t
from datetime import datetime, timedelta
from properties import Transmission as transmission_properties

DEFAULT_LOOKBACK_MINS = 15
NCORE_SEED_HRS = 50
tc = t.Client(**transmission_properties)


def stop_seeding():
    stopped = []
    for torrent in tc.get_torrents():
        has_ncore_tracker = False
        for tracker in torrent.trackers:
            # stop seeding ncore torrents after 50 hours
            if tracker.get("announce", "").find("ncore") > 0:
                has_ncore_tracker = True
                if torrent.status == 'seeding' and torrent.date_done < datetime.now() - timedelta(hours=NCORE_SEED_HRS):
                    torrent.stop()
                    stopped.append(torrent)
            # stop seeding other torrents immediately
        if not has_ncore_tracker and torrent.status == 'seeding':
            torrent.stop()
            stopped.append(torrent)
    return stopped


def get_latest_finished(lookback_min=DEFAULT_LOOKBACK_MINS):
    return [t for t in tc.get_torrents() if t.date_done > datetime.now() - timedelta(minutes=lookback_min)]


if __name__ == '__main__':
    for t in get_latest_finished(4880):
        print(t.name)

