word = "aaahhhoj"

clean_word = []
for i in range(len(word)):
    if word[i] != word[i-1]:
        clean_word.append(word[i])
        #clean_word += word[i]

print("".join(clean_word))