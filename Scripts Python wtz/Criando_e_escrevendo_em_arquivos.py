with open('text.txt','w') as t:
    t.write('aqui esta')

with open('text.txt','r') as t:
    text = t.read()
    print(text)
