#v1.8.5
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
fileexec = False



def colour(empty):
    empty = empty.lower()
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

def fillcolour(empty):
    empty = empty.lower()
    try:
        turtle.fillcolor(empty)
        print("fillcolour has been set to",empty)
    except:
        print("Unknown colour")
        
def startfill():
    turtle.begin_fill()
    print("Fill started")

def endfill():
    turtle.end_fill()
    print("Fill ended")

def backgroundcol(empty):
    empty = empty.lower()
    try:
        turtle.bgcolor(empty)
        print("background colour has been set to", empty)
    except:
        print("unknown colour")

def forward(empty):
    turtle.forward(float(empty))

def left(empty):
    turtle.left(float(empty))
    
def right(empty):
    turtle.right(float(empty))
    
def backwards(empty)
    turtle.back(float(empty))
    
def setang(empty):
    turtle.setheading((int(empty)-90)*-1)
    print("the turtles heading is",empty)

def setpos(empty,empty2):
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

def home():
    if turtle.penup():
        turtle.home()
    else:
        turtle.penup()
        turtle.home()
        turtle.pendown()
    turtle.left(90)
    print("Turtle is at 0,0")

def towards(empty,empty2):
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

def getang():
    heading = turtle.heading()
    print("The turtles current heading is", heading - 90)

def helpp(empty):
    empty = empty.lower()
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
    elif empty in("filecode","fcode","fcd"):
        print("The filecode command executes the code in the specified file, files must be in the same folder as this program")
        print("format: filecode,*filename.txt*")
    elif empty in("filecommand","fcommand","fcmd"):
        print("The filecommand command executes the command in the specified file, files must be in the same folder as this program")
        print("format: filecommand,*filename.txt*")
    else:
        print("That command is unrecognised, did you misspell it?")

def getpos():
    print("Turtles pos is", turtle.pos())

def distance(empty,empty2):
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

def show():
    turtle.showturtle()
    print("Turtle is showing")

def hide():
    turtle.hideturtle()
    print("Turtle is hidden")

def cursor(empty):
    empty = empty.lower()
    try:
        turtle.shape(str(empty))
        print("The cursor has been set to a",empty)
    except:
        print("Unknown shape please retry")

def speed(empty):
    turtle.speed(int(empty))


def penup():
    turtle.penup()
    print("Pen is up")

def pendown():
    turtle.pendown()
    print("Pen is down")


def circle(empty):
    radius = int(empty)
    turtle.circle(radius)


def arc(empty,empty2):
    radius = int(empty)
    degrees = int(empty2)
    turtle.circle(radius, degrees)


def polygon(empty,empty2,empty3):
    if empty3 == "":
        radius = int(empty)
        sides = int(empty2)
        turtle.circle(int(empty), steps=int(sides))
    else:
        radius = int(empty)
        degrees = int(empty2)
        sides = int(empty3)
        turtle.circle(int(radius), int(degrees), steps=int(sides))


def clear():
    turtle.clearscreen()
    turtle.left(90)
    print("Screen is clear")
    
def pensize(empty):
    turtle.pensize(empty)
    print("The pen size has been set to", empty)


def dot(empty,empty2):
    empty2 = empty2.lower()
    turtle.dot(int(empty), str(empty2))
    print("dot drawn with radius", empty, "pixels in colour", empty2)


def undo():
    turtle.undo()
    print("Action undone")


def dimensions():
    print("The dimensions of the screen are", turtle.window_width(), "by", turtle.window_height(), "pixels")


def text(empty,empty2,empty3,empty4,empty5,empty6):
    try:
        if empty2 == "":
            txt = empty
            turtle.write(str(txt), move=False, align='left', font=('Arial', 8, 'normal'))
            print("text has been written")
        elif empty5 == "":
            txt = str(empty)
            empty2 = empty2.lower()
            move = str(empty2)
            if move in("true"):
                move = True
            else:
                move = False
            empty3 = empty3.lower()
            alignment = str(empty3)
            if alignment in("centre","center","cent","c"):
                alignment = "center"
            elif alignment in("left","l"):
                alignment = "left"
            elif alignment in("right","r"):
                alignment = "right"
            empty4 = empty4.lower()
            fontness = str(empty4)
            turtle.write(str(txt), move=move, align=alignment, font=fontness)
            print("text has been written")
        elif empty5 != "":
            txt = str(empty)
            empty2 = empty2.lower()
            move = str(empty2)
            if move in("true"):
                move = True
            else:
                move = False
            empty3 = empty3.lower()
            alignment = str(empty3)
            if alignment in("centre","center","cent","c"):
                alignment = "center"
            elif alignment in("left","l"):
                alignment = "left"
            elif alignment in("right","r"):
                alignment = "right"
            empty4 = empty4.lower()
            fontness = str(empty4)
            try:
                height = int(empty5)
            except:
                height = float(empty5)
            empty6 = empty6.lower()
            special = str(empty6)
            turtle.write(str(txt), move=move, align=alignment, font=(fontness, height, special))
            print("text has been written")
    except Exception as e:
        print("You may have misspelled something or tried an unsupported font/formatting")
        print(e)


def execute(rawinput):
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

def filecode(empty):
    try:
        fileexec = True
        file = open(empty, "r")
        line = file.readline()
        while line:
            exec(line.strip())
            line = file.readline()
        fileexec = False
        file.close()
    except Exception as e:
        print("bad file, may be typo or missing file")
        print(e)
        
def filecommand(empty):
    try:
        file = open(empty,"r")
        for line in file:
            print(line)
            rawinput = line
            do_command()
    except Exception as e:
        print(e)

def quitt():
    play = False
    print("Bye")
    turtle.bye()
    
def do_command():
    try:
        #-------------------------------------------------------------------------#
        #colour stuff
        #-------------------------------------------------------------------------#

            #sets colour
        if command in("c","colour","color","rgb"):
            colour(empty)
            
            #sets fillcolour
        elif command in("fillcolour","fillcolor","fcolour","fcolor","fc"):
            fillcolour(empty)
            
            #starts the colour fill
        elif command in("sfill","startfill","sf"):
            startfill()
            
            #ends the colour fill
        elif command in("efill","endfill","ef"):
            endfill()
            
            #sets the background colour
        elif command in("bcolour","bacgroundcolour","bclr","bc"):
            backgroundcol(empty)




        #-------------------------------------------------------------------------#
        #movement stuff
        #-------------------------------------------------------------------------#



            
            #moves forward
        elif command in("f","forward"):
            forward(empty)
            
            #turns left
        elif command in("l","left"):
            left(empty)
            
            #turns right
        elif command in("r","right"):
            right(empty)
            
            #sets the turtles angle
        elif command in("setang","setangle","sa"):
            setang(empty)
            
            #moves back
        elif command in("b","back","backwards"):
            backwards()
            
            #sets the turtles position
        elif command in("setpos","setposition","sp"):
            setpos(empty,empty2)
            
            #sets turtles position to 0,0
        elif command in("home","home"):
            home()
            
            #points the turtle towards the specified coordinates
        elif command in("towards","twrds","pointto","point","pnt"):
            towards(empty,empty2)
            
            




        #-------------------------------------------------------------------------#
        #information stuff
        #-------------------------------------------------------------------------#



            #returns the turtles heading
        elif command in("getang","getangle","ga","heading","he"):
            getang()

            #lists commands
        elif command in("h","help"):
            helpp(empty)

            #gives the turtles position
        elif command in("p","pos","getpos","gp"):
            getpos()
                    
            #returns the distance to a specified point
        elif command in("distance","dist","dis"):
            distance(empty,empty2)






        #-------------------------------------------------------------------------#
        #turtle stuff
        #-------------------------------------------------------------------------#



            #shows the turtle
        elif command in("show","show"):
            show()
            
            #hides the turtle
        elif command in("hide","hide"):
            hide()

            #sets the shape of the cursor
        elif command in("turtleshape","cursor","setcursor"):
            cursor(empty)
            
            #sets the speed of the turtle
        elif command in("speed","setspeed","ss"):
            speed(empty)




        #-------------------------------------------------------------------------#
        #drawing stuff
        #-------------------------------------------------------------------------#


            #sets the pen to up
        elif command in("pup","penup","pu"):
            penup()
            
            #sets the pen to down
        elif command in("pdown","pendown","pd"):
            pendown()

            #draws a circle
        elif command in("circle","circ","cir"):
            circle(empty)
            
            #draws an arc
        elif command in("arc","ar","a"):
            arc(empty,empty2)
            
            #draws a regular polygon
        elif command in("polygon","poly"):
            polygon(empty,empty2,empty3)

            #clears the screen
        elif command in("clear","clearscreen"):
            clear()


            #changes pen size
        elif command in("psize","pensize","ps"):
            pensize(empty)
            
            #draws a dot
        elif command in("dot","dot"):
            dot(empty,empty2)

            #undoes previous actions
        elif command in("undo","un","und"):
            undo()


        #-------------------------------------------------------------------------#
        #miscallaneous
        #-------------------------------------------------------------------------#



            #returns the dimentions of the screen
        elif command in("dimension","dimensions","dim"):
            dimensions()

            #writes text
        elif command in("write","text","txt"):
            write(empty,empty2,empty3,empty4,empty5,empty6)

            #executes entered code
        elif command in("execute","exec","exe"):
            execute(empty)
                
            #executes code in the specified file
        elif command in("filecode","fcode","fcd"):
            filecode(empty)
            
            #executes commands in the specified file
        elif command in("filecommand","fcommand","fcmd"):
            filecommand(empty)
                
            #ends the session
        elif command in("quit","quit"):
            quitt()
            
            #prints if command is unrecognised
        else:
            print("Unknown command")

    except Exception as e:
        print(e)
        print("you messed up somehow, type all required arguments")

while play:
    try:
            #is where commands are input
        if fileexec == False:
            rawinput = input("Command: ")
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
        
        command = command.lower()
        do_command()
        
    except Exception as e:
        print(e)
        print("you messed up somehow, type all required arguments")
            #returns the distance to a specified point
        elif command in("distance","dist","dis"):
            distance()






        #-------------------------------------------------------------------------#
        #turtle stuff
        #-------------------------------------------------------------------------#



            #shows the turtle
        elif command in("show"):
            show()
            
            #hides the turtle
        elif command in("hide"):
            hide()

            #sets the shape of the cursor
        elif command in("turtleshape","cursor","setcursor"):
            cursor()
            
            #sets the speed of the turtle
        elif command in("speed","setspeed","ss"):
            speed()




        #-------------------------------------------------------------------------#
        #drawing stuff
        #-------------------------------------------------------------------------#


            #sets the pen to up
        elif command in("pup","penup","pu"):
            penup()
            
            #sets the pen to down
        elif command in("pdown","pendown","pd"):
            pendown()

            #draws a circle
        elif command in("circle","circ","cir"):
            circle()
            
            #draws an arc
        elif command in("arc","ar","a"):
            arc()
            
            #draws a regular polygon
        elif command in("polygon","poly"):
            polygon()

            #clears the screen
        elif command in("clear","clearscreen"):
            clear()


            #changes pen size
        elif command in("psize","pensize","ps"):
            pensize()
            
            #draws a dot
        elif command in("dot"):
            dot()

            #undoes previous actions
        elif command in("undo","un","und"):
            undo()


        #-------------------------------------------------------------------------#
        #miscallaneous
        #-------------------------------------------------------------------------#



            #returns the dimentions of the screen
        elif command in("dimension","dimensions","dim"):
            dimensions()

            #writes text
        elif command in("write","text","txt"):
            write()

            #executes entered code
        elif command in("execute","exec","exe"):
            execute()
                
            #executes code in the specified file
        elif command in("filecode","fcode","fcd"):
            empty = empty.lower()
            filecode()
            
            #executes commands in the specified file
        elif command in("filecommand","fcommand","fcmd"):
            empty = empty.lower()
            filecommand()
                
            #ends the session
        elif command in("quit"):
            quitt()
            
            #prints if command is unrecognised
        else:
            print("Unknown command")

    except Exception as e:
        print(e)
        print("you messed up somehow, type all required arguments")

while play:
    try:
            #is where commands are input
        if fileexec == False:
            rawinput = input("Command: ")
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

        do_command()
        
    except Exception as e:
        print(e)
        print("you messed up somehow, type all required arguments")
