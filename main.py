import tkinter as tk
import sys

from config import Config
from ship import Ship
from player import Player
from board import Board
from stopwatch import Stopwatch

class Window(tk.Tk):

	def __init__(self, Game):
		self.game = Game
		self.config = Game.config

		super().__init__()
		self.title(self.config.app_title)
		self.geometry(self.config.screen)

		self.create_container()

		self.pages = {}
		self.create_board()


	def create_container(self):
		self.container = tk.Frame(self, bg="white")
		self.container.pack(fill="both", expand=True)

	def create_board(self):
		self.pages["board"] = Board(self.container, self.game)

class Battleship:

	def __init__(self):
		self.config = Config()
		self.ship = Ship(self)
		self.player = Player()
		self.stopwatch = Stopwatch()
		self.window = Window(self)
		

	def check_answer(self):
		ship = self.ship.location
		player = self.player.location
		if ship == player:
			self.stopwatch.stop_stopwatch()
			return True
		return False

	def button_clicked(self, pos_x, pos_y):
		#print(pos_x, pos_y)
		self.player.current_location(pos_x, pos_y)
		win = self.check_answer()
		self.window.pages['board'].change_img_button(pos_x, pos_y, win)
		if win:
			print("You Win!!!")
			#self.window.destroy()
			sys.exit()


	def run(self):
		self.window.mainloop()


if __name__ == '__main__':
	my_battleship = Battleship()
	my_battleship.run()