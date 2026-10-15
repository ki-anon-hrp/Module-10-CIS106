# Kirill M10P5 10/15/2026

# Define function
def compute_home(county, market_value):
# If statement with comparison of county and giving specific assessed value 
    if county == "Cook":
        assessed_value = 0.90
    elif county == "DuPage":
        assessed_value = 0.80
    elif county == "McHenry":
        assessed_value = 0.75
    elif county == "Kane":
        assessed_value = 0.60
    else: 
        assessed_value = 0.70

# Finding procent value by multiply market value on assessed value
    procent_value = market_value * assessed_value

# Finding final price by additing market value and procent value
    final_price = market_value + procent_value

    return assessed_value, procent_value, final_price

# Creating value for sum of all house values
total_value = 0.0

# Asking to continue program or stop
start = input("Do you want to repeatedly to do program (Yes / No): ")

# Begining of the loop
while start == "Yes":
# Entering county and market value
    county = input("Enter county: ")
    market_value = int(input("Enter market value of a home: "))

# Calling for function compute_home
    assessed_value, procent_value, final_price = compute_home(county, market_value)

# Additing in total value variable, final house price
    total_value += final_price

# Printing county, market value of the house, assessed value precent, assessed value of the house, and final market value of the house
    print(f"County: {county}")
    print(f"Market value of the house: ${market_value:,.2f}")
    print(f"Assessed value precent: %{assessed_value}")
    print(f"Assessed value of the house: ${procent_value:,.2f}")
    print(f"Final market value of the house: ${final_price:,.2f}")

# Asking to continue program or stop
    start = input("Do you want to repeatedly to do program (Yes / No): ")

# Printing final statement about sum of all house values
print(f"Total sum of all market value houses: ${total_value:,.2f}")