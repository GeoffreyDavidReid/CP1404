""" Word Occurrences """

words_str = str(input("Enter string of words: "))
words_list = words_str.split()
words_list_sorted = words_list.sort()

word_count_dict = {}

for word in words_list:
    if word in word_count_dict:
        word_count_dict[word] += 1
    else:
        word_count_dict[word] = 1

print()
print("Text: ", words_str)
for key,val in word_count_dict.items():
    print("{}: {:>5d}".format(key, val))

#def get_max_column_width(column_number, table):
#   max_width = 0
#    for row in table:
#    current_width = len(row[column_number])
#        if current_width > max_width
#           max_width = current_width
#    return max_width + 5