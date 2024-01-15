"""
a fake login that lets you look like you're hacking into some super 
secret mainframe lol (practice with if statements, imports, print statements)
"""

print("Welcome to top secret mainframe , provide your credentials below")
username = input("Username : ")
password = input("Password : ")

if username == 'praveen' and password == 'abcde123':
    print("Sucessfully Logged in")
elif username != 'praveen':
    print("Username incorrect")
elif password != 'abcde123':
    print("Password incorrect")
else :
    print("Please check your credentials and try again !!! , wrong credentials can lead to punitive action")





