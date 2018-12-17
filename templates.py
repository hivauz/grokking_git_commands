import os
#system agnostic
def get_template_path(path):
    file_path = os.path.join(os.getcwd(), path)
    if not os.path.isfile(file_path):
        raise Exception("this is not valid template")
    return file_path

file_ = 'templates/email_message.txt'


def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()

template = get_template(file_)
context = { "name":"Justing", "date":None, "total":None}

def render_context(template_string,context):
    return template_string.format(**context)



template_text = get_template(file_).format(name='justin', total= None)

print(render_context(template,context))
