# Using the dictionary from the Nested dictionaries exercise above, 
ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [{'name': 'Jasmine','email': 'jasmine@yahoo.com','interests': ['photography', 'tennis']}, {'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': ['movies', 'tv']}]
}

# write a function countFriends() that accepts a dictionary 
# as an argument and returns a new dictionary that includes 
# a new key friends_count:

def countFriends(dict):
    friends = 0
    
    for item in dict['friends']:
        friends += 1
    dict['friends_count'] = friends
    return dict


countFriends(ramit)
print(ramit)




