from flask import render_template, request

from app import app
from app.forms import WordCount

@app.route("/", methods=["GET", "POST"])
def index():
	word_count = WordCount(request.form)

	#if request.method == "POST" and word_count.validate():
	phrase_length = len( word_count.count.data.split())
	char_list = list(word_count.count.data)
	char_split = []
	for char in char_list:
		if char != " ":
			char_split.append(char)
	char_length = len(char_split)


	return render_template("index.html", word_count=word_count, 
		phrase_length=phrase_length, char_length=char_length)
