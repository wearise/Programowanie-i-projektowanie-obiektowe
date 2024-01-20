# initialising dictionary
ini_dict = {'nikhil': 1, 'vashu': 5, 'manjeet': 10, 'akshat': 15}

# printing initial json
print("initial 1st dictionary", ini_dict)

# changing keys of dictionary
ini_dict['akash'] = ini_dict.pop('akshat')

# printing final result
print("final dictionary", str(ini_dict))
