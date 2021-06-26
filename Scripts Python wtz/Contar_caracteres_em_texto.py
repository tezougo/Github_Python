from collections import Counter

with open('text.txt','w') as t:
    t.write('escrevi o texto')

with open('text.txt','r') as t:
    text = t.read()
    print(text)
#for c in text:
#    quantidade = [text.count(c) for c in text]

##  ou

print(Counter(text))
print(Counter(text).most_common(1))