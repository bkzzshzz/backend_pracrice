# Dictionary with one key mapped to one value
phonebook = {
    "James" : '9812345679',
    "Ryan"  : '9888787878',
    "Harry" : '9878457845',
    "Gary"  : '9845789865',
    "Tony"  : '9878456532',
}

print(phonebook['James'])

#Dictionary mapped wth one key to different values
phonebook_address = {
    'James'     :   ['9898989898', 'Arizona'],
    'Maddie'    :   ['9845659879', 'Texas'],
    'Zeno'      :   ['7845789865', 'Ohio'],
    'Herald'    :   ['4556122345', 'Kansas']       
}

print(phonebook_address['Herald'])
print(phonebook_address['Herald'][0])
print(phonebook_address['Herald'][1])