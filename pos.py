# -*- coding: utf-8 -*-

from nltk import pos_tag, word_tokenize
from nltk import WordNetLemmatizer
import csv
import sys
import re

reload(sys)
sys.setdefaultencoding('utf8')

def preprocess(original_str):
	# stemmer
	wnl = WordNetLemmatizer()
	# pos
	original_str = unicode(original_str, errors='ignore')
	print type(original_str)
	article_tok = pos_tag(word_tokenize(original_str))
	print type(article_tok)
	print "token: "
	print article_tok

	# choose Noun
	str_noun = ''
	for word, tag in article_tok:
		if ("NN" in tag) or ("JJ" in tag):
			# print(word,":",tag)
			# print(wnl.lemmatize(word))
			try:
				stemming_word = wnl.lemmatize(word)
				print stemming_word
				if len(word) > 1:
					str_noun = str_noun + stemming_word + " "
			except UnicodeDecodeError as e:
				print "error: " + word
			# end if



	# result
	# final_doc.append(str_noun)
	# print "return_preprocess : " + str_noun

	return str_noun

def dataCleaning(doc_str):
	pat = r"(\w+\.)([a-zA-Z]+\w)"
	temp = re.sub(pat, r"\1 \2", doc_str)
	# print cleanData
	# print temp

	return temp

def inputs_to_str(unicode_or_str):
	if isinstance(unicode_or_str, unicode):
		return_value = unicode_or_str.encode('utf-8')
	else:
		return_value = unicode_or_str
	return return_value

def main():
	a = 0
	# original_doc = []
	final_doc = []
	# read csv file
	with open('test.csv', 'wb') as f:
		reader = csv.reader(open('../datas/medical_research/un_labeled/training_data.csv', 'rb'))
		writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		for row in reader:
			input_row = row[1] + row[2]
			row[2] = ""
			print "input_row:"
			print type(input_row)
			print input_row

			cleanData = dataCleaning(input_row)

			final_doc = preprocess(cleanData.lower())

			print final_doc
			row.append(final_doc)
			# print "result_row: " + row[2]
			writer.writerow(row)

if __name__ == "__main__":
	main()
