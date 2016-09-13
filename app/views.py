from flask import render_template, request
from collections import Counter

from app import app
from app.forms import WordCount

@app.route("/", methods=["GET", "POST"])
def index():
	word_count = WordCount(request.form)

	word_list = []
	phrase_length = 0
	char_length = 0
	max_key = ""

	if request.method == "POST" and word_count.validate():
		word_list = word_count.count.data.split()
		phrase_length = len(word_list)
		char_list = list(word_count.count.data)
		char_split = []
		for char in char_list:
			if char != " ":
				char_split.append(char)
		char_length = len(char_split)

		counter_dict = Counter(word_list)
		
		max_value = max(counter_dict.values())
		#if max_value == counter_dict.values():
		#	max_key = counter_dict.keys()


	return render_template("index.html", word_count=word_count, phrase_length=phrase_length, char_length=char_length)
