#v1.8.4
#tested 
import turtle
turtle.left(90)
print("you control the turtle")
print("the dimensions of the box are", turtle.window_width(), "pixels by", turtle.window_height(), "pixels")
print("COMMAND FORMAT: *comand*,*value*")
print("type \"help\" for commands")
play = True

empty = ""
empty2 = ""
empty3 = ""
empty4 = ""
empty5 = ""
empty6 = ""
excecuting = bool

#file = open("turtle commands file.txt","r")
#for line in file:
    #print(line)
    #split_instruction = line.split(",")
    #command = split_instruction[0]
    #print(command)
    


while play:
        try:
            if excecuting == True:
                for line in file:
                    if line == "end":
                        excecuting = False
                        file.close()
                    else:
                        line = file.readline()
                        rawinput = line.strip().lower()
            
            
            
                #is where commands are input
            if excecuting == False:
                rawinput = input("Command: ").lower()
            empty = rawinput
            if empty[-1] == " ":
                empty = empty[0:-1]
            if empty[0] == " ":
                empty = empty[1:]

            args = empty.split(",")
            if len(args) == 1:
                command = empty
                empty = ""
            elif len(args) == 2:
                command,empty = empty.split(",")
            elif len(args) == 3:
                command,empty,empty2 = empty.split(",")
            elif len(args) == 4:
                command,empty,empty2,empty3 = empty.split(",")
            elif len(args) == 5:
                command,empty,empty2,empty3,empty4 = empty.split(",")
            elif len(args) == 6:
                command,empty,empty2,empty3,empty4,empty5 = empty.split(",")
            elif len(args) == 7:
                command,empty,empty2,empty3,empty4,empty5,empty6 = empty.split(",")
            else:
                print("Too many inputs")

    #-------------------------------------------------------------------------#
    #colour stuff
    #-------------------------------------------------------------------------#

                #sets colour
            if command in("c","colour","color","rgb"):
                try:
                    int(empty)
                except:
                    empty = empty
                if empty == str:
                    try:
                        turtle.color(empty)
                        print("Colour set to", empty)
                    except:
                        print("unknown colour")
                #else:
                #    try:
                #        turtle.colormode(255)
                #        turtle.color(int(empty),int(empty2),int(empty3))
                #        print("colour has been set to RGB:",empty,empty2,empty3)
                #        
                #    except Exception as e:
                #        print("something went wrong")
                #        print(e)
                
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
                
                #sets the background colour
            elif command in("bcolour","bacgroundcolour","bclr","bc"):
                try:
                    turtle.bgcolor(empty)
                    print("background colour has been set to", empty)
                except:
                    print("unknown colour")




    #-------------------------------------------------------------------------#
    #movement stuff
    #-------------------------------------------------------------------------#



                
                #moves forward
            elif command in("f","forward"):
                turtle.forward(float(empty))
                
                #turns left
            elif command in("l","left"):
                turtle.left(float(empty))
                
                #turns right
            elif command in("r","right"):
                turtle.right(float(empty))
                
                #sets the turtles angle
            elif command in("setang","setangle","sa"):
                turtle.setheading((int(empty)-90)*-1)
                print("the turtles heading is",empty)
                
                #moves back
            elif command in("b","back","backwards"):
                turtle.back(float(empty))
                
                #sets the turtles position
            elif command in("setpos","setposition","sp"):
                print("this will draw a line to that pos if pen is not up, type y to continue, n to exit")
                ans = input().lower()
                if ans in("y","yes","ye"):
                    if int(empty) + int(empty2) != 0:
                        x = float(empty)
                        y = float(empty2)
                    else:
                        x = float(input("X-coordinate: "))
                        y = float(input("Y-coordinate: "))
                    turtle.setpos(x, y)
                    print("Turtles position has been set to", x, ",", y)
                else:
                    print("command aborted")
                
                #sets turtles position to 0,0
            elif command in("home","home"):
                if turtle.penup():
                    turtle.home()
                else:
                    turtle.penup()
                    turtle.home()
                    turtle.pendown()
                turtle.left(90)
                print("Turtle is at 0,0")
                
                #points the turtle towards the specified coordinates
            elif command in("towards","twrds","pointto","point","pnt"):
                if empty2 == "":
                    x = input("X-coordinate: ")
                    y = input("Y-coordinate: ")
                    try:
                        turtle.setheading(turtle.towards(int(x),int(y)))
                        print("Turtle is pointing towards",x,",",y)
                    except Exception as e:
                        print(e)
                else:
                    try:
                        x = empty
                        y = empty2
                        turtle.setheading(turtle.towards(int(x),int(y)))
                        print("Turtle is pointing towards",x,",",y)
                    except Exception as e:
                        print(e)
                
                




    #-------------------------------------------------------------------------#
    #information stuff
    #-------------------------------------------------------------------------#



                #returns the turtles heading
            elif command in("getang","getangle","ga","heading","he"):
                heading = turtle.heading()
                print("The turtles current heading is", heading - 90)

                #lists commands
            elif command in("h","help"):
                if empty == "":
                    print("""This is just a list of commands, for info on what a command does type help and then the command.

    COMMAND FORMAT: *command* *value* OR *comand*,*value*

    Movement:
        f/forward, b/back, setpos/setposition/sp, p/pos/getpos/gp, h/home, speed/setspeed/ss, distance/dist/dis
        
    Angle:
        r/right, l/left, setang/setangle/sa, getang/getangle/ga/heading/ha, towards/twrds/pointto/point/pnt
        
    Turtle:
        pup/penup, pdown/pendown, pensize/psize/ps, hide, show, turtleshape/cursor/setcursor
        
    Drawing:
        dot, circle/circ/cir, arc/ar/a, polygon/poly, clear/clearscreen, undo/und/un
        
    Colour:
        fillcolour/fillcolor/fc, c/colour/color, startfill/sfill/sf,
        endfill/efill/ef, backgroundcolour/bcolour/bclr/bc
        
    Miscellaneous:
        h/help, quit, dimensions/dimension/dim, execute/exec/exe, file
        
    capitalisation doesnt matter type your commands: *command* *amount*""")
                elif empty in("c","colour","color"):
                    print("The colour command sets the colour that the turtle draws in")
                    print("format: colour,*colour*")
                elif empty in("fillcolour","fillcolor","fcolour","fcolor","fc"):
                    print("The fillcolour command sets the colour used when using the startfill and endfill commands")
                    print("format: fillcolour,*colour*")
                elif empty in("sfill","startfill","sf"):
                    print("The startfill command starts selecting the area where the fillcolour will be placed")
                    print("format: startfill")
                elif empty in("efill","endfill","ef"):
                    print("The endfill command ends the selectrin of the area where the fillcolour will be put, this is when you see the result")
                    print("format: startfill")
                elif empty in("pup","penup","pu"):
                    print("The penup command lifts the pen from the canvas, the turtle wil not draw when the pen is up")
                    print("format: penup")
                elif empty in("pdown","pendown","pd"):
                    print("The pendown command places the pen to the canvas, the turtle will draw when the pen is down, this is the default")
                    print("format: pendown")
                elif empty in("f","forward"):
                    print("The forward command moves the turtle in the direction it is facing by the specified amount")
                    print("format: forward,*distance*")
                elif empty in("l","left"):
                    print("The left command rotates the turtle left by the spcified number of degrees")
                    print("format: left,*degrees*")
                elif empty in("r","right"):
                    print("The right command rotates the turtle right by the specified number of degrees")
                    print("format: right,*degrees*")
                elif empty in("setang","setangle","sa"):
                    print("The setangle command sets the angle the turtle is facing (it starts facing 0 degrees)")
                    print("format: setang,*degrees*")
                elif empty in("b","back","backwards"):
                    print("The back command moves the turtle backwards by the specified distance")
                    print("format: back,*distance*")
                elif empty in("setpos","setposition","sp"):
                    print("The setposition command sets the position ofthe turtle to the specified coordinates")
                    print("format: setpos,*x-coord*,*y-coord*")
                    print("or")
                    print("setpos")
                    print("*x-coord*")
                    print("*y-coord*")
                elif empty in("h","help"):
                    print("The help command on is own lists all recognised commands for the turtle, when paired with a command it givs details on that command")
                    print("format: help")
                    print("or")
                    print("help,*command*")
                elif empty in("home"):
                    print("The home command sets the turtles position to 0,0")
                    print("format: home")
                elif empty in("p","pos","getpos"):
                    print("The getpos command prints the x and y coordinates of the turtle")
                    print("format: getpos")
                elif empty in("clear","clearscreen"):
                    print("The clear command clears the screen of all markings")
                    print("format: clear")
                elif empty in("quit"):
                    print("The quit command ends the session")
                    print("format: quit")
                elif empty in("getang","getangle","ga","heading","ha"):
                    print("The getang command returns the turtles current heading")
                    print("format: getang")
                elif empty in("circle","circ","cir"):
                    print("The circle command draws a circle with the radius provided, a negative radius draws the circle clockwise")
                    print("format: cir,*radius*")
                elif empty in("arc","ar","a"):
                    print("The arc command draws an arc with the specified radius and length in degrees,")
                    print("a negative number draws the arc anticlockwise")
                    print("format: arc,*radius*,*degrees*")
                elif empty in("polygon","poly","p"):
                    print("The polygon command draws a regular polygon with the radius and num of sides provided")
                    print("WARNING THE POLY COMMAND DRAWS THE SHAPE RORATED 45 DEGREES TO THE LEFT OF THE TURTLE")
                    print("format: poly,*radius*,*extent(360 degrees if not specified),*num of sides*")
                elif empty in("hide"):
                    print("The hide command hides the turtle")
                    print("format: hide")
                elif empty in("show"):
                    print("The show command shows the turtle, this is on by default")
                    print("format: show")
                elif empty in("turtleshape","cursor","setcursor"):
                    print("The cursor command changes the shape if the pointer, by default a turtle from a list of recognised shapes")
                    print("format: cursor,*shape*")
                elif empty in("speed","setspeed","ss"):
                    print("the speed command sets the speed of the turtle, thid only affects how fast it does commands")
                    print("format: speed,*speed*")
                elif empty in("pensize","psize","ps"):
                    print("The pensize command sets the width of the line drawn to the specified value in pixels")
                    print("format: psize,*width*")
                elif empty in("dimensions","dimension","dim"):
                    print("The dimension command returns the width and height of the screen in pixels")
                    print("format: dim")
                elif empty in("undo","und","un"):
                    print("The undo command undoes the most reecent action")
                    print("format: undo")
                elif empty in("dot"):
                    print("The dot command draws a dot around the cursor with the specified radius and color")
                    print("format: dot,*radius*,*colour*")
                elif empty in("backgroundcolour","bcolour","bclr","bc"):
                    print("The backgroundcolour command sets the colour of the background")
                    print("format: bcolour,*colour*")
                elif empty in("towards","twrds","pointto","point","pnt"):
                    print("The point command points the turtle towards the specified coordinates")
                    print("format: point,*x-coordinate*,*y-coordinate*")
                    print("or")
                    print("point")
                    print("x-coordinate")
                    print("y-coordinate")
                elif empty in("distance","dist","dis"):
                    print("The distance command returns the distance towards the specified coordinates")
                    print("format: dist,*x-coordinate*,*y-coordinate*")
                    print("or")
                    print("dist")
                    print("x-coordinate")
                    print("y-coordinate")
                elif empty in("write","text","txt"):
                    print("The text command writes the given text on the screen with the given perameters")
                    print("format: write,*text*")
                    print("or")
                    print("write,*text*,*move with text (true/false)*,*alignment (left,centre,right)*,*font*")
                    print("or")
                    print("write,*text*,*move with text (true/false)*,*alignment (left,centre,right)*,*font*,*height*,*extra (bold, italics ect)*")
                elif empty in("execute","exec","exe"):
                    print("The exe command executes the entered python code (only works with a single line")
                    print("format: exec,*code*")
                    print("example: exec,turtle.left(90)")
                elif empty in("file"):
                    print("The file command executes the specified file, files must be in the same folder as this program")
                    print("format: file,*filename.txt*")
                else:
                    print("That command is unrecognised, did you misspell it?")

                #gives the turtles position
            elif command in("p","pos","getpos","gp"):
                print("Turtles pos is", turtle.pos())
                        
                #returns the distance to a specified point
            elif command in("distance","dist","dis"):
                if empty2 == "":
                    x = input("X-coordinate: ")
                    y = input("Y-coordinate: ")
                    try:
                        print("The distance towards",x,",",y)
                        print("is", turtle.distance(int(x),int(y)))
                    except Exception as e:
                        print(e)
                else:
                    try:
                        x = empty
                        y = empty2
                        print("The distance towards",x,",",y)
                        print("is", turtle.distance(int(x),int(y)))
                    except Exception as e:
                        print(e)






    #-------------------------------------------------------------------------#
    #turtle stuff
    #-------------------------------------------------------------------------#



                #shows the turtle
            elif command in("show","show"):
                turtle.showturtle()
                print("Turtle is showing")
                
                #hides the turtle
            elif command in("hide","hide"):
                turtle.hideturtle()
                print("Turtle is hidden")

                #sets the shape of the cursor
            elif command in("turtleshape","cursor","setcursor"):
                try:
                    turtle.shape(str(empty))
                    print("The cursor has been set to a",empty)
                except:
                    print("Unknown shape please retry")
                
                #sets the speed of the turtle
            elif command in("speed","setspeed","ss"):
                turtle.speed(int(empty))




    #-------------------------------------------------------------------------#
    #drawing stuff
    #-------------------------------------------------------------------------#


                #sets the pen to up
            elif command in("pup","penup","pu"):
                turtle.penup()
                print("Pen is up")
                
                #sets the pen to down
            elif command in("pdown","pendown","pd"):
                turtle.pendown()
                print("Pen is down")

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


                #changes pen size
            elif command in("psize","pensize","ps"):
                turtle.pensize(empty)
                print("The pen size has been set to", empty)
                
                #draws a dot
            elif command in("dot","d"):
                turtle.dot(int(empty), str(empty2))
                print("dot drawn with radius", empty, "pixels in colour", empty2)

                #undoes previous actions
            elif command in("undo","un","und"):
                turtle.undo()
                print("Action undone")


    #-------------------------------------------------------------------------#
    #miscallaneous
    #-------------------------------------------------------------------------#



                #returns the dimentions of the screen
            elif command in("dimension","dimensions","dim"):
                print("The dimensions of the screen are", turtle.window_width(), "by", turtle.window_height(), "pixels")

                #writes text
            elif command in("write","text","txt"):
                try:
                    if empty2 == "":
                        txt = empty
                        turtle.write(str(txt), move=False, align='left', font=('Arial', 8, 'normal'))
                        print("text has been written")
                    elif empty5 == "":
                        txt = str(empty)
                        move = str(empty2)
                        if move in("true"):
                            move = True
                        else:
                            move = False
                        alignment = str(empty3)
                        if alignment in("centre","center","cent","c"):
                            alignment = "center"
                        elif alignment in("left","l"):
                            alignment = "left"
                        elif alignment in("right","r"):
                            alignment = "right"
                        fontness = str(empty4)
                        turtle.write(str(txt), move=move, align=alignment, font=fontness)
                        print("text has been written")
                    elif empty5 != "":
                        txt = str(empty)
                        move = str(empty2)
                        if move in("true"):
                            move = True
                        else:
                            move = False
                        alignment = str(empty3)
                        if alignment in("centre","center","cent","c"):
                            alignment = "center"
                        elif alignment in("left","l"):
                            alignment = "left"
                        elif alignment in("right","r"):
                            alignment = "right"
                        fontness = str(empty4)
                        try:
                            height = int(empty5)
                        except:
                            height = float(empty5)
                        special = str(empty6)
                        turtle.write(str(txt), move=move, align=alignment, font=(fontness, height, special))
                        print("text has been written")
                except Exception as e:
                    print("You may have misspelled something or tried an unsupported font or formatting")
                    print(e)

                #executes entered code
            elif command in("execute","exec","exe"):
                if command == "execute":
                    try:
                        exec(rawinput[8:])
                    except Exception as e:
                        print("invalid code")
                        print(e)
                elif command == "exec":
                    try:
                        exec(rawinput[5:])
                    except Exception as e:
                        print("invalid code")
                        print(e)
                elif command == "exe":
                    try:
                        exec(rawinput[4:])
                    except Exception as e:
                        print("invalid code")
                        print(e)
                else:
                    print("Unknown command")
                    
                #executes code in the specified file
            elif command in("filecode","filecd","fcd"):
                try:
                    file = open(empty, "r")
                    line = file.readline()
                    while line:
                        exec(line.strip())
                        line = file.readline()
                    file.close()
                except Exception as e:
                    print("bad file, may be typo or missing file")
                    print(e)
                    
            elif command in("filecommand","filecmd","fcmd"):
                excecuting = True
                filename = empty
                file = open(filename, "r")

                #ends the session
            elif command in("quit","q"):
                play = False
                print("Bye")
                turtle.bye()
                #prints if command is unrecognised
            else:
                print("Unknown command")
        except Exception as e:
            print(e)
            print("you messed up somehow, type all required arguments")
