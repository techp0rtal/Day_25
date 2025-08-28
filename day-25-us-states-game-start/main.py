
import turtle

screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image) # we can add our own custom shapes for our turtle
turtle.shape(image) # now we will see the map when we run it




# if we didn't have the csv file, we would need to know the coordinates of each state so we know where to put our text. this is how:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) # this is an event listener which will call the get mouse clicks when we click
# turtle.mainloop() # this will keep our screen open even AFTER we click. better than screen.exitonclick()

answer = screen.textinput(title= "Guess the state", prompt="What's another state's name?") #this method creates a popup box
