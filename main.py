# Import everything you need to start the game!
# Start the game. You should only run this file to have the game running.

from utils.player import *
from utils.game import Board


#if __name__ == '__main__':
#	main()

deck = Deck()
deck = Deck.shuffle()
print(deck)

players = []
number_players = int(input('How many players?'))

for element in number_players:
	draw