"""
First of all i will create dictonaries to put the menu and its counter in it

secondly, i will print for the user all the menu
"""

menu=[
    {
        "name":"appetizers",
        "items": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
    },
    {
        "name":"Entrees",
        "items": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden"
        ],

    },
    {
        "name":"Desserts",
        "items": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],

    },
    {
        "name":"Drinks",
        "items": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ],
    },
]
print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
for i in menu:
    print(i['name'])
    print('----------')

    print(*i['items'], sep = "\n")

    print('----------')

print("""
***********************************
** What would you like to order? **
***********************************
""")

lists = [ sub['items'] for sub in menu ]
final_orders = []
element = str(input('>'))
while element !='quit':
    res1 = any(element in sublist for sublist in lists)
    if res1:
        final_orders.append(element)
        my_dict = {i:final_orders.count(i) for i in final_orders}
        # print(my_dict.get('Tea'))
        value=my_dict.get(element)
        print(f'** {value} order of {element} have been added to your meal **')
        element = str(input(''))
    elif res1==False:
        print(f'Unfortunatly!, We dont have {element} :(')
        break