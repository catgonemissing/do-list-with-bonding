#Task system here...
# task = []
# task_id = 1

# def create_task():
# def read_task():
# def update_task():
# def remove_task():

#Bond system here...
# char = []
# char_id = 1

# def create_char():
# def read_task():
# def update_task():
# def remove_task():

#Main system here...
while True:
    user_input = input("Input what you wanna do here (number only):")

    try:
        choice = int(user_input)
    except (ValueError):
        print("Enter an actual number broski...")

    if choice == 1:
        print("You picked 1")
    elif choice == 2:
        print("You picked 2")
    elif choice == 3:
        print("You picked 3")
    elif choice == 4:
        print("You picked 4")
    elif choice == 5:
        print("You picked 5")
    else:
        print("Enter what's available...")