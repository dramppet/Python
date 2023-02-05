import os

try:
    os.remove('proba.txt')
    print('File already deleted')
except FileNotFoundError as err:
    print(err)

