print("Hi! My job is to delete all of '!@#$%^&*()_-' from your text.")
text=input("Please paste your text in here: \n")
clean=''
punctuations="!@#$%^&*()_-"

for char in text:
    if char not in punctuations:
        clean=clean + char

print()
print(clean)

info=input("Did you enjoy my program? \n")
if info==("yes"or"Yes"):
    print("I am happy to help!")
elif info==("no"or"No"):
    print("I will try to do better!")
else:
    print("Thank you")