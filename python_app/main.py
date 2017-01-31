from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
import urllib.request
import random, string

from classify_image import *

app = Flask("TensorflowMircoserviceAPI", static_folder="./static")
app.config["JSON_SORT_KEYS"] = False

HTTP_ERROR_CLIENT = 422
HTTP_ERROR_SERVER = 500
HTTP_OK = 200

def random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/classify', methods=['GET'])
def visualize_account_api():
    if 'link' not in request.args or request.args['link'] in ("", None):
        return make_response(jsonify({'error': 'parameter \'link\' is missing'}), HTTP_ERROR_CLIENT)

    try:
        link = request.args.get('link', '')
        if link == '':
            print("Empty link!")
            return app.send_static_file('index.html')
        image_name = random_word(5) + '.jpg'
        urllib.request.urlretrieve(link, image_name)
        classification = run_inference_on_image(image_name)
    except Exception as ex:
        return make_response(jsonify({'error': str(ex)}), HTTP_ERROR_SERVER)

    response = make_response(jsonify(classification), HTTP_OK)
    os.remove(image_name)
    return response


if __name__ == '__main__':
    app.run()
