import base64

import json

import requests

from PIL import Image


# solve the json problems

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')

        return json.JSONEncoder.default(self, obj)


# class for request the card analysis

class OCR(object):

    # need a key

    def __init__(self, key, photo):
        self.key = key
        self.photo = photo

    def remote_call(self):
        # you owen key

        url = 'http://api.hanvon.com/rt/ws/v1/ocr/bcard/recg?key=%s&code=cf22e3bb-d41c-47e0-aa44-a92984f5829d' % self.key

        print(url)

        base64img = ""

        img = self.photo

        img = img.convert('L')

        _w = img.width

        _h = img.height

        img = img.resize((_w, _h), Image.ANTIALIAS)

        img.save('card_gray.jpg')

        # base64img需要是utf-8格式的字符串

        base64img = base64.b64encode(open('card_gray.jpg', 'rb').read())

        data = {"uid": '', "lang": 'auto', "color": 'color', "image": base64img}

        headers = {"Content-Type": "application/json"}

        resp = requests.post(url, data=json.dumps(data, cls=MyEncoder, indent=4), headers=headers)

        print(resp.text)

        return resp.json()
