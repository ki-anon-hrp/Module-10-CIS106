# Kirill M10P2 10/15/2026

# Define a function
def compute(lenght, width, height):
# Formula of finding square footage of the room and amount of gallons for painting a walls
    footage_room = (2 * lenght * height) + (2 * width * height)
    gallons_room = (footage_room / 50)
    return gallons_room

# Asking to continue program or stop
start = input("Do you want to repeatedly to do program (Yes / No): ")

# Begining of the loop 
while start == "Yes":
# Entering values of lenght, width, and height
    lenght = int(input("Enter lenght of the room: ")) 
    width = int(input("Enter width of the room: "))
    height = int(input("Enter height of the room: "))

# Calling for function compute
    gallons_room = compute(lenght, width, height)

# Printing final statment
    print(f"Number of gallons you need: {gallons_room} gal")

# Asking to continue program or stop
    start = input("Do you want to repeatedly to do program (Yes / No): ")
