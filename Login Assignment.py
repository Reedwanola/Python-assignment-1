#Create a simple username and password authentication.
# If the username and password specified are correct, then print
# a success message, else print "You're are wrong!" five times.
# Define the correct username and password
correct_username = "Reedwan_ola"
correct_password = "KARATU"
username = input("Enter your username ")
password = input("Enter your password: ")
if username == correct_username and password == correct_password:
    print("Login is Successful")
else:
    for _ in range(5):
        print("You're wrong!")