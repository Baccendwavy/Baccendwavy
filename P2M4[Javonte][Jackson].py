# [] create The Weather

weather_file = open('mean_temp.txt', 'a+')
weather_file.write("\nRio de Janeiro,Brazil,30.0,18.0")

weather_file.seek(0)
headings = weather_file.readline()
headings = headings.split(',')

city_temp = weather_file.readline()
while city_temp:
    city_temp = city_temp.split(',')
    print(headings[0].capitalize()+ " of " + city_temp[0].title() + " " + headings[2] + " is " + city_temp[2] + " Celsius")
    city_temp = weather_file.readline()

weather_file.close()
# It was okay to submit
