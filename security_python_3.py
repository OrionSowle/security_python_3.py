
#def function for logging in
def login_attempts(logins_allowed = 5, login_times = 3):
    print("number of times loged in", login_times)
    login_rate = login_times / logins_allowed
    print("This is a your rate\n", login_rate, "Try to keep in the range of .5 and 1")
login_attempts()

# ip addrs
roles = ["admin", "front desk", "Ceo"]
user_roles = (input("what role do you have\n"))
if user_roles in roles:
    print("welcome")
else:
    print("you dont work here")



#User names
approved_list = ["osowle", "lsowle", "ssowle", "osowle", "bhayes", "chayes", "raireland", "roireland"]
username = input("whats your name\n")

if username in approved_list:
    print("Hello and welcome to the computer\n", username)
else:
    print("you are not welcome here")







