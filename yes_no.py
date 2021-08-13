# string checking functions, takes in
# question and list of valid responses

def string_checker(question, to_check):


    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
# checks if response is the first letter of
# an item in the list
                if response == item[0]:
                    return item

# Main routine goes here

for item in range(0,6):
    want_snacks = string_checker("Do you want snacks? ", ["yes", "no"])
    print("Answer Ok, you said:", want_snacks)
    print()











































































