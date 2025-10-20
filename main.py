from rotor import *
from enigma import *
swaped = (input('Provide the distinct characters that should be swapped\n')).lower()
swaped_to = (input('Provide the distinct characters that should swap the provided letters\n')).lower()
while len(swaped) != len(swaped_to):
    print('Information provided is not correct please check the letters\n')
    print(f'Letters that should be swaped --{swaped}\n')
    swaped_to = input('Please provide new letters\n')
rotors = (input('Name the three rotors that should be used space in between\n A, B, C, D, E\n')).lower()
rotors = rotors.split()
swaped_dict = {}
for x in range(0,len(swaped)):
    swaped_dict[swaped[x]] = swaped_to[x]

print(enigma(rotors_dict[rotors[0]],rotors_dict[rotors[1]],rotors_dict[rotors[2]], swaped_dict))








