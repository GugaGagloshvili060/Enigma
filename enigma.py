from rotor import *

def shift_dict_values(d):
    keys = list(d.keys())
    values = list(d.values())
    shifted_values = values[-1:] + values[:-1]

    return dict(zip(keys, shifted_values))

def make_bidirectional(d):
    result = {}
    for k, v in d.items():
        result[k] = v
        result[v] = k
    return result


def get_key_by_value(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return ''

def enigma(rotorX, rotorY, rotorZ, swaped_to):
    swaped_to = make_bidirectional(swaped_to)
    text = (input('Provide the text that should be encrypted\n')).lower()
    encrypted_text = ''
    i = 0
    x = 0
    for char in text:
        if char == ' ':
            encrypted_text += ' '
            continue

        rotorX = shift_dict_values(rotorX)
        i += 1
        if i == 26:
            rotorY = shift_dict_values(rotorY)
            i = 0
            x += 1
        if x == 26:
            rotorZ = shift_dict_values(rotorZ)
            x = 0

        if char in swaped_to:
            char = swaped_to[char]


        rotorX
        char = rotorX[char]
        char = rotorY[char]
        char = rotorZ[char]

        # Reflector
        char = reflector[char]

        char = get_key_by_value(rotorZ, char)
        char = get_key_by_value(rotorY, char)
        char = get_key_by_value(rotorX, char)


        if char in swaped_to:
            char = swaped_to[char]

        encrypted_text += char

    return encrypted_text

