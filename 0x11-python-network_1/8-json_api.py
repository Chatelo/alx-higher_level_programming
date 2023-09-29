#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with...
 a letter as a parameter.The letter must be sent in the variable q.
If no argument is given, set q="".If the response body is properly JSON formatted and not empty,
it displays the id and name like this: [<id>] <name>. Otherwise, it displays appropriate error messages.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}

    try:
        response = requests.post("http://0.0.0.0:5000/search_user",
                                 data=payload)
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
    except Exception as e:
        print(e)
