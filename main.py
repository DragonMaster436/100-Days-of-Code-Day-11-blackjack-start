import random
from art import logo
from replit import clear


# This function deals a card to the selected hand. 
def deal_card(card_list):
  card = random.choice(cards)
  card_list.append(card)


# This function calls the deal_card function twice to deal the user and computer 2 cards each.
def starting_hand(user_cards, computer_cards):
  for i in range(2):
    deal_card(user_cards)

  for i in range(2):
    deal_card(computer_cards)


# This funtion calculates the score of the selected hand.
def calculate_hand(hand):
  total_hand = sum(hand)
  return total_hand


# This function will change the ace value to 1 if the score is over 21. 
def change_ace(card_list, total_hand):
  for i in range(len(card_list)):
    if card_list[i] == 11 and total_hand > 21:
      card_list[i] = 1

# this function refrshs the screen and prints the logo.
def refresh_screen():
  clear()
  print(logo)

def final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,):
  print(f"\nYour final hand was {user_cards} with a total of {total_user_hand}")
  print(f"The Computer's final hand was {computer_cards} with a total of {total_computer_hand}")



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play_game == 'y':
  refresh_screen()

else:
  exit()

# This is the all the variables outside of the loop..




# This will be whre I need to recall the code to restart the game..

def blackjack_game():
  user_cards = []
  user_wins = False
  computer_cards = []
  computer_wins = False
  its_a_draw = False


  starting_hand(user_cards, computer_cards)



  while not user_wins or not computer_wins or not its_a_draw:
    total_user_hand = calculate_hand(user_cards)
    total_computer_hand = calculate_hand(computer_cards)

    if total_user_hand == 21 and total_computer_hand == 21:
      refresh_screen()
      print("It's a draw!")
      final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
      its_a_draw = True
      break

    elif total_user_hand == 21:
      refresh_screen()
      print("Player Wins! 🥳 You have a Blackjack!")
      final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
      user_wins = True
      break
    elif total_computer_hand == 21:
      refresh_screen()
      print("Computer Wins! 😭 Computer has a Blackjack!")
      final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
      computer_wins = True
      break



    # note to future self, these go after we add a card to a list. or possible putting these functions in a function..?
    change_ace(user_cards, total_user_hand)
    change_ace(computer_cards, total_computer_hand)


    # This bit of code is to check to see if either computer or user went over 21..
    if total_user_hand > 21:
      refresh_screen()
      print("You loose! 😭 You went over 21!")
      final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
      computer_wins = True
      break
    elif total_computer_hand > 21:
      refresh_screen()
      print("You win! 🥳 Computer went over 21!")
      final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
      user_wins = True
      break


    print(f"Your cards are {user_cards} with a current total of: {total_user_hand}.")
    print(f"    The computer's fisrt card is {computer_cards[0]}")

    # This is for the user to decide if they want to hit or stay.
    more_cards = input("would you like to draw another card? 'y' or 'n':  ")
    if more_cards == "y":
      refresh_screen()
      deal_card(user_cards)

    elif more_cards == "n":
      refresh_screen()
      print("Computer's turn")
      if total_computer_hand > total_user_hand:
        refresh_screen()
        print("Computer Wins! 😭 Computer has a higher score than you!")
        final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
        computer_wins = True
        break


      if total_computer_hand < 17:
        deal_card(computer_cards)
        if total_computer_hand > 21:
          refresh_screen()
          print("You win! 🥳 Copmuter went over 21!")
          final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
          user_wins = True
          break

      if total_user_hand > total_computer_hand:
        refresh_screen()
        print("You win! 🥳 You have a higher score than the computer!")
        final_display_of_score(user_cards, total_user_hand, computer_cards, total_computer_hand,)
        user_wins = True
        break


  keep_playing = input("\nWould you like to play again? 'y' or 'n': ")

  if keep_playing == 'y':
    refresh_screen()
    blackjack_game()






blackjack_game()