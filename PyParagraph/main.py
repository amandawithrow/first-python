#open file with paragraph to read it
gatsby = open("gatsby paragraph.txt", "r")

#read whole text file
whole = gatsby.read()

#close file
gatsby.close()

#find total word count
words = whole.split(" ")
total_word_count = len(words)

#find total sentence count
sentence = whole.split(".")
total_sentence = len(sentence) - 1



print(total_word_count)
print(total_sentence)
print(sentence)




