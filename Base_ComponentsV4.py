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

        # ask user for number and check it is valid
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
        print("Sorry you are to young to see this movie")
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
        ["popcorn", "p", "pop", "corn", "a"],
        ["M&M's", "m&m's", "mms", "m", "b", "mm"],
        ["pita chips", "chips", "pc", "pita", "c"],
        ["water", "w", "d", "h20"],
        ["Orange Juice", "oj", "j"],
    ]
    snack_order = []
    desired_snack = ""
    while desired_snack != "xxx" or desired_snack != "n":

        snack_row = []
        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            return snack_order

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
            snack_order.append(snack_row)


yes_no = [
    ["Yes", "y"],
    ["No", "n"]
]

pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

MAX_TICKETS = 5

name = ""
ticket_count = 0
ticket_sales = 0

all_names = []
all_tickets = []
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

snack_list = [popcorn, mms, pita_chips, water, orange_juice]

surcharge_mult_list = []

summary_headings = ["Popcorn", "M&M's", "Pita Chips", "Water",
                    "Orange Juice", "Snack Profit", "Ticket Profit",
                    "Total Profit"]
summary_data = []




# data frame dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets,
    'Popcorn': popcorn,
    'Water': water,
    'Pita Chips': pita_chips,
    'M&Ms': mms,
    'Orange Juice': orange_juice,
    'Surcharge_Multiplier': surcharge_mult_list
}

summary_data_dict = {
    'Item': summary_headings,
    'Amount': summary_data
}




price_dict = {
    'Popcorn': 2.5,
    'Water': 2,
    'Pita Chips': 4.5,
    'M&Ms': 3,
    'Orange Juice': 3.25
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

    snack_order = get_snack()

    for item in snack_list:
        item.append(0)

    for item in snack_order:
        if len(item) > 0:
            to_find = (item[1])
            amount = (item[0])
            add_list = movie_data_dict[to_find]
            add_list[-1] = amount

    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)?").lower()
        how_pay = string_check(how_pay, pay_method)

    if how_pay == "Credit":
        surcharge_multiplier = 0.05
    else:
        surcharge_multiplier = 0

    surcharge_mult_list.append(surcharge_multiplier)

movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index('Name')

movie_frame["Sub Total"] = \
    movie_frame['Ticket'] + \
    movie_frame['Popcorn']*price_dict['Popcorn'] + \
    movie_frame['Water']*price_dict['Water'] + \
    movie_frame['Pita Chips']*price_dict['Pita Chips'] + \
    movie_frame['M&Ms']*price_dict['M&Ms'] + \
    movie_frame['Orange Juice']*price_dict['Orange Juice']

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge_Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + \
    movie_frame["Surcharge"]

movie_frame = movie_frame.rename(columns={'Orange Juice': 'OJ',
                                        'Pita Chips': 'Chips',
                                        'Surcharge_Multiplier': 'SM'})
for item in snack_list:
    summary_data.append(sum(item))

snack_total = movie_frame['Snacks'].sum()
snack_profit = snack_total * 0.2
summary_data.append(snack_profit)


ticket_profit = ticket_sales - (5 * ticket_count)
summary_data.append(ticket_profit)

total_profit = snack_profit + ticket_profit
summary_data.append(total_profit)

summary_frame = pandas.DataFrame(summary_data_dict)

summary_frame = summary_frame.set_index('Item')

pandas.set_option('display.max_columns', None)

pandas.set_option('precision', 2)

print()
print("*** Ticket / Snack Information ***")
print("Note: for full details, please see the exel file called")
print()
print(movie_frame[['Ticket', 'Snacks', 'Sub Total',
                   'Surcharge', 'Total']])

print()

print("*** Snack / Profit Summary ***")
print()
print(summary_frame)



if ticket_count == MAX_TICKETS:
    print("You have reached max tickets")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, MAX_TICKETS - ticket_count))
# what
