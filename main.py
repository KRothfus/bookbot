
def main():

	def get_book_text(url):
		with open(url) as f:
			print( f.read())
  
	get_book_text("./frankenstein.txt")
if "__name__" == "__main__":
	main()

