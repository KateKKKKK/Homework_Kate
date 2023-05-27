
import re

string = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
pattern = re.compile(r"([a-zA-Z]+)=([a-zA-Z-?0-9]+)")
dict_result = dict(pattern.findall(string))
print(dict_result)

camel_case = ["FirstItem", "FriendsList", "MyTuple"]
snake_case = []

for name in camel_case:
    converted_name = ""
    for i, letter in enumerate(name):
        if letter.isupper() and i > 0:
            converted_name += "_" + letter.lower()
        else:
            converted_name += letter.lower()
    snake_case.append(converted_name)
print(snake_case)


import re

text = "The Hubble.Space.Telescope (often referred to as HST or Hubble) is a space telescope that was launched into low Earth orbit in 1990 and remains in operation.... It was not the first space telescope, but it is one of the largest and most versatile, renowned both as a vital research tool and as a public relations boon for astronomy. The Hubble telescope is named after astronomer Edwin Hubble and is one of NASA's Great Observatories..... The Space Telescope Science Institute (STScI) selects Hubble's targets and processes the resulting data, while the Goddard Space Flight Center (GSFC) controls the spacecraft.A commission headed by Lew Allen, director of the Jet Propulsion Laboratory, was established to determine how the error could have arisen. The Allen Commission found that a reflective null corrector, a testing device used to achieve a properly shaped non-spherical mirror, had been incorrectly assembled—one lens was out of position by 1.3 mm (0.051 in)."
sentences = re.split(r'(?<=[.!?…])(?:\.{2,}|)\s+(?=[A-Z])', text)
print(sentences)

import re

html = '''
<link id="google" href="http://www.google.com">Google</a>
<link id="facebook" href="http://facebook.com/dign-in">Facebook</a>
<link id="amazon" href="amazon.com">Amazon</a>
'''

pattern = r'<link id="(.*?)" href="(.*?)">(.*?)</a>'
matches = re.findall(pattern, html)

links = [(id_, href, text) for id_, href, text in matches]
print(links)
