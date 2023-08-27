Text = input("camelCase: ")
n =len(Text)
i = 0
snake = ""

while i < n :
    char = Text[i]
    if char.isupper():
        snake += '_' + char.lower()
    else:
        snake += char
    i = i +1

print(snake)