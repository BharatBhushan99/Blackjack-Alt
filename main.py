import random 

import graphics

from replit import clear



def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0

    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)

    return sum(cards)

def compare(player_score, computer_score):

  if player_score > 21 and computer_score > 21:
      return "You went over. You lose 😤"

  if player_score == computer_score:
    return "Draw 🙃"
  elif calculate_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif player_score == 0:
    return "Win with a Blackjack 😎"
  elif player_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif player_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(graphics.logo)

  is_game_done = False

  player_cards = []

  computer_cards = []

  for _ in range(2):
    player_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_done:
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\tYour cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"\tComputer’s first card: {computer_cards[0]}")


    if player_score == 0 or computer_score == 0 or player_score > 21:
      is_game_done = True
    else:
      hit = input("Type 'y' to get another card, type 'n' to pass: ")

      if hit == 'y':
        player_cards.append(deal_card())
      else:
        is_game_done = True


  while computer_score != 0 and computer_score < 17: 
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"\tYour final hand: {player_cards}, final score: {sum(player_cards)}")
  print(f"\tComputer’s final hand: {computer_cards}, final score: {sum(computer_cards)}")
  print(compare(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
   clear()
   play_game()