
club_name = "Манчестер Юнайтед"
for char in club_name:
    print(char)
word = "слово"
print(word[::-1])
s1 = "информация"
s2 = "".join(s1[i] for i in range(1, len(s1), 2))
print(s2)
s = "календарь"
t = s[::-1]
print(t)
symbol = "*"
count = 7
print(symbol * count)
word = "Python"
print("++++" + word + "-----")
word = "слово"
print("*" * len(word) + word + "*" * len(word))
word1 = "замена"
word2 = "слово"
print(word1[:len(word2)])
sentence = "Это предложение содержит буквы и."
for char in sentence:
    if char.lower() == 'и':
        print(char)
sentence = "Это предложение с символами"
for i in range(2, len(sentence), 3):
    print(sentence[i])
sentence = "Это предложение с символами"
char1 = 'с'
char2 = 'о'
print([i for i, c in enumerate(sentence) if c == char1 or c == char2])
sentence = "Это длинное предложение"
for i in range(len(sentence)):
    if (i + 1) % 4 < 3:
        print(sentence[i])
sentence = "Это предложение с пробелами"
print(sentence.count(' '))
sentence = "Это предложение с буквой а"
a_count = sentence.lower().count('а')
print(f"{(a_count / len(sentence)) * 100:.2f}%")
text = "+++**+++***"
plus_count = text.count('+')
star_count = text.count('*')
print(f"Количество '+': {plus_count}, Количество '*': {star_count}")
sentence = "Это предложение с гласными"
vowels = "аеёиоуыэюя"
vowel_count = sum(1 for char in sentence.lower() if char in vowels)
print(f"Количество гласных: {vowel_count}")
sentence = "Это предложение содержит четыре слова"
print(len(sentence.split()) > 3)
text = "аааааbbbccccccccc"
found = False
for i in range(len(text) - 4):
    if text[i:i+5] == text[i] * 5:
        found = True
        break
print(found)