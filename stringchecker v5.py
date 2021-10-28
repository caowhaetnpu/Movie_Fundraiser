import re

#function goes here
def string_check(choice, options):


    #regular expression to find if item starts with a number
    number_regex = "^[1-9]"




#  valid snacks holds list of all snacks
    #  Each item in valid snacks is a list with
    #  Valid options for each snacks <full name, letter code (a - e)>

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
    ]

    #valid options for yes or no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]
# holds snack order for a single user
snack_order = []

# ask user if they want a snack
check_snack = "invalid choice"
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks?").lower()
    check_snack = string_check(want_snack, yes_no)

# if they say yes, ask what snacks they want
if check_snack == "yes":
    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # if item has a number, seperate it into two (number / item)
        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]
        else:
            amount = 1
            desired_snack = desired_snack

        # remove white space around snack
        desired_snack = desired_snack.strip()

        # check if snack is valid
        snack_order = string_check(desired_snack, valid_snacks)

        # check snack amout is valid (less then 5)
        if amount >= 5:
            print("Sorry - we have a four snack maximum policy")
            snack_choice = "invalid choice"


        # add snack to list and amount to list...
        amount_snack = ("{}  {}".format(amount, snack_choice))

        # check if that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(amount_snack)

# Show snack orders
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")
else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)

