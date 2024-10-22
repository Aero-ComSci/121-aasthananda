# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spot_color = "pink"
spot_size = 2
spot_shape = "circle"
score = 0
font_setup = ("Arial", 20, "normal")
timer = 30
counter_interval = 1000  
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
counter =  trtl.Turtle() 


#-----game functions--------
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

def update_score():
    global score 
    score += 1
    score_writer.clear()
    score_writer.hideturtle()
    print(score_writer.write(score,font=font_setup))
    
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos= rand.randint(-150,150)
    spot.goto(new_xpos, new_ypos)
    update_score()
def spot_clicked(x,y):
    spot.penup()
    spot.hideturtle()
    change_position()
    spot.showturtle()
    spot.pendown()



#-----events----------------
spot.onclick(spot_clicked)
score_writer.penup()
score_writer.goto(-100,100)
counter.penup()
counter.goto(-250, 100)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
