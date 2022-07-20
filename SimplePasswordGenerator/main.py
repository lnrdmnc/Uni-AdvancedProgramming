import random
uppercase_letter="ABCDEFGHILMNOPQRSZUWXYZ"
lowercase_letters="abcdefghilmnopqrstuwxyz" ##uppercase_letter.lower()
numbers="0123456789"
symbols="()!$%&/=?^\\*+#@"

upper,lower,num,sym= True,True,True,True

all=""

if upper:
    all += uppercase_letter
if lower:
    all+= lowercase_letters
if num:
    all+= numbers
if sym:
    all += symbols

lenght=15
amount=1000000
with open("passwordGenerator.txt", "w") as f:
    for x in range(amount):
        password= "".join(random.sample(all,lenght))
        f.write(password)
        f.write("\n")

