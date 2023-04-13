import urllib
import base64
import urllib.parse


def urlIncode(str):

    urlCode = urllib.parse.quote(str)
    return urlCode


def urlDecode(urlCode):
    str = urllib.parse.quote(urlCode)
    return str
