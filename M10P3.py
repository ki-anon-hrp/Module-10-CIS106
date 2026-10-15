# Kirill M10P3 10/15/2026

# Define function
def compute_price(model, vechile_code, msrp):
# If statement with comparison of enter model and vechile code 
    if model == "Honda Accord":
        percent_off = 0.10
    elif model == "Toyota Rav4":
        percent_off = 0.15
    elif vechile_code.upper() == "Y":
        percent_off = 0.30
    elif vechile_code.upper() == "N":
        percent_off = 0.05
    else:
        percent_off = 0.0

# Finding discount amount 
    discoun_msrp = msrp * percent_off

# Finding msrp price with discount
    new_msrp = msrp - discoun_msrp

# Finding final msrp price with tax
    final_msrp = new_msrp + (new_msrp * 0.07)
 
    return discoun_msrp, percent_off, new_msrp, final_msrp

# Creating values for containing sum of msrp and final price
total_msrp_sum = 0.0
total_final_price = 0.0

# Asking to continue program or stop
start = input("Do you want to repeatedly to do program (Yes / No): ")

# Begining of the loop
while start == "Yes":
# Entering values of make, model, vechile code, and msrp
    make = input("Enter a vechile maker: ")
    model = input("Enter a model of the vechile: ")
    vechile_code = input("Enter electric vechile code (Y or N): ")
    msrp = int(input("Enter a MSRP of the vechile: "))

# Calling for function compute_price
    discoun_msrp, percent_off, new_msrp, final_msrp = compute_price(model, vechile_code, msrp)

# Additing into values sum of all msrp and sum of all prices
    total_msrp_sum += msrp
    total_final_price += final_msrp

# Printing statements aboit vechile, it msrp, discount and final price
    print(f"Vechile maker: {make}")
    print(f"Model: {model}")
    print(f"Electric vechile code: {vechile_code}")
    print(f"MSRP: ${msrp:,.2f}")
    print(f"Discount: ${discoun_msrp}")
    print(f"Final price wtih tax: ${final_msrp:,.2f}")

# Asking to continue program or stop
    start = input("Do you want to repeatedly to do program (Yes / No): ")

# Printing final statement with sum of all msrp and sum of all prices
print(f"Total sum of all MSRP: ${total_msrp_sum:,.2f}")
print(f"Total sum of all prices: ${total_final_price:,.2f}")