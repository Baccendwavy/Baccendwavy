# fishstore()take 2 string argument:fish and price
def fishstore(fish,price):
    # fishstore return a string in sentence form 
    return ("fish type: "+ fish.capitalize()+ "costs $" + price)
# gather input for fish_entry and price_entry 
fish_entry= input("enter fish type: ")
price_entry= input("enter fish type price: ")
print(fishstore(fish_entry, price_entry))