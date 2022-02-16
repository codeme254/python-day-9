# blind auction program
from os import system, name 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 
  
all_bids = []
def add_to_dictionary_append_to_list(name, price):
    bid_dictionary = {}
    bid_dictionary["name"] = name
    bid_dictionary["price"] = price
    all_bids.append(bid_dictionary)

keep_going = True
while keep_going:
    name = input("What is your name: ")
    price = int(input("What is Your bid: "))
    add_to_dictionary_append_to_list(name=name, price=price)

    other_bidder = input("Is there any other bidder? type 'yes' or 'no': ").lower()
    if other_bidder == 'yes':
        clear()
    elif other_bidder == 'no':
        print("we will show the winner shortly")
        keep_going = False

best_bid = 0
for bid in all_bids:
    for val in bid:
        if bid["price"] > best_bid:
            best_bid = bid["price"]
            best_bidder = bid["name"]

print(f"{best_bidder} won, he bidded $ {best_bid}")