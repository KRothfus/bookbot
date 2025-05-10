
def main():

	def get_book_text(url):
		with open(url) as f:
			return f.read()
	
	def word_count(str):
		count = 0
		words = str.split()
		for word in words:
			count += 1
		print(count)

		return f'{count} words found in the document'

	word_count(get_book_text("./books/frankenstein.txt"))
main()

