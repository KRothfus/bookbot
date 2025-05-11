def word_count(str):
		count = 0
		words = str.split()
		for word in words:
			count += 1
		print(f'Found {count} total words')

def character_count(str):
    counts = {}
    str_lower = list(str.lower())
    for char in str_lower:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def report(counts_dict):
    
    def sort_on(dict):
        return dict["num"]
    list = []
    for char in counts_dict:
        if char.isalpha():
            list.append({'char': char, "num": counts_dict[char]})
    list.sort(reverse=True, key=sort_on)
    return list    

    
if __name__ == '__main__':
	# character_count('kellan is great')
    report(character_count('kellan is great'))