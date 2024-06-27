import csv

def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    cookies = []
    with open(filepath, mode='r') as file:  
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Check for the existence of the extra credit fields and provide defaults if missing
            cookie = {
                'id': int(row['id']),
                'title': row['title'],
                'description': row['description'],
                'price': float(row['price'].replace('$', '').strip()),
                'sugar_free': row.get('sugar_free', 'no').strip().lower() in ['yes', 'y'],
                'gluten_free': row.get('gluten_free', 'no').strip().lower() in ['yes', 'y'],
                'contains_nuts': row.get('contains_nuts', 'no').strip().lower() in ['yes', 'y']
            }
            cookies.append(cookie)
    return cookies

def welcome():
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")

def get_dietary_restrictions():
    print("\nWe'd hate to trigger an allergic reaction in your body. So please answer the following questions:")
    nuts = input("Are you allergic to nuts? ").strip().lower() in ['yes', 'y']
    gluten = input("Are you allergic to gluten? ").strip().lower() in ['yes', 'y']
    sugar = input("Do you suffer from diabetes? ").strip().lower() in ['yes', 'y']
    return {'nuts': nuts, 'gluten': gluten, 'sugar': sugar}

def filter_cookies(cookies, restrictions):
    filtered_cookies = []
    for cookie in cookies:
        if restrictions['nuts'] and cookie['contains_nuts']:
            continue
        if restrictions['gluten'] and not cookie['gluten_free']:
            continue
        if restrictions['sugar'] and not cookie['sugar_free']:
            continue
        filtered_cookies.append(cookie)
    return filtered_cookies

def display_cookies(cookies):
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        print(f"#{cookie['id']} - {cookie['title']}")
        print(f"{cookie['description']}")
        print(f"Price: ${cookie['price']:.2f}\n")


def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    for cookie in cookies:
        if cookie['id'] == id:
            return cookie
    return None

def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    cookie = get_cookie_from_dict(id, cookies)
    if cookie:
        while True:
            try:
                quantity = int(input(f"My favorite! How many {cookie['title']} would you like? ").strip())
                if quantity > 0:
                    subtotal = quantity * cookie['price']
                    print(f"Your subtotal for {quantity} {cookie['title']} is ${subtotal:.2f}.")
                    return quantity
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return 0

def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    orders = []
    while True:
        cookie_id = input("Please enter the number of any cookie you would like to purchase (type 'finished' to end): ").strip().lower()
        if cookie_id in ['finished', 'done', 'quit', 'exit']:
            break
        try:
            cookie_id_int = int(cookie_id)
            cookie = get_cookie_from_dict(cookie_id_int, cookies)
            if cookie:
                quantity = solicit_quantity(cookie_id_int, cookies)
                if quantity > 0:
                    orders.append({'id': cookie_id_int, 'quantity': quantity})
            else:
                print("Invalid cookie ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return orders

def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.

    :param order: A list of dictionaries, where each dictionary contains 'id' and 'quantity' of a cookie.
    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    if order:
        print("Thank you for your order. You have ordered:")
        total_price = 0
        for item in order:
            cookie = get_cookie_from_dict(item['id'], cookies)
            quantity = item['quantity']
            subtotal = cookie['price'] * quantity
            total_price += subtotal
            print(f"- {quantity} {cookie['title']} (Subtotal: ${subtotal:.2f})")
        print(f"Your total is ${total_price:.2f}.")
        print("Please pay with Bitcoin before picking-up.")
    else:
        print("You didn't order any cookies.")

    print("Thank you!\n-The Python Cookie Shop Robot.")

def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    welcome()
    restrictions = get_dietary_restrictions()
    filtered_cookies = filter_cookies(cookies, restrictions)
    display_cookies(filtered_cookies)
    order = solicit_order(filtered_cookies)
    display_order_total(order, cookies)