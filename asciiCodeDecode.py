
def urlIncode(string):

    asciiCode = ""
    for i in string:

        asciiCode = asciiCode + str(ord(i)) + "/"

    return asciiCode
