import transmission_service as transmission
import kodi_service as kodi
import mail_service as mail

PATTERN = '%r downloaded'

def main():
    all_finished = transmission.get_latest_finished(4800)
    if len(all_finished) == 0:
        return
    msg = all_finished[0].name if len(all_finished) == 1 else len(all_finished)
    kodi.display_message("Transmission Event", PATTERN % msg)
    kodi.refresh_video_library()
    msg = "\n".join(all_finished.name)
    mail.send_tr_mail_to_all(msg)


if __name__ == '__main__':
    main()

