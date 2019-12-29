# gain email adresses from the text
import re

print("This little program is going to help you with finding email adresses in a solid text.")
pattern=r'[\w\.-]+@[\w\.-]+'
x=input("Insert any amount of text: \n")
match=re.findall(pattern, x)

if len(match)>1:
    print()
    print("Here is what I have found: ")
    print(match)
else:
    print()
    print("There are no email addresses in a provided text.")
    

#gain url from the text    
page =('your text or webpage source')
start_link = page.find('<a href=')+len('<a href=')+1
stop_link = page.find('>', start_link)-1
url=page[start_link:stop_link]
print(url)