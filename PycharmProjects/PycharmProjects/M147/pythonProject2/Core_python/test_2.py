#10. Write a python program to get the below outputs
sentence="Hi How are you"
#o/p should be "ouy era woH iH"
i=0
while i<len(sentence):
    rev_sen=sentence[::-1]
    i+=1
print(rev_sen,end='')

print(tuple(range(0,11)))


s = "This is a Programming language and Programming is fun"
words = s.split()
longest_word = ""
max_length = 0
for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

# Output the longest word and its length
print("Longest word:", longest_word)
print("Length of the longest word:", max_length)

#Longest word: Programming
#Length of the longest word: 11


ords = ['Look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not',
 'around', 'the', 'eyes', "don't", 'look', 'around', "the", 'eyes', 'Look', 'into', 'my', 'eyes', "you're", "under"]

word_count = {}

for word in ords:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for word, count in word_count.items():
    print(f"'{word}': {count}")

a = 10
b = 20

for _ in range(1):
    a = a + b
    b = a - b
    a = a - b

print("Swapped values: a =", a, "b =", b)


# Input numbers
a = 10
b = 20
count = 1
while count == 1:
    a = a + b
    b = a - b
    a = a - b
    count -= 1
print("Swapped values: a =", a, "b =", b)

