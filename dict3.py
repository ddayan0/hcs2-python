#Dennis Dayan
#dict3.py

def line():
    print('\n--------------------------------')

groceryStore = {
    1: {
        'itemName': 'Apple',
        'itemPrice': 6,
        'itemQuantity': 10

    },
    2: {
        'itemName': 'Yellow_Watermelon',
        'itemPrice': 12,
        'itemQuantity': 20
    },
    3: {
        'itemName': 'Void',
        'itemPrice': 000,
        'itemQuantity': 000

    },
    4: {
        'itemName': 'Watermelon',
        'itemPrice': 24,
        'itemQuantity': 40

    },
    5: {
        'itemName': 'Mango',
        'itemPrice': 48,
        'itemQuantity': 80


    },
}

grandtotal = 0

shoppingCart = []

def addToCart(itemNum, quant): #Shows how many of selected item left
    global shoppingCart
    for i in range (0, quant):
        shoppingCart.append(groceryStore[itemNum])
    groceryStore[itemNum]['itemQuantity'] = groceryStore[itemNum]['itemQuantity'] - quant
    print('We now have {} {}\'s left'.format(groceryStore[itemNum]['itemQuantity'],groceryStore[itemNum]['itemName']))

addToCart(1, 2)
line()
def mediumAddtoCart(itemName, howMany):
    additems = 0
    while(additems < howMany):
        for i in groceryStore:
            if groceryStore[i]['itemName'] == itemName:
                foundItem = i
                shoppingCart.append(groceryStore[i])
                groceryStore[i]['itemQuantity'] -= 1
                additems += 1
    print('We now have {} {}\'s left'.format(groceryStore[foundItem]['itemQuantity'], groceryStore[foundItem]['itemName']))
    print('We have purchased {} {}\'s '.format(howMany, groceryStore[foundItem]['itemName']))
mediumAddtoCart('Apple', 2)
line()
#BELOW IS FAULTY, FUNCTION DOES NOT GET CORRECT NUMBER OF ITEMS AND CORRECT TOTAL PRICE
#def checkOut():
    #global grandtotal
    #for i in shoppingCart:
        #n = i['itemName']
        #p = i['itemPrice']
        #q = i['itemQuantity']
        #a = p*q
    #print(str(n))
    #print(str(p)+ ' :Price')
    #print(str(q)+ ' :Quantity')
    #print(str(a)+ ' :Total')


#checkOut()

def otherCheckOut():
    global grandtotal
    for i in range(0, len(shoppingCart)):
        grandtotal += shoppingCart[i]['itemPrice']
        print('{}: {}'.format(shoppingCart[i]['itemName'], shoppingCart[i]['itemPrice']))
    print('Your total is ${}'.format(grandtotal))
line()
addToCart(3, 1)
addToCart(2, 3)
line()
otherCheckOut()

