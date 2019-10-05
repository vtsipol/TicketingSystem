EXTRA_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

def calculate_function(number_of_tickets):
  return (ticket_amount * TICKET_PRICE) + EXTRA_CHARGE

while tickets_remaining >=1:
  print("There are {} tickets remaining".format(tickets_remaining)) 
  username = input("What is your name?    ") 
  print("Hey {}!".format(username))
  ticket_amount = input("How many tickets would you like, {}?    ".format(username)) 
  try:
    ticket_amount = int(ticket_amount)
    if ticket_amount > tickets_remaining:
      raise ValueError("There are only {} tickets remaining. Hurry up!".format(tickets_remaining))
  except ValueError as err:
    print("Oh no, we ran into an issue. {} Please try again!".format(err))
  else:
    total_price = calculate_function(ticket_amount)
    print("The total price is ${}".format(total_price))
    answer = input("Do you want to proceed?  Y/N  ")
    if answer.lower() == "y":
      print("SOLD!")
      tickets_remaining -= ticket_amount
    else:
      print("Thank you {}!".format(username))
else:
  print("Sorry! Tickets are sold out.")    