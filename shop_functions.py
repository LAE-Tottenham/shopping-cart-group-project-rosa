import os
itemdict = {
    'Bread': 1.20,
    'Milk': 1.20,
    'Chocolate': 0.50,
    'Eggs': 0.13,
    'Water': 1.00,
    'Crisps': 0.50,
    'Chicken Wings': 0.20,
    'Watermelon': 3.50,
    'Bananas': 1.50,
    'Grapes': 1.50
}

def start_shop():
        itemlist = []
        pricelist = []
        start_shop.total = 0
        os.system("clear")
        print("What you would like to buy? ")
        print(itemdict)
        while True:
            items = input("Select your items one by one please, and say 'finished' when you're done choosing.\n")
            items2 = items.title()
            if items2 in itemdict:
                 os.system("clear")
                 while True:
                      number = input("How many of this item would you like?\n")
                      if number.isdigit():
                          os.system("clear")
                          print("OK. It's been added to your basket.") 
                          numberint = int(number)
                          for i in range(numberint):
                               itemlist.append(items2)
                          break
                      else:
                           os.system("clear")
                           print("Please enter a suitable number of the item you would like.")
                           continue
                 continue
            elif items.lower() == "finished":
                os.system("clear")
                print("OK. I will calculate your total bill now.")
                break
            else:
                 os.system("clear")
                 print("Thats not an option. Please pick one of our available products.")
        for u in itemlist:
             price = itemdict.get(u)
             pricelist.append(price)
        for i in pricelist:
             start_shop.total = start_shop.total + i
        os.system("clear")
        return "Your total is: €" + "{:.2f}".format(start_shop.total)
x = start_shop()
print(x)
print(start_shop.total)

        