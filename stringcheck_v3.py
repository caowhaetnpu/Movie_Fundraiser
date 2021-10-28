#function goes here
def string_check(choice, options):

    for var_list in options:

        #if the snack is in one of the lists, return the full
        if choice in var_list:

            # get full name of snacks and puts it
            # in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            is_valid = "no"

    # if snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


#  valid snacks holds list of all snacks
#  Each item in valid snacks is a list with
#  Valid options for each snacks <full name, letter code (a - e)>

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
]

# intitialise variables
snack_ok = ""
snack = ""


# for loop three times to make testing quicker

for item in range(0, 3):

    #ask user for desired snack and put it in lowercase
    desired_snack = input("Snack:").lower()

    #check if snack is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack Choice:", snack_choice)




