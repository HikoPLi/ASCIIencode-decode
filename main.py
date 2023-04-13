import osIdentify
import urlCodeDecode


def main():
    string = str(osIdentify.platForm())
    print(urlCodeDecode.urlIncode(string))
    decode = urlCodeDecode.urlDecode(urlCodeDecode.urlIncode(string))
    print(decode)


if "_main_" == "_main_":
    main()
