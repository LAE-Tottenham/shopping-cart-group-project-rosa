
    #25
    # print('Please select what you would like to buy')
    #items_to_buy = start_sh
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
        return "{:.2f}".format(start_shop.total)
price = start_shop()





thisdict = {
"usd" :	1.0903,
"yen" :	162.85,	
"lev" :	1.9558,	
"koruna" :	25.242,	
"D krone" :	7.4610,	
"sterling" :	0.83355,	
"forint" :	400.48,
"zloty" :	4.2938,	
"leu" :	4.9758,
"S krona" :	11.3010,	
"franc" :	0.9401,
"krona" :	149.30,	
"N krone" :	11.7660,	
"lira" :	37.3517,
"A dollar" :	1.6236,	
"real" :	6.0949,
"C dollar" :	1.5063,	
"renminbi" :	7.7574,
"HK dollar" :	8.4690,	
"rupiah" :	16927.02,
"shekel" :	4.0905,
"I rupee" :	91.6220,	
"won" :	1482.73,
"M peso" :	21.2097,	
"ringgit" :	4.6986,	
"Z dollar" :	1.7902,	
"S dollar" :	1.4271,	
"baht" :	36.345,	
"rand" :	19.1651
}
price = float(price)
def currency():
    print(price, " in pounds")
    if (input(f"Would you like to convert this to another currency? (y/n) ")) == "y":
        os.system("clear")
        c = input("what currency would you like to convert to?\n")
        eut = price *1.19451
        if c == "euro":
            print(eut)
        if c in thisdict:
            a = (thisdict[c]*eut)
            print (a)
        eut = eut*thisdict[c]

currency()






