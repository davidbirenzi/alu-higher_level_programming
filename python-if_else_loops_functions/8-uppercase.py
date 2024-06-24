#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    print("{}".format(result))
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
