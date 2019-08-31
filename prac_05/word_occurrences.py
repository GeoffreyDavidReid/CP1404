""" Word Occurrences """

words_str = str(input("Enter string of words: "))
words_list = words_str.split()

word_count_dict = {}

for word in words_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

print(word_count_dict)
