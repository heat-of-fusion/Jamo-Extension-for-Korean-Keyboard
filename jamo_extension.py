from utils import *

def double_moum_merge(text):
    new_string = str()
    skip_flag = False

    for idx in range(len(text)):
        if skip_flag:
            skip_flag = False

            continue

        if text[idx : idx + 2] in list(double_moum_dict.keys()):
            new_string += double_moum_dict[text[idx : idx + 2]]
            skip_flag = True

            continue

        new_string += text[idx]

    return new_string

def double_moum_decomp(text):
    new_string = str()

    for idx in range(len(text)):
        if text[idx] in moum_decomp_dict.keys():
            new_string += moum_decomp_dict[text[idx]]

            continue

        new_string += text[idx]

    return new_string