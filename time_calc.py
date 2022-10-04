# Functions
def check_user ():
    password = "vostok"

    while True:
        check_password = input("Input the password: ")

        if check_password != password:
            print("Incorrect password! Try again")
        
        if check_password == password:
            break

def display_commands ():
    print("  Following commands are:")
    print("  T - Calculate required time")
    print("  S - Start launching")
    print("  X - Turn off the program")

def calc_time (distance, speed):
    time = distance / speed
    return time

def inputs_for_time_calc ():
    d = float(input("Define distance in km: "))
    s = float(input("Define speed in km/h: "))
    time = calc_time(d, s)

    print(f"Required time is {round(time)} hours.")


# Main program
check_user()

while True:

    display_commands()

    command = input("Input the command: ")

    if command.upper() == "X":
        print("Program is turning off...")
        break

    if command.upper() == "T":
        inputs_for_time_calc()
    
    if command.upper() == "S":
        print("Spacecraft takes off...")
    
    if command.upper() != "X" or command.upper() != "T" or command.upper() != "S":
        print("Type only the valid commands!")