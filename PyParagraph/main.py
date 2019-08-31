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

#find letter count per word
total_letters = 0
i = 0
while i < total_word_count:
    letters = len(words[i])
    total_letters = total_letters + letters
    i += 1

letter_count = round(total_letters/total_word_count, 2)

print("Paragraph Analysis")
print("-------------------")
print(f"Approximate word count: {total_word_count}")
print(f"Approximate sentence count: {total_sentence}")
print(f"Average Letter count: {letter_count}")





