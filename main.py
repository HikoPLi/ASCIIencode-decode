import json
import osIdentify
import asciiCodeDecode


def main():
    string = str(osIdentify.platForm())
    encode = asciiCodeDecode.urlIncode(string)
    print(encode)

    machineInfo = [
        {
            "Front ID": {
                "Basic Info": string,
                "ASCII Encode": encode
            },
            "Local ID": {
                "": ""
            }
        }]

    with open("ID.json", "w") as infoFile:
        jsonFile = json.dumps(machineInfo, indent=4)
        infoFile.write(jsonFile)


if "_main_" == "_main_":
    main()
