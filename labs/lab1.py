

def user_input():
    # Get user input
    user_input = input("Enter a server name: ")
    return user_input

valid_servers = ["nginx", "docker", "apache", "mysql"]

try:
    user_input= user_input()
    if user_input not in valid_servers:
       print("server not recognized.")
    else:
        print("Server name is running.")
except Exception  as err:
    err.add_note = "Invalid input. Please enter a number and letters."
    #print("Invalid input. Please enter a number and letters.")  
    err.ValueError = "Invalid input. Please enter a number and letters."
    raise  