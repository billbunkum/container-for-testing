from flask import render_template, request
from collections import Counter

from app import app
from app.forms import WordCount
from app.good_file import GoodFile

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html")

@app.route("/word-counter", methods=["GET", "POST"])
def word_counter():
	word_count = WordCount(request.form)
	good_stuff = GoodFile()

#'if' protects for shitty empty form
	if request.method == "POST" and word_count.validate():
		phrase_length = good_stuff.number_words(word_count)
		char_length = good_stuff.number_char(word_count)
		max_key = good_stuff.common_word(word_count)
		frequent_letter = good_stuff.common_char(word_count)

	return render_template("word-counter.html", good_stuff=good_stuff, word_count=word_count)

@app.route("/times-table")
def times_table():
	return render_template("times-table.html")