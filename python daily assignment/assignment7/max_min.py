
dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(dict.keys(), key=(lambda k: dict[k]))
key_min = min(dict.keys(), key=(lambda k: dict[k]))

print('Maximum Value: ',dict[key_max])
print('Minimum Value: ',dict[key_min])