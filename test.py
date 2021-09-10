import re
import pandas
# functions

# checks the ticket is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)
# if name is not blank , program continues
        if response != "":
            return response
# if ticket is blank, shows error ( and repeats the loop)
        else:
            print(error_message)

def int_check(question):

    error = "Please enter a whole number between 12 and 130"
    valid = False
    while not valid:

#ask user for number and check it is valid
        try:
            response = int(input(question))


            if response <= 0:
                print(error)
            else:
                return response


# if an integer is not entered, display an error
        except ValueError:
            print(error)


def check_tickets(tickets_sold, ticket_limit):

        if tickets_sold < ticket_limit - 1:
            print("You have {} seats"
                  " Left".format(ticket_limit - tickets_sold))

        else:
            print("*** There is ONE seat left!!! ***")

        return ""

def get_ticket_price():

    age = int_check("Age: ")

    if age < 12:
        print("Sorry your are to young to see this movie")
        return "invalid ticket price"
    elif age > 130:
        print("That is very old - looks like that was a mistake")
        return "invalid ticket price"

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    return ticket_price


def string_check(choice, options):


    for var_list in options:

        is_valid = ""
        chosen = ""

        if choice in var_list:

            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        print("Please enter a valid option")
        print()
        return "invalid choice"


def get_snack():
    number_regex = "^[1-9]"

    valid_snacks = [
        ["popcorn", "p", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d"],
        ["Orange Juice", "oj", "j"],
    ]
    get_order = []
    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return get_order

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()
        snack_choice = string_check(desired_snack, valid_snacks)

        if amount >= 5:
            print("Sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

        snack_row.append(amount)
        snack_row.append(snack_choice)

        if snack_choice != "xxx" and snack_choice != "invalid choice":
            get_order.append(snack_row)



yes_no = [
    ["Yes", "y"],
    ["No", "n"]
]




MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

all_names = []
all_tickets = []

# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Tickets': all_tickets
}

while name != "xxx" and ticket_count < MAX_TICKETS:


    check_tickets(ticket_count, MAX_TICKETS)


    name = not_blank("Name: ",
                     "Sorry - this cant be blank,"
                     "Please enter your name?")

    if name == "xxx":
        break

    ticket_price = get_ticket_price()

    if ticket_price == "invalid ticket price":
        continue

    ticket_count += 1
    ticket_sales += ticket_price

    all_names.append(name)
    all_tickets.append(ticket_price)
    check_snack = "invalid choice"
    while check_snack == "invalid choice":
        want_snack = input("Do you want to order snacks? ").lower()
        check_snack = string_check(want_snack, yes_no)

    if check_snack == "Yes":
        get_order = get_snack()
    else:
        get_order = []

    print()
    if len(get_order) == 0:
        print("Snacks ordered: None")
    else:
        print("Snacks Ordered: ")

        '''for item in get_order:
            print(item)
    
    
            '''
        print(get_order)

movie_frame = pandas.DataFrame(movie_data_dict)
print(movie_frame)

ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

if ticket_count == MAX_TICKETS:
    print("You have reached max tickets")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
#what
