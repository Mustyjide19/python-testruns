#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator")
Bill= float(input("what was the total bill? £"))
tip=int(input("How much tip would you like to give ? 10, 12, or 15? ")) 
people= int(input("How many people splitting bill ?"))
tip_as_percent = tip/100
total_tip_amount = Bill * tip_as_percent
total_Bill = Bill + total_tip_amount
Bill_per_person = total_Bill /people
final_amount = round(Bill_per_person , 2)
final_amount = "{:.2f}".format(Bill_per_person)
print(final_amount)
print(f"Each person should pay: £{final_amount}")

