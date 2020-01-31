# import webbrowser to allow us to open the browser
import webbrowser

class Movie():
	""" This class helps to store Movie information """
	def __init__ (self, movie_title, movie_storyline, poster_image, trailer_youtube):
		# set instance variables for arguments
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image = poster_image
		self.trailer_youtube = trailer_youtube

		# create a function to open the movie trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)
