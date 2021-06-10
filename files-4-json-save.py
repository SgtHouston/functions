# JSON = Javascript Object Notation
import json 

superhero = {
    "name": "Wonder Woman",
    "alias": "Diana Prince",
    "gear": [
        "Lasso of Truth",
        "Bracelets of Submission"
    ],
    "vehicle": {
        "title": "Invisible Jet",
        "speed": "2000 mph",
    }
}

with open('superhero.json', 'w') as file_handle:
    json.dump(superhero, file_handle)