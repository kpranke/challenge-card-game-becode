from utils.card import Card
from utils.player import Player, Deck
#from card import Card
#from player import Player, Deck

class Board:
	'''A class to stores a board'''
	def __init__(self, players : list, turn_count : int, active_cards: dict, history_cards : dict):
		self.players = []
		self.turn_count = 0
		self.active_cards = {}
		self.history_cards = {}


	def start_game():
		''' 
		Starts the game, fills a Deck, distributes cards of the Deck to the players.
		'''	
#call distribute
	

