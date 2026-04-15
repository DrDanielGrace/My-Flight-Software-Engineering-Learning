# Code to Build a Movie Ticket Booking Calculator

# Base ticket price in dollars
base_price = 15

# Customer details
age = 21
seat_type = 'Gold'    # Options: Premium, Gold, Standard
show_time = 'Evening' # Options: Evening, Matinee

# Check if user meets minimum age requirement to book
if age > 17:
    print('User is eligible to book a ticket')

# Evening shows require age 21 and above
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# Membership and weekend flags for discount/charge calculations
is_member = False
is_weekend = False

# Calculate membership discount
# User must be a member AND aged 21 or above to qualify
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Calculate extra charges
# Applied if it is a weekend OR an Evening show
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# Final booking eligibility check
# User must be 21+ OR (18+ with non-Evening show or membership)
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Calculate service charges based on seat type
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5    # Highest tier
    elif seat_type == 'Gold':
        service_charges = 3    # Mid tier
    else:
        service_charges = 1    # Standard tier
    print('Service charges:', service_charges)

    final_price = base_price + extra_charges + service_charges - discount
    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')
