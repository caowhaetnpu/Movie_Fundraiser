#function goes here
def string_check(choice, options):
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
    ["yes", "y"]
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
if check_snack == "Yes":

    desired_snack = ""
    while desired_snack != "xxx":
        # ask user for desired snack and put it in lowercase
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        # check if snack is valid
        snack_choice != "xxx" and snack_choice != "invalid choice":
        print("Snack Choice: ", snack_choice)

        # add snack to list

        # check if that snack is not the exit code before adding
        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append(snack_choice)

# Show snack orders
print()
if len(snack_order) == 0:
    print("Snacks Ordered: None")

else:
    print("Snacks ordered: ")

    for item in snack_order:
        print(item)