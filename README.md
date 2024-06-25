[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15328953&assignment_repo_type=AssignmentRepo)
# Cookie Shop Assignment

Your assignment today is to create a virtual cookie shop. You will do this by writing code into a file named `cookie_shop.py`. Several function definitions are indicated in that file with documentation - you must complete these functions. Your program must use each of the functions indicated here to perform the tasks they are designed to perform.

A file named `main.py` is given to you. The code in this file must not be modified. You must write your code in `cookie_shop.py` such that running the `main.py` file runs the entire program.

**Extra credit** -
There is an advanced version of this assignment that you can optionally attempt. All extra credit requirements are indicated following the basic requirements. If doing the extra credit, be sure to...

1. Complete the basic assignment in the given file named `cookie_shop.py`. You can use the automated tests included in the given code to make sure your basic version works perfectly before proceeding.
2. Complete the extra-credit version in a separate file named `cookie_shop_extra_credit.py`. There are no automated tests to help you with this version. Feel free to update `main.py` to import your extra credit version, rather than the basic version, so you can run and debug it more easily.

## Cookie inventory

The cookie shop has an inventory of at least **10 different kinds of cookies**. A data file named `cookies.csv` is given within the `data` directory - feel free to add more cookies to it, but do not modify or remove any lines already in the file, unless you are doing the extra credit part of the assignment. Each cookie has a unique `id`, a `title`, `description`, and `price` associated with it.

### Extra credit

Each cookie is also marked as to whether it is `sugar free`, `gluten free`, or `contains nuts` for those with diabetes or allergies. You must add these fields to the existing lines within the given `cookies.csv` file. Do not otherwise modify any of the existing lines in this file.

## Welcome message

Running the program first shows a welcome message.

```
Welcome to the Python Cookie Shop!
We feed each according to their need.
```

### Extra credit

The welcome message additionally asks the user questions whether they have any allergies to nuts or gluten, and whether they are avoiding sugar.

Here is sample of the additional output for this version, including example responses from the user.

```
We'd hate to trigger an allergic reaction in your body. So please answer the following questions:

Are you allergic to nuts? yes
Are you allergic to gluten? no
Do you suffer from diabetes? yes
```

## List of cookies

The program then outputs a user-friendly list of the cookies in the shop.

Sample output:

```
Here are the cookies we have in the shop for you:

#1 - Basboosa Semolina Cake
This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
Price: $3.99

#2 - Vanilla Chai Cookie
Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
Price: $5.50

#3 - Fudge Strip Cookie
Everyone needs to experience this one ' with the flavors of a soft baked cookie the 'fudge stripe' is our excuse for adding the perfect amount of rich decadent chocolate.
Price: $5.78

#4 - Animal Cupcake
Go wild and choose from a set of animal faces or one animal face printed on edible sugar paper.
Price: $0.99
```

### Extra credit

Rather than showing all the cookies in the store, as the default version does, the extra credit version must output a user-friendly list of only those cookies that match the user's dietary needs.

For example, a user with a gluten allergy should be shown only those cookies without gluten. And likewise for sugar and nuts.

Sample output below:

```
Great! Here are the cookies without nuts or sugar that we think you might like:

#1 - Basboosa Semolina Cake
This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.
Price: $3.99

#4 - Animal Cupcake
Go wild and choose from a set of animal faces or one animal face printed on edible sugar paper.
Price: $0.99
```

## Taking orders

The user is then asked to enter the `id` number of any cookie he/she would like to purchase, as well as the quantity. The user must enter the number of the cookie and the quantity as integers (e.g. `4`).

Sample output, including example responses from the user:

```
Please enter the number of any cookie you would like to purchase: 4
My favorite! How many Animal Cupcakes would you like? 8
Your subtotal for 8 Animal Cupcakes is $7.92.
```

The user is prompted over-and-over to enter the `id` number of any aadditional cookie they would like to purchase until they type '`finished`'.

When the ordering is finished, the total price is displayed.

```
Please enter the number of any other cookie you would like to purchase (type "finished" if finished with your order): finished

Thank you for your order. You have ordered:

-8 Animal Cupcake
-1 Basboosa Semolina Cake

Your total is $11.91.
Please pay with Bitcoin before picking-up.

Thank you!
-The Python Cookie Shop Robot.
```

## Parsing the data file

Except for the first line, which contains field headings, each line in the `cookies.csv` data file contains information about one cookie. The program must read the data from this file once at the beginning of running the program, and store the data found in the file into the appropriate data structures in the memory of the program.

The subsequent sections in this document explain the appropriate data structures to use.

## One dictionary per cookie

The data for each cookie must be stored as a dictionary. The dictionary must have keys for `id`, `title`, `description`, and `price`.

- The value of '`id`' must be an Integer.
- The value of '`title`' must be a String.
- The value of '`description`' must be a String.
- The value of '`price`' must be a Float with two decimal points.

For example, here is what a dictionary with data for one cookie would look like, if the values were written as literals in the code, rather than pulled from the data file:

```python
{
  'id': 1,
  'title': 'Basboosa Semolina Cake',
  'description': "This is a This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.",
  'price': 3.99
}
```

### Extra credit

- The dictionary must also have additional keys for '`sugar_free`', '`gluten_free`', and '`contains_nuts`'. Each should have a boolean value associated with it.

## Dictionaries stored in a list

All dictionaries representing individual cookies must be stored together as elements in a list. In other words, there is a single list that contains all the 10 or more cookie dictionaries.

For example, here is what the list with data for all cookies would look like, if the values were written as literals in the code, rather than pulled from the data file:

```python
[
  {
    'id': 1,
    'title': 'Basboosa Semolina Cake',
    'description': "This is a This is a traditional Middle Eastern dessert made with semolina and yogurt, then soaked in a rose water syrup.",
    'price': 3.99
  },
  {
    'id': 2,
    'title': 'Vanilla Chai Cookie',
    'description': "Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner, a combination of cinnamon, ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?",
    'price': 5.50
  },
  # and so on...
]
```

## User input validation

All user input data must be validated. If the user enters inappropriate data, the program must response by repeating the request for input. Data to validate includes:

- The `id` number of the cookie the user would like to order must be entered as an integer (e.g. `4`). This integer must be an actual `id` for a cookie in the cookie shop.
- The quantity of an ordered cookie must be an integer.
- The words '`finished`', '`done`', '`quit`', or '`exit`' in response to the request for the user to enter an additional cookie `id` must trigger the program to stop asking the user for more orders and continue to show them the total price for their order.

### Extra credit

- The response to questions about allergies or diabetes must be either '`yes`', '`y`', '`no`', or '`n`'.

If you are completing the extra credit version, you must send this fact as a message to the graders.

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "`Source Control"` and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)

Helpful video:

- [Submitting work from Visual Studio Code to GitHub](https://www.youtube.com/watch?v=ePIOee1D8Js&list=PL-DdwrWUDZnMCYaUqegGMPKDVJcPn-QJm&index=1)
