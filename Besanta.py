# Be Santa!

# Write a program that simulates a visit to Santa,
gift_list = []
gift_adder = True

def gift_tracker(list):
    print('----------Gift List----------')
    gift_dict = {}
    count = 1
    for gift in gift_list:
        gift_dict[count] = gift
        print(f"[{count}]: {gift}")
        count += 1
        print('-----------------------')
    return gift_dict

# Ask the user what they want for Christmas (can be any number of items)

while gift_adder == True:
    add_gift = (str(input('Do you want to add a gift to your list? Type Yes or No: \n')).lower())
    
    if add_gift[0] == 'y':
        gift_request = input(str("What do you want for Christmas?: \n"))
        gift_list.append(gift_request)
        
    elif add_gift[0] == 'n':
        gift_adder = False
        
    else:
        print('Wrong Input, no gifts for you!\n')
        gift_adder = False
        exit
            



# Ask if they've been bad or good this year.
behavior = str(input('Have you been bad or good this year? Type Bad or Good: \n')).lower()
 
# Based on their response, return the appropriate statement:
# If they've been good, list the presents they'll receive.
# If they've been bad, tell them they can expect a lump of coal.

if behavior[0] == 'g':
    gift_tracker(gift_list)
else:
    print('Congratulations on your lump of coal!')


