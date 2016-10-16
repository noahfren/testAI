#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'aaeb284ed9c14a80ada5f99c0ae0d579'
SESSION_ID = "arbitrary-session-id-string-waddup"


def main():

    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    while True:

        request = ai.text_request()

        request.lang = 'en'  # optional, default value equal 'en'

        request.session_id = SESSION_ID

        arg = input("ApiAI> ")

        if arg == "quit":
            print("Bye")
            break

        request.query = arg

        response = request.getresponse()

        resp = json.loads(str(response.read().decode('utf-8')))

        if resp["result"]["fulfillment"]["speech"]:
            print(resp["result"]["fulfillment"]["speech"])
        else:
            print("No response")

if __name__ == '__main__':
    main()