word_list = ["Amar", "Anjali", "Diksha", "Drishti", "Kushal"]
longest_latter = 0
longest_word = ""
for word in word_list:
     if len(word) > longest_latter:
         longest_latter = len(word)
         longest_word = word
print(longest_word)
