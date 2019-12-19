import os

from flask import Flask, request

from dataset_visualize import dataset_visualize
from homepage import homepage
from dependency_visualize import dependency2html

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return homepage()

@app.route('/<dataset>', methods=['GET'])
def dataset_vis(dataset):
    print("route " + dataset)
    # FileNotFoundError: [Errno 2] No such file or directory: 'data/favicon.ico/format.txt'
    if dataset == 'favicon.ico':
        return ''
    return dataset_visualize()

@app.route('/<dataset>/<filename>', methods=['GET'])
def data_vis(dataset, filename):
    format_path = os.path.join('data', dataset, 'format.txt')
    if not os.path.exists(format_path):
        return "<h1> format.txt not exists </h1>"
    format_type = open(format_path, encoding='utf-8').read().strip()

    if format_type == 'UD':
        return dependency2html(os.path.join("data", dataset, filename))
    # elif format_type == 'amr':
        # return 'amr'
    else:
        return '<h1> format not support! </h1>'
    

if __name__ == "__main__":
    app.run()
