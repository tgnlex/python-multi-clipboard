import sys 
import clipboard 
import json 
import xmltodict

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def list_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            print(data)
    except:
        print("could not find clipboard file")
def convert_xml(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        file = open("output.xml", "w")
        xmltodict.unparse(data, output=file)
        file.close()
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved.")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")
    elif command == "list":
        list_items(SAVED_DATA)   

    elif command == "convert_xml":
        convert_xml(SAVED_DATA)
        print("Data written to output.xml")

    else:
        print("unknown command")
else:
    print("Please pass exactly one command")