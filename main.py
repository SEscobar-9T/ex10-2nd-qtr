# working with dictionary
from pyscript import display


hiragana = {
    'morning' : 'ohayougozaimasu',
    'afternoon' : 'konnichiwa',
    'evening' : 'konbanwa'
} # specifying dictionaries

display(hiragana, target='output1')
display(f'{hiragana['morning']}!', target='output1') # accessing

keys = ['first_name', 'last_name', 'age']
values = ['Megan', 'Skiendiel', 19]

kats1 = dict(zip(keys, values)) # convert and combine
display(kats1, target='output2')

kats = {
    'Leader' : 'Sophia',
    'Visual' : 'Manon',
    'Main Vocalist' : 'Lara',
    'All Rounder' : 'Megan',
    'Maknae' : 'Yoonchae'
}

kats['Main Dancer'] = 'Daniela' # adding
del kats['Visual'] # delete
display(kats, target='output3')
display(kats | kats1, target='output3')