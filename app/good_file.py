from collections import Counter


class GoodFile():
	def __init__(self):
		self.word_list = []
		self.char_list = []
		self.phrase_length = 0
		self.char_length = 0
		self.max_key = ""
		self.frequent_letter = ""		

	def number_words(self, word_count):
	#finding number of words
		self.word_list = word_count.count.data.split()
		self.phrase_length = len(self.word_list)

		return self.phrase_length

	def number_char(self, word_count):
	#finding number of characters
		self.char_list = list(word_count.count.data)
		char_split = []
		for char in self.char_list:
			if char != " ":
				char_split.append(char)
		self.char_length = len(char_split)

		return self.char_length

	def common_word(self, word_count):
	#finds most common word		
		counter_dict = Counter(self.word_list)

		max_value = max(counter_dict.values())
		for key, value in counter_dict.items():
			if value == max_value:
				self.max_key = key

		return self.max_key

	def common_char(self, word_count):
	#finds most common character
		letters_dict = Counter(self.char_list)

		max_value = max(letters_dict.values())
		for key, value in letters_dict.items():
			if value == max_value:
				self.frequent_letter = key


		return self.frequent_letter
