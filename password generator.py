import secrets
import string

#here we are using secrets to generate cryptographically strong passwords

#defining letters,digits and special characters

letters=string.ascii_letters
digits=string.digits
special_characters=string.punctuation

alphabets=letters+digits+special_characters  #combining all values


password_length=int(input('enter the length of password:'))   #getting the length of the password from the user

pwd=''

for i in range(password_length):
    pwd += '' + pwd.join(secrets.choice(alphabets))
print(pwd)



