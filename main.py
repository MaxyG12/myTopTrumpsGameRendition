print ("TOP TRUMPS")
print ("----------")
print ()
print ("Welcome to the Top Trumps 'Most Legendary Avenger' Simulator")
print ()
# Create a dictionary for the card
card = {"Thanos": {"Intelligence": 100, "Handsomeness": 10, "L33t c0ding skillz": 100, "Baldness level": 0}}
# Create a dictionary for the card
card2 = {"Black Panther": {"Intelligence": 200, "Handsomeness": 20, "L33t c0ding skillz": 200, "Baldness level": 0}}
# Create a dictionary for the card
card3 = {"Thor": {"Intelligence": 300, "Handsomeness": 30, "L33t c0ding skillz": 300, "Baldness level": 0}}
# Create a dictionary for the card
card4 = {"Iron Man": {"Intelligence": 400, "Handsomeness": 40, "L33t c0ding skillz": 400, "Baldness level": 0}}

while True:
  print("Pick your card: 1 - Thanos,  2 - Black Panther,  3 - Thor,  4 - Iron Man")
  print()
  # Create a variable for the card
  card_choice = input("Choose your card > ")
  print()
  # Create a variable for the stat
  stat_choice = input("Choose your stat: 1. Intelligence, 2. Handsomeness, 3. L33t c0ding skillz, 4. Baldness level > ")
  print()
  if card_choice == "1":
    print("You have chosen Thanos")
    print()
    print("Computer has chosen Black Panther")
    print()
    if stat_choice == "1":
      print("Intelligence: Thanos: ", card["Thanos"]["Intelligence"], "Black Panther: ", card2["Black Panther"]["Intelligence"])
      print()
      if card["Thanos"]["Intelligence"] > card2["Black Panther"]["Intelligence"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "2":
      print("Handsomeness: Thanos: ", card["Thanos"]["Handsomeness"], "Black Panther: ", card2["Black Panther"]["Handsomeness"])
      print()
      if card["Thanos"]["Handsomeness"] > card2["Black Panther"]["Handsomeness"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "3":
      print("L33t c0ding skillz: Thanos: ", card["Thanos"]["L33t c0ding skillz"], "Black Panther: ", card2["Black Panther"]["L33t c0ding skillz"])
      print()
      if card["Thanos"]["L33t c0ding skillz"] > card2["Black Panther"]["L33t c0ding skillz"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "4":
      print("Baldness level: Thanos: ", card["Thanos"]["Baldness level"], "Black Panther: ", card2["Black Panther"]["Baldness level"])
      print()
      if card["Thanos"]["Baldness level"] > card2["Black Panther"]["Baldness level"]:
        print("You win!")
      else:
        print("You lose!")

  elif card_choice == "2":
    print("You have chosen Black Panther")
    print()
    print("Computer has chosen Thor")
    print()
    if stat_choice == "1":
      print("Intelligence: Black Panther: ", card2["Black Panther"]["Intelligence"], "Thor: ", card3["Thor"]["Intelligence"])
      print()
      if card2["Black Panther"]["Intelligence"] > card3["Thor"]["Intelligence"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "2":
      print("Handsomeness: Black Panther: ", card2["Black Panther"]["Handsomeness"], "Thor: ", card3["Thor"]["Handsomeness"])
      print()
      if card2["Black Panther"]["Handsomeness"] > card3["Thor"]["Handsomeness"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "3":
      print("L33t c0ding skillz: Black Panther: ", card2["Black Panther"]["L33t c0ding skillz"], "Thor: ", card3["Thor"]["L33t c0ding skillz"])
      print()
      if card2["Black Panther"]["L33t c0ding skillz"] > card3["Thor"]["L33t c0ding skillz"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "4":
      print("Baldness level: Black Panther: ", card2["Black Panther"]["Baldness level"], "Thor: ", card3["Thor"]["Baldness level"])
      print()
      if card2["Black Panther"]["Baldness level"] > card3["Thor"]["Baldness level"]:
        print("You win!")
      else:
        print("You lose!")

  elif card_choice == "3":
    print("You have chosen Thor")
    print()
    print("Computer has chosen Iron Man")
    print()
    if stat_choice == "1":
      print("Intelligence: Thor: ", card3["Thor"]["Intelligence"], "Iron Man: ", card4["Iron Man"]["Intelligence"])
      print()
      if card3["Thor"]["Intelligence"] > card4["Iron Man"]["Intelligence"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "2":
      print("Handsomeness: Thor: ", card3["Thor"]["Handsomeness"], "Iron Man: ", card4["Iron Man"]["Handsomeness"])
      print()
      if card3["Thor"]["Handsomeness"] > card4["Iron Man"]["Handsomeness"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "3":
      print("L33t c0ding skillz: Thor: ", card3["Thor"]["L33t c0ding skillz"], "Iron Man: ", card4["Iron Man"]["L33t c0ding skillz"])
      print()
      if card3["Thor"]["L33t c0ding skillz"] > card4["Iron Man"]["L33t c0ding skillz"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "4":
      print("Baldness level: Thor: ", card3["Thor"]["Baldness level"], "Iron Man: ", card4["Iron Man"]["Baldness level"])
      print()
      if card3["Thor"]["Baldness level"] > card4["Iron Man"]["Baldness level"]:
        print("You win!")
      else:
        print("You lose!")

  else:
    print("You have chosen Iron Man")
    print()
    print("Computer has chosen Thanos")
    print()
    if stat_choice == "1":
      print("Intelligence: Iron Man: ", card4["Iron Man"]["Intelligence"], "Thanos: ", card["Thanos"]["Intelligence"])
      print()
      if card4["Iron Man"]["Intelligence"] > card["Thanos"]["Intelligence"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "2":
      print("Handsomeness: Iron Man: ", card4["Iron Man"]["Handsomeness"], "Thanos: ", card["Thanos"]["Handsomeness"])
      print()
      if card4["Iron Man"]["Handsomeness"] > card["Thanos"]["Handsomeness"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "3":
      print("L33t c0ding skillz: Iron Man: ", card4["Iron Man"]["L33t c0ding skillz"], "Thanos: ", card["Thanos"]["L33t c0ding skillz"])
      print()
      if card4["Iron Man"]["L33t c0ding skillz"] > card["Thanos"]["L33t c0ding skillz"]:
        print("You win!")
      else:
        print("You lose!")

    elif stat_choice == "4":
      print("Baldness level: Iron Man: ", card4["Iron Man"]["Baldness level"], "Thanos: ", card["Thanos"]["Baldness level"])
      print()
      if card4["Iron Man"]["Baldness level"] > card["Thanos"]["Baldness level"]:
        print("You win!")
      else:
        print("You lose!")

  print()
  again = input("Again? y/n > ")
  if again == "y":
    print()
    continue
  else:
    break





