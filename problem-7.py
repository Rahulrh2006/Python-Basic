#ticket pricing 
age = 30
member = True

if age > 18:
    if member:
     print("Ticket price is $12.")
    else:
     print("Ticket price is $20.")
else:
    if member:
     print("Ticket price is $8.")
    else:
     print("Ticket price is $10.")
