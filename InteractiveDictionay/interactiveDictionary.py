import json
from difflib import get_close_matches
import sys

myDictionary = {
    "Aftermath": 'The consequences of an event, espcially a catastrophic one',
    "Money": 'A current medium of exchange in the form of coins and banknotes; coins and banknotes collectively',
    "Collectively": 'As a group; as a whole',
    "Discombobulated": 'Confused and disconcerted',
    "Organization": 'An organized group of people with a particular purpose, such as a business or government department',
    "Confess": 'Admit that one has committed a crime or done something wrong',
    "Atmosphere": 'The envelope of gases surrounding the earth or another planet',
    "Engaged": 'Busy; occupied',
    "Unavailable": 'Not able to be used or obtained; not at someone\'s disposal',
    "Disposal": 'The action or process of getting rid of something',
    "Success": 'The accomplishment of an aim or purpose',
    "Architecture": 'The art or practice of designing and constructing buildings',
    "Practice": 'The actual application or use of an idea, belief, or method, as opposed to theories relating to it',
    "Opposed": 'Anxious to prevent or put an end to; disagreeing with',
    "Contrast": 'The state of being strikingly different from something else in juxtaposition or close association',
    "Mental": 'Relating to the mind',
    "Informal": 'Having a relaxed, friendly, or unofficial style, manner, or nature',
    "Denoting": 'Being a sign of; indicate',
    "Purity": 'Freedom from adulteration or contamination',
    "Especially": 'Used to single out one person or thing over all others'
    }

with open('myOwnDictionary.json', 'w') as json_file:
    json_file.write(json.dumps(myDictionary, indent=2, sort_keys=True))
    json_file.close()

with open('myOwnDictionary.json') as json_file:
    data = json.load(json_file)
    json_file.close()

def definition(name):
    if name in data:
        return data[name]

    elif len(get_close_matches(name, data.keys())) > 0:

        check = input("Wrong search!! Please try again \nDo you want to find a close match? Enter Y for Yes and N for No: ")

        if check == "y":
            print("%s" % get_close_matches(name, data.keys())[0])
            return data[get_close_matches(name, data.keys())[0]]
        elif check == "n":
            sys.exit()
        else:
            return "We did not understand your entry."

    else:
        return "Wrong search!! Please try again."

try:
    word = input("Enter the word you want to search: ")
    if word.isdigit():
        print("No numeric values allowed!")
        sys.exit()
except:
    sys.exit()

output = definition(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
