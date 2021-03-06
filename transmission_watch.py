import transmission_service as transmission
import kodi_service as kodi
import mail_service as mail
import imdb_service as imdb

PATTERN = '%r downloaded'
EVENT = "Transmission Event"


def notify_kodi(msg, update=True):
    kodi.display_message(EVENT, PATTERN % msg)
    if update:
        kodi.refresh_video_library()


def notify_dl_mail(msg, add_poster=False):
    res = imdb.get_poster_by_name(msg)
    if not res:
        mail.send_tr_dl_mail_to_all(msg, add_poster=False)
    else:
        mail.send_tr_dl_mail_to_all(msg, add_poster=add_poster)

def notify_stop_mail(msg, add_poster=False):
    mail.send_tr_stop_mail_to_all(msg, add_poster=False)
    


def check_downloaded():
    all_finished = transmission.get_latest_finished()
    if len(all_finished) == 0:
        return
    msg = all_finished[0].name if len(all_finished) == 1 else len(all_finished)
    print(msg)
    try:
        notify_kodi(msg)
    except Exception as e:
        print(str(e))
    for t in all_finished:
        try:
            notify_dl_mail(t.name, add_poster=True)
        except Exception as e:
            print(str(e))
            notify_dl_mail(t.name)


def stop_seeding():
    stopped = transmission.stop_seeding()
    if len(stopped) == 0:
        return
    msg = "STOP_SEEDING:\n" + "\n ".join([s.name for s in stopped])
    try:
        notify_kodi(msg)
    except Exception as e:
        print(str(e))
    notify_stop_mail(msg)


def main():
    check_downloaded()
    stop_seeding()


if __name__ == '__main__':
    main()

