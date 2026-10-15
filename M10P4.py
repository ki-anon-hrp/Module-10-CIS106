# Kirill M10P4 10/15/2026

# Define function
def compute_ticket(miles):
# If statement with comparison of miles
    if miles >= 30:
        ticket_price = 12
    elif miles >= 20 and miles <= 29:
        ticket_price = 10
    elif miles >= 10 and miles <= 19:
        ticket_price = 8
    else:
        ticket_price = 5

    return ticket_price

# Creating value for counting sum of all values
all_tickets = 0.0

# Asking to continue program or stop
start = input("Do you want to repeatedly to do program (Yes / No): ")

# Begining of the loop
while start == "Yes":
# Entering last name and miles from downtown
    last_name = input("Enter last name: ")
    miles = int(input("Enter miles from downtown Chicago: "))

# Calling for function compute_ticket
    ticket_price = compute_ticket(miles)

# Additing in all_tickets value of current ticket price
    all_tickets += ticket_price

# Printing statement last name, miles from downtown Chicago, and price of ticket
    print(f"Last name: {last_name}")
    print(f"Miles from downtown Chicago: {miles}")
    print(f"Price of ticket: ${ticket_price}")

# Asking to continue program or stop
    start = input("Do you want to repeatedly to do program (Yes / No): ")

# Printing sum of all tickets
print(f"Total sum of all tickets: ${all_tickets:,.2f}")