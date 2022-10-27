import requests
import ssl
import re

def main():
    r = requests.post(url='example.com', data='', headers='headers', verify=False)
    context = ssl._create_unverified_context()
    r2 = requests.post("https://127.0.0.1/login", verify=False, data=data, headers=headers)
    string_a = "abcdefg"
    regex = re.search("/A(B+|C)*D/", string_a)


if __name__ == '__main__':
    main()
