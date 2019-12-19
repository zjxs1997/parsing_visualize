import os
from flask import request

def dataset_visualize():
    path = request.path
    base_url = request.base_url
    full_path = os.path.join('data', path[1:])
    format_path = os.path.join(full_path, 'format.txt')
    file_format = open(format_path, encoding='utf-8').read()
    file_format = file_format.strip()
    
    html = '<h1> choose a file </h1>'
    html += '\n<p> dataset: %s, file type: %s </p>' % (path[1:], file_format)

    data_files = os.listdir(full_path)
    data_files = sorted(data_files)
    for file in data_files:
        if file == 'format.txt':
            continue
        url_ref = base_url + '/' + file
        html += '\n<a href=%s>%s</a>' % (url_ref, file)
    
    return html

