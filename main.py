

# we can use open() to access the data from a csv
# with open("./weather_data.csv", "r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# BUT we still have commas in our dang list though so we ned the csv library

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file) # this creates a csv reader object. this object can be looped through
#     temperatures = []
#     print(data)
#     for row in data:
#         temp = row[1]
#         if temp != "temp":
#             temp = int(temp)
#             temperatures.append(temp)
#         #print(row)
#     print(temperatures)

# ^^^ this method works, but is a lot of work to get just 1 column. what if we were using more complex data? let's use pandas
# 3 lines of code vs 8 lines of code
import pandas
# 1. Create a pandas dataframe object (basically an Excel sheet in Python)
data = pandas.read_csv("weather_data.csv")
#print(data)
# if we want to print a specific column, just use the [] and specify the name of the column you want printed
#print(data["temp"])
# series methods can be found here https://pandas.pydata.org/docs/reference/api/pandas.Series.html

data_dict = data.to_dict() # this converts it into a dictionary
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average = sum(temp_list)/len(temp_list)
# print(average)
#
# # Can also just use the .mean() function in pandas
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data from columns
# print(data["condition"])
# print(data.condition)

#Get data from row (harder)
# print(data[data.day == "Monday"]) # inside the Monday column I want to check for the row where the value is equal to Monday
# # data[data["day"]] # could also format it like this, same thing
#
# # Now let's figure out how to pull the row of data where the temp was at the maximum
# print(data[data.temp == data.temp.max()])
#
# # What if we want a particular row's condition or temperature?
# monday = data[data.day == "Monday"]
# # now witht his row we can tap into the values under the different columns in the same way we got data from the entire column previously
# print(monday.condition)
#
# # Now let's get monday's temperature and convert it to Fahrenheit
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# How to create a dataframe from scratch (instead of reading from a csv file like we did previously).
#Let's say we wanted to create a data frame just from some data you're generating in python
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
my_dataframe = pandas.DataFrame(data_dict)
print(my_dataframe)

# Now we can go even further than this. Let's convert to a csv file
my_dataframe.to_csv("my_data.csv") # we'll name it my_data.csv
