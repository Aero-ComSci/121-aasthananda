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
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
sizes = [1/2, 1, 1.5, 1.8, 1.75, 1.99]

#-----initialize turtle-----
spot = trtl.Turtle()
spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
score_writer = trtl.Turtle()
counter =  trtl.Turtle() 
trtl.bgcolor("lavender")


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
    score_writer.write(score,font=font_setup)
    
def change_position():
    new_xpos = rand.randint(-200,200)
    new_ypos= rand.randint(-150,150)
    spot.goto(new_xpos, new_ypos)
    update_score()

def spot_clicked(x,y):
    global timer_up
    spot.penup()
    spot.hideturtle()
    change_position()
    spot.showturtle()
    spot.pendown()
    add_color()
    new_sizes()
    if timer_up == True:
       spot.hideturtle()

def add_color():
   random_color = rand.choice(colors)
   spot.color(random_color)
   spot.stamp()
   spot.color(spot_color)

def new_sizes():
   newsize = rand.choice(sizes)
   spot.shapesize(newsize)

def start_game():
   global timer_up, score, timer
   score = 0
   timer = 30
   timer_up = False
   score_writer.clear()
   score_writer.write(score, font=font_setup)
   countdown()

#-----events----------------
spot.onclick(spot_clicked)
new_sizes()
add_color()
score_writer.penup()
score_writer.goto(-100,100)
counter.penup()
counter.goto(-250, 100)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
start_game()
wn.mainloop()
