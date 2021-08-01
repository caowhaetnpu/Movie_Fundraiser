# Start of loop

# initialise loop so that it runs at least once
name = ""
count = 0
max_tickets = 5

while name!= "quit" and count < max_tickets:

# get details
    name = input("Name:")
    if name == "quit":
        break
    count += 1
    print()

if count == max_tickets:
    print("You Have Reached Max Tickets")
else:
    print("You have sold {} tickets.\n"
          "There are {} places still available"
          .format(count, max_tickets - count))
