import phonenumbers as p #pip install phonenumbers

from phonenumbers import carrier

print("For EX: +917409*****") # Any No !
mno = input("Enter Phone NO:") # Any No !

s_pro = p.parse(mno) #IT will Take Input

p_name = carrier.name_for_number(s_pro,"en")

print(p_name) # Print Carrier No!

