import re

def find_word(text, word):
    info = {'result': False,
            'first_index': None,
            'last_index': None,
            'search_string': None,
            'string': None
            }
    match = re.search(word, text)
    
    print(match)
    if match:
        info['result'] = True
        info['first_index'] = match.span()[0]
        info['last_index'] = match.span()[1]
        info['search_string'] = match.group()
        info['string'] = match.string
 #   else:
 #       info['search_string'] = match.group()
 #       info['string'] = match.string
     
    return info

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))