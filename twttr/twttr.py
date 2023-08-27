Text = input("Input: ")
n =len(Text)
i = 0
output = ""

while i < n :
    char = Text[i]
    if char.upper() in ['A', 'E', 'I', 'O', 'U']:
        output = output
    else:
        output += char
    i = i +1

print(output)