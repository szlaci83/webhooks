'''
    Repository using html and txt templates to create e-mails 
'''


def create_mail(message, link):
    body, text = _get_from_template('cp')
    body = body.format(message=message, link=link)
    text = text.format(message=message, link=link)
    return body, text


def _get_from_template(template_name):
    with open('templates/' + template_name + '.html', 'r') as html_file:
        body = html_file.read().replace("\n", "")
    with open('templates/' + template_name + '.txt', 'r') as text_file:
        text = text_file.read()
    return body, text


def _example():
    print(create_mail("got", "link"))
    print(create_mail("", ""))


if __name__ == "__main__":
    _example()

