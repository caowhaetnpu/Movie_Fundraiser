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

    for var_list in valid_snacks:

        #if the snack is in one of the lists, return the full
        if desired_snack in var_list:

            # get full name of snacks and puts it
            # in title case so it looks nice when outputted
            snack = var_list[0].title()
            snack_ok = "yes"
            break

        # if the chosen snack is not valid, set snack_ok to no
        else:
            snack_ok = "no"

    # if snack is not ok - ask question again
    if snack_ok == "yes":
        print("Snack Choice: ", snack)
    else:
        print("invalid choice")















































