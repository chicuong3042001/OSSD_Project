import json
import random
import time
import urllib
from urllib.parse import quote

from apps.home.utils import ErrorCode


class Utils:
    @staticmethod
    def YTB_API_KEY():
        return 'AIzaSyBQff7R7ksnqICKSj4dUB_dgAFBFbNxj9c'


    @staticmethod
    def graphFB():
        return "https://graph.facebook.com/"

    @staticmethod
    def avatarFBParam():
        return "/picture?height=500&width=500&access_token=6628568379%7Cc1e620fa708a1d5696fb991c1bde5662"


    @staticmethod
    def cut_string_start_end(original, start_string, end_string):
        result = original.split(start_string)
        if len(result) < 2:
            return ''
        if end_string not in result[1]:
            return ''
        return result[1].split(end_string)[0]

    @staticmethod
    def parse_json_fb(json_data):
        try:
            if 'for (;;);' in json_data:
                json_data = json_data.replace('for (;;);', '')

            try:
                data_json = json.loads(json_data)
                return data_json
            except json.JSONDecodeError:
                json_data = json_data.split('\n')
                result = [json.loads(val) for val in json_data]
                if len(result) == 1:
                    return result[0]
                return result
        except Exception as error:
            raise error

    @staticmethod
    def make_id(length: int) -> str:
        result = ''
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        for _ in range(length):
            result += random.choice(characters)
        return result

    @staticmethod
    def get_numeric_value(a: str) -> str:
        c = 0
        for char in a:
            c += ord(char)
        return '2' + str(c)

    @staticmethod
    def make_number(length: int) -> str:
        characters = '0123456789'
        return ''.join(random.choice(characters) for _ in range(length))

    @staticmethod
    def getSpinT():
        return round(time.time())

    @staticmethod
    def get_logging_interaction_key1():
        pattern = "xxxxxxxx-xxxx-1xxx-yxxx-xxxxxxxxxxxx"
        split = list(pattern)
        for i in range(len(split)):
            b = random.randint(0, 15)
            char = split[i]
            if char != '1' and char != '-':
                if char == 'x':
                    a = b
                else:
                    a = b & 3 | 8
                split[i] = hex(a)[2]
        result = ''.join(split)
        return result
