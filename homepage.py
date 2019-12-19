import os

from flask import request


def homepage():
    url_root = request.url_root
    data_list = []
    for directory in os.listdir('data'):
        full_path = os.path.join('data', directory)
        format_path = os.path.join(full_path, 'format.txt')
        if os.path.exists(format_path):
            data_list.append(directory)
    
    html = '<h1>choose a dataset</h1>'
    for data in data_list:
        url_ref = url_root + data
        html += '\n<a href=%s>%s</a>' % (url_ref, data)

    return html
