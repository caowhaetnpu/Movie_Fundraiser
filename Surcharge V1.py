import re
import pandas

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



pay_method = [
    ["cash", "ca"],
    ["credit", "cr"]
]

name = ''
while name != "xxx":
    name = input("Name: ")
    if name == "xxx":
        break

    how_pay = "invalid choice"
    while how_pay == "invalid choice":
        how_pay = input("Please choose a payment method (cash / credit)?").lower()
        how_pay = string_check(how_pay, pay_method)

    subtotal = float(input("Sub total? $"))

    if how_pay == "Credit":
        surcharge = 0.05 * subtotal
    else:
        surcharge = 0

    total = subtotal + surcharge

    print("Name {} | Subtotal: ${:.2f} | Surcharge: ${:.2f} |"
          "Total Payable: ${:.2f}".format(name, subtotal, surcharge, total))