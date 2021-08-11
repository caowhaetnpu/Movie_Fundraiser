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


# loop to get ticket details
max_tickets = 5
name = ""
ticket_count = 0
ticket_sales = 0


while name != "quit" and ticket_count < max_tickets:

    name = not_blank("Name: ",
                     "Sorry - this cant be blank,"
                     "Please enter your name?")
    if name == "quit":
        break

# get age between 12 - 130
    age = int_check("Age:")
# check that age is valid
    if age < 12:
        print("Sorry your are to young to see this movie")
        continue
    elif age > 130:
        print("That is very old - looks like that was a mistake")
        continue

    if age < 16:
        ticket_price = 7.5
    elif age < 65:
        ticket_price = 10.5
    else:
        ticket_price = 6.5

    ticket_count += 1
    ticket_sales += ticket_price
# calculate ticket profit
ticket_profit = ticket_sales - (5 * ticket_count)
print("Ticket profit: ${:.2f}".format(ticket_profit))

if ticket_count == max_tickets:
    print("You have reached max tickets")
else:
    print("You have sold {} tickets. \n"
          "There are {} places still available"
          .format(ticket_count, max_tickets - ticket_count))
