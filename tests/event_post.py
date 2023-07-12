# Author: Sakthi Santhosh
# Created on: 14/01/2023
def main() -> int:
    from base64 import b64encode
    from json import dumps
    from requests import post
    from requests.exceptions import ConnectionError
    from uuid import uuid4

    from constants import URL

    try:
        DATA = {
            "device_id": "99060525-a02a-4870-b336-69b638ef4104",
            "image": b64encode(open("./tests/test.jpg", "rb").read()).decode("utf-8"),
            "prediction": 0.812345
        }

        request_handle = post(
            url=URL + "add_event",
            data=dumps(DATA),
            headers={"Content-Type": "application/json"}
        )

        print("Response:", request_handle.status_code)
        request_handle.close()
    except FileNotFoundError:
        print("Error: Image file not found.")
        return 1
    except ConnectionError:
        print("Error: Failed to establish a new connection to \"%s\"."%(URL))
        return 1
    except:
        print("Error: Something went wrong.")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
