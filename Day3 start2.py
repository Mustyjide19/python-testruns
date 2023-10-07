print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster") 
  age= int(input("what's your age ?"))
  if age >= 18:
    print("Please pay 7 pounds")
  elif age <12:
    print ("Please pay 5 pounds")
  else:
    print("Please pay 12 pounds")
else:
  print("You can't ride the rollercoaster,Go grow taller")
