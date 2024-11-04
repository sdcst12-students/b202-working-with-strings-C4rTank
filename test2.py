


sentence = "There is a big ball-oon in the blue sky"

x = 0
sentence = list(sentence)

print(sentence)

count = len(sentence)
print(count)
count = count / 2
print(count)
count = count + 0.5
count = int(count)


sentence.insert(count, "\n")
print(sentence)
sentence = "".join(sentence)


print(sentence)





