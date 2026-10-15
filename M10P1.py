# Kirill M10P1 10/15/2026

# Define function
def compute(month, sales):
# If statement with specific month and forecast percent
    if month in ("Jan", "Feb", "March"): 
        forecast_percent = 0.10
    elif month in ("Apr", "May", "Jun"):
        forecast_percent = 0.15
    elif month in ("Jul", "Aug", "Sep"):
        forecast_percent = 0.20
    elif month in ("Oct", "Nov", "Dec"):
        forecast_percent = 0.25
    else: 
        forecast_percent = 0.0

# Formula for value of the sales
    next_sales = sales * (1 + forecast_percent)
    return next_sales    

# Asking to continue program or stop
start = input("Do you want to repeatedly to do program (Yes / No): ")

# Begining of loop
while start == "Yes": 
# Entering last name, month, and sales
    last_name = input("Enter your last name: ") 
    month = input("Enter month: ")
    sales = int(input("Enter a sales: "))

# Calling for function compute
    next_sales = compute(month, sales)

# Printing final result
    print(f"Last name: {last_name}")
    print(f"Month enter: {month}")
    print(f"Compute value: {next_sales:,.2f}")

# Asking to continue the pgoram
    start = input("Do you want to repeatedly to do program (Yes / No): ")
