# import colorgram as cg
#
# colors = cg.extract("painting.jpg", 30)
# color_list = []
#
# for i in range(30):
#     rgb = colors[i].rgb
#     red = rgb[0]
#     green = rgb[1]
#     blue = rgb[2]
#     color_list.append((red, green, blue))
#
# print(color_list)
import turtle as t
import random as rand

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154),
              (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8),
              (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216),
              (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

toto = t.Turtle()
toto.speed("fastest")
my_screen = t.Screen()
my_screen.colormode(255)
my_screen.screensize(650, 650)
my_screen.setworldcoordinates(0, 0, 650, 650)
toto.penup()
toto.hideturtle()

for i in range(0, 10):
    toto.setpos(0, 0 + (i*65))
    for _ in range(10):
        toto.dot(20, rand.choice(color_list))
        toto.forward(50)

# my_screen.screensize(100,100)
my_screen.exitonclick()
