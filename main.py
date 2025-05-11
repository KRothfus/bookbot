from stats import word_count, character_count, report
import sys

  
def main():
	book = sys.argv[1]

	print('============ BOOKBOT ============/n')
	print(f'Analyzing book found at {book}...')
	def get_book_text(url):
		with open(url) as f:
			return f.read()
	print('----------- Word Count ----------')
	word_count(get_book_text(book))
	print('--------- Character Count -------')
	chars = character_count(get_book_text(book))
	word_count_list = report(chars)
	
	for row in word_count_list:
		print(f'{row['char']}: {row['num']}')
	print('============= END ===============')
 
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
 
elif 'books/' not in sys.argv[1] :
	print('Usage: python3 main.py <path_to_book>')
	sys.exit(1)
  
main()
