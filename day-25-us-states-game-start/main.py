import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")

image = "blank_states_img.gif"
screen.addshape(image) # we can add our own custom shapes for our turtle
turtle.shape(image) # now we will see the map when we run it
writer = turtle.Turtle()
writer.hideturtle() # don't want to see the turtle when we write to an area
writer.penup() # no lines drawn on our map please


# if we didn't have the csv file, we would need to know the coordinates of each state so we know where to put our text. this is how:
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor) # this is an event listener which will call the get mouse clicks when we click
# turtle.mainloop() # this will keep our screen open even AFTER we click. better than screen.exitonclick()

# but we do have the data from the csv file in x and y columns.
states_data = pandas.read_csv("50_states.csv")
#print(states_data)
states_list = states_data["state"].to_list() # i don't even use this, might delete.
states_list = [state.lower() for state in states_list] # i don't even use this, might delete.
#print(states_list)
score = 0
# I need to keep track of correct answers that have already been submitted (and thus, states that have already been added to the map)
already_mapped_answers = []

while len(already_mapped_answers) < 50:
    answer = screen.textinput(title= f"{score}/50 States Correct", prompt="Guess a state name?") # this method creates a popup box
    answer = answer.lower()
    answer = answer.title() # make sure our answers match the state names perfectly if there are multiple words (i.e. New York)

    if answer in states_data["state"].values and answer not in already_mapped_answers: # we must use .values here because this a Panda Series, not an actual list, therefore we must refer to the value of the index-value pair (similar to a dictionary)
        already_mapped_answers.append(answer) # keep updating the list of already given answers so we don't write the same state twice (or increase the score twice for the same state)
        print(already_mapped_answers)
        row = states_data[states_data["state"] == answer]
        x_coordinate = int(row["x"])
        y_coordinate = int(row["y"])
        writer.goto(x_coordinate, y_coordinate)
        writer.write(answer)
        score += 1

title = f"{score}/50 States Correct"


"""
Logic Summary:

User Input:
1. Compare the input with a bank of names
2. If correct, remove it from the bank of names 

3. Write correct guesses on map
    3.1. Do this by checking if the answer is in the Series (use .values to avoid checking the index). 

4. Use a loop to keep them guessing
    4.1. while the length of the list of already_guessed_answers is < 50, the game continues.
5.
6. Keep track of score. Easy. just add one. or check the length of the list (which is more efficient?)



"""
