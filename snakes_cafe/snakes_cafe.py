"""
First of all i will create dictonaries to put the menu and its counter in it

secondly, i will print for the user all the menu
"""

menu=[
    {
        "name":"appetizers",
        "items": [
            "wings",
            "cookies",
            "spring Rolls",
        ],
    },
    {
        "name":"entrees",
        "items": [
            "salmon",
            "steak",
            "meat Tornado",
            "a Literal Garden"
        ],

    },
    {
        "name":"desserts",
        "items": [
            "Ice Cream",
            "cake",
            "pie",
        ],

    },
    {
        "name":"drinks",
        "items": [
            "coffee",
            "tea",
            "unicorn Tears",
        ],
    },
]


def main_func():
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
element = input('>').lower()
print('edee',element)
while element !='quit':
    res1 = any(element in sublist for sublist in lists)
    if res1:
        final_orders.append(element)
        my_dict = {i:final_orders.count(i) for i in final_orders}
        # print(my_dict.get('Tea'))
        value=my_dict.get(element)
        print(f'** {value} order of {element} have been added to your meal **')
        element = input('>').lower()
    elif res1==False:
        print(f'Unfortunatly!, We dont have {element} :(')
        print('is there anything else?, if not please type quit')
        element = input('>').lower()
        


if __name__ == "__main__":
    main_func()
    