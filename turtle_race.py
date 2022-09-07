# TURTLE RACE 

from turtle import Turtle,Screen
import random
screen=Screen()
names=["toto","tim","shazo","lolo","titu","pitti"]
colours=["purple2","red","blue","yellow","green","orange","red","black","RosyBrown1","turquoise2","violet","seagreen","SlateBlue"]
ypos=[-100,-50,0,50,100,150]
all_turtles=[]
for i in range(6):
    # name=random.choice(names)
    name=Turtle(shape="turtle")
    name.color(colours[i])
    # name.goto(x=-230,y=)
    name.penup()
    name.setposition(x=-175,y=ypos[i])
    all_turtles.append(name)

screen.setup(400,400)

# to create a pop up screen to ask the user to make bet 
# who is going to win?{which colour?}

user_bet=screen.textinput("Make your bet!",prompt="Which colour turtle will win?")
is_race_on=True
while is_race_on:
    
    for i in all_turtles:
        if i.xcor()>180:
            is_race_on=False
            winner=i.pencolor()
            if winner==user_bet:
                print("🎊🎉🎊🎉Yayyyy!!! Your tutle won the race🎊🎉🎊🎉")
            else:
                print("Oops 🥴🥴 !Your turtle has lost the race😟\n")
                print(f"🎊🎉🎊🎉🎊🎉 The winner is the {winner} turtle. 🎊🎉🎊🎉🎊🎉")
        else:  
            rand_dist=random.randint(1,11)
            i.forward(rand_dist)
             
    


screen.exitonclick()

