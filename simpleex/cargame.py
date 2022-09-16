instruction = input(">").lower()

start = False
stop = False

instructions = '''        start - to start the car
        stop - to stop the car
        quit - to exit'''

while instruction != "quit":
    if instruction == "help":
        print(instructions)
    elif instruction == "start":
        if start == False:
            print("Car started... Ready to go!")
            start = True
        else:
            print("Car is already started.")
    elif instruction == "stop":
        if stop == False:
            print("Car stopped")
            stop = True
        else:
            print("Car is already stopped.")
    elif instruction == "quit":
        break
    else:
        print("Not a command")
    instruction = input(">").lower()