#v1.6
#tested, all works
import turtle
turtle.left(90)
print("you control the turtle")
print("type , \"help\" for commands")
play = True

empty = ""
empty2 = ""
empty3 = ""

while play:
    try:
            #is where commands are input
        empty = input("Command: ").lower()
        if empty[-1] == " ":
            empty = empty[0:-1]
        args = empty.split(" ")
        if len(args) == 1:
            command = empty
            empty = ""
        elif len(args) == 2:
            command,empty = empty.split()
        elif len(args) == 3:
            command,empty,empty2 = empty.split()
        elif len(args) == 4:
            command,empty,empty2,empty3 = empty.split()

       
            #sets colour
        if command in("c","colour","color"):
            try:
                turtle.color(empty)
                print("Colour set to", empty)
            except:
                print("unknown colour")
            #sets fillcolour
        elif command in("fillcolour","fillcolor","fcolour","fcolor","fc"):
            try:
                turtle.fillcolor(empty)
                print("fillcolour has been set to",empty)
            except:
                print("Unknown colour")
            #starts the colour fill
        elif command in("sfill","startfill","sf"):
            turtle.begin_fill()
            print("Fill started")
            #ends the colour fill
        elif command in("efill","endfill","ef"):
            turtle.end_fill()
            print("Fill ended")
            #sets the pen to up
        elif command in("pup","penup","pu"):
            turtle.penup()
            print("Pen is up")
            #sets the pen to down
        elif command in("pdown","pendown","pd"):
            turtle.pendown()
            print("Pen is down")
            #shows the turtle
        elif command in("show"):
            turtle.showturtle()
            #hides the turtle
        elif command in("hide"):
            turtle.hideturtle()
            #moves forward
        elif command in("f","forward"):
            turtle.forward(int(empty))
            #turns left
        elif command in("l","left"):
            turtle.left(int(empty))
            #turns right
        elif command in("r","right"):
            turtle.right(int(empty))
            #sets the turtles angle
        elif command in("setang","setangle","sa"):
            turtle.setheading(int(empty)+90)
            print("the turtles heading is",empty)
            #returns the turtles heading
        elif command in("getang","getangle","ga","heading","he"):
            heading = turtle.heading()
            print("The turtles current heading is", heading - 90)

            #moves back
        elif command in("b","back","backwards"):
            turtle.back(int(empty))
            #sets the turtles position
        elif command in("setpos","setposition"):
            print("this will draw a line to that pos if pen is not up, type y to continue, n to exit")
            ans = input().lower()
            if ans in("y","yes","ye"):
                if int(empty) + int(empty2) > 0:
                    x = int(empty)
                    y = int(empty2)
                else:
                    x = int(input("X-coordinate: "))
                    y = int(input("Y-coordinate: "))
                turtle.setpos(x, y)
                print("Turtles position has been set to", x, ",", y)
            else:
                print("command aborted")
            #lists commands
        elif command in("h","help"):
            if empty == "":
                print("""This is just a list of commands, for info on what a command does type help and then the command.
Movement:
    f/forward, b/back, setpos/setposition/sp, p/pos/getpos/gp, h/home
Angle:
    r/right, l/left, setang/setangle/sa, getang/getangle/ga/heading/ha
Pen:
    pup/penup, pdown/pendown, circle/circ/cir, arc/ar/a, polygon/poly
Colour:
    fillcolour/fillcolor/fc, c/colour/color, startfill/sfill/sf,
    endfill/efill/ef
Miscellaneous:
    clear/clearscreen, h/help, quit, hide, show
capitalisation doesnt matter type your commands: *command* *amount*
""")
            elif empty in("c","colour","color"):
                print("""The colour command sets the colour that the turtle draws in
format: colour *colour*""")
            elif empty in("fillcolour","fillcolor","fcolour","fcolor","fc"):
                print("""The fillcolour command sets the colour used when using the startfill and endfill commands
format: fillcolour *colour*""")
            elif empty in("sfill","startfill","sf"):
                print("""The startfill command starts selecting the area where the fillcolour will be placed
format: startfill""")
            elif empty in("efill","endfill","ef"):
                print("""The endfill command ends the selectrin of the area where the fillcolour will be put, this is when you see the result
format: startfill""")
            elif empty in("pup","penup","pu"):
                print("""The penup command lifts the pen from the canvas, the turtle wil not draw when the pen is up
format: penup""")
            elif empty in("pdown","pendown","pd"):
                print("""The pendown command places the pen to the canvas, the turtle will draw when the pen is down, this is the default
format: pendown""")
            elif empty in("f","forward"):
                print("""The forward command moves the turtle in the direction it is facing by the specified amount
format: forward 50""")
            elif empty in("l","left"):
                print("""The left command rotates the turtle left by the spcified number of degrees
format: left 90""")
            elif empty in("r","right"):
                print("""The right command rotates the turtle right by the specified number of degrees
format: right 90""")
            elif empty in("setang","setangle","sa"):
                print("""The setangle command sets the angle the turtle is facing (it starts facing 0 degrees)
format: setang 180""")
            elif empty in("b","back","backwards"):
                print("""The back command moves the turtle backwards by the specified distance
format: back 100""")
            elif empty in("setpos","setposition","sp"):
                print("""The setposition command sets the position ofthe turtle to the specified coordinates
format: setpos 100 100
or
setpos
100
100""")
            elif empty in("h","help"):
                print("""The help command on is own lists all recognised commands for the turtle, when paired with a command it givs details on that command
format: help
or
help *command*""")
            elif empty in("home"):
                print("""The home command sets the turtles position to 0,0
format: home""")
            elif empty in("p","pos","getpos"):
                print("""The getpos command prints the x and y coordinates of the turtle
format: getpos""")
            elif empty in("clear","clearscreen"):
                print("""The clear command clears the screen of all markings
format: clear""")
            elif empty in("quit"):
                print("""The quit command ends the session
format: quit""")
            elif empty in("getang","getangle","ga","heading","ha"):
                print("""The getang command returns the turtles current heading
format: getang""")
            elif empty in("circle","circ","cir"):
                print("""The circle command draws a circle with the radius provided, a negative radius draws the circle clockwise
format: cir *radius*""")
            elif empty in("arc","ar","a"):
                print("""The arc command draws an arc with the specified radius and length in degrees,
a negative number draws the arc anticlockwise
format: arc *radius* *degrees*""")
            elif empty in("polygon","poly","p"):
                print("""The polygon command draws a regular polygon with the radius and num of sides provided
format: poly *radius* *extent(360 degrees if not specified) *num of sides*""")
            elif empty in("hide"):
                print("""The hide command hides the turtle
format: hide""")
            elif command in("show"):
                print("""The show command shows the turtle, this is on by default
format: show""")
            else:
                print("That command is unrecognised, did you misspell it?")
            #sets turtles position to 0,0
        elif command in("home"):
            if turtle.penup():
                turtle.home()
            else:
                turtle.penup()
                turtle.home()
                turtle.pendown()
            turtle.left(90)
            print("Turtle is at 0,0")
            #gives the turtles position
        elif command in("p","pos","getpos","gp"):
            print("Turtles pos is", turtle.pos)
            #draws a circle
        elif command in("circle","circ","cir"):
            radius = int(empty)
            turtle.circle(radius)
            #draws an arc
        elif command in("arc","ar","a"):
            radius = int(empty)
            degrees = int(empty2)
            turtle.circle(radius, degrees)
            #draws a regular polygon
        elif command in("polygon","poly"):
            if empty3 == "":
                radius = int(empty)
                sides = int(empty2)
                turtle.circle(int(empty), steps=int(sides))
            else:
                radius = int(empty)
                degrees = int(empty2)
                sides = int(empty3)
                turtle.circle(int(radius), int(degrees), steps=int(sides))
            #clears the screen
        elif command in("clear","clearscreen"):
            turtle.clearscreen()
            turtle.left(90)
            print("Screen is clear")
            #ends the session
        elif command in("quit"):
            play = False
            print("Bye")
            turtle.bye()
            #prints if command is unrecognised
        else:
            print("Unknown command")
    except:
        print("you messed up somehow, dont use decimals on setpos and type all required arguments")