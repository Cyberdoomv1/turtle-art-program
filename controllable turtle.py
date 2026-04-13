import turtle
print("you control the turtle")
play = True
while play:
    command = input("Command: ").lower()
    if command == "colour":
        empty = input("What colour? ")
        turtle.color(empty)
        command = input("Command: ").lower()
    elif command == "fillcolor":
        empty = input("What colour? ")
        turtle.fillcolor(empty)
        command = input("Command: ").lower()
    elif command == "forward":
        empty = int(input("How far: "))
        turtle.forward(empty)