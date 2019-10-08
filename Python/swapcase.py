"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s):
    w = [l for l in s]
    result = []
    for letter in w:
        if letter.isupper():
            result.append(letter.lower())

        elif letter.islower():
            result.append(letter.upper())
        else:
            result.append(letter)

    result = "".join(result)
    return result


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)