import os
from art import logo
con=False
bidders={
  
}
def highest_bidder(bidding_record):
  highest_bid=0
  winner=''
  print(logo)
  for key in bidders:
    if bidders[key] > highest_bid:
      highest_bid=bidders[key]
      winner=key
  print('The winner is',winner ,'With the bid of',highest_bid,'$')
while con==False:
  print(logo)
  name=input("Whats the name of the bidder? ")
  bid=int(input("\nHow much you want to bid $ "))
  bidders[name]=bid
  con1=input("\nDo we have another bidder? Yes or No ")
  con1=con1.lower()
  os.cls()
  if con1=='no':
    con=True
    highest_bidder(bidders)