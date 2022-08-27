import argparse
import string
import random

parser = argparse.ArgumentParser()
parser.add_argument("text")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-e", "--encode", action="store_true")
group.add_argument("-d", "--decode", action="store_true")

args = vars(parser.parse_args())


def rand_word(length: int, title_case: bool = False) -> str:
    tmp = ""
    for i in range(length):
        tmp += random.choice(string.ascii_lowercase)
    if title_case:
        tmp = tmp.title()
    return tmp


def encode(text: str) -> None:
    letter_list = list(text)
    for i in letter_list:
        if i == " ":
            print("!", end='')
        elif i in string.ascii_lowercase:
            idx = string.ascii_lowercase.index(i)
            print(rand_word(idx + 1) + "!", end='')
        elif i in string.ascii_uppercase:
            idx = string.ascii_uppercase.index(i)
            print(rand_word(idx + 1, title_case=True) + "!", end='')
        else:
            print("[!]Encode failed. Exclamatory only support letters from", string.ascii_letters)
            return


def decode(text: str) -> None:
    letter_list = text.split("!")
    for i in letter_list:
        if len(i) == 0:
            print(" ", end='')
        else:
            idx = len(i) - 1
            if not 0 <= idx <= 25:
                print("[!]Decode failed.")
            if i[0] in string.ascii_uppercase:
                print(string.ascii_uppercase[idx], end='')
            elif i[0] in string.ascii_lowercase:
                print(string.ascii_lowercase[idx], end='')


if args['encode']:
    encode(args['text'])

if args['decode']:
    decode(args['text'])
