import re

#open file with paragraph to read it
doc = open("test.txt", "r")

#read whole text file
paragraph = doc.read()

#close file
doc.close()

#find total word count by splitting at spaces between words
words = paragraph.split(" ")
total_word_count = len(words)

#find total sentence count by splitting at periods
sentence = paragraph.split(".")
total_sentence = len(sentence) - 1

#find letter count per word by iterating through each word in list and counting
total_letters = 0
i = 0
while i < total_word_count:
    letters = len(words[i])
    total_letters = total_letters + letters
    i += 1

letter_count = round(total_letters/total_word_count, 2)

sentence_list = re.split("(?<=[.!?]) +", paragraph)
j=0
sentence_length = 0

while j < total_sentence:
    wordy = re.findall("[a-zA-Z_]+", sentence_list[j])
    sentence_length = sentence_length + len(wordy)
    j+=1

avg_sentence = round((sentence_length/total_sentence), 2)

print("Paragraph Analysis")
print("-------------------")
print(f"Approximate word count: {total_word_count}")
print(f"Approximate sentence count: {total_sentence}")
print(f"Average Letter count: {letter_count}")
print(f"Average Sentence Length: {avg_sentence}")





