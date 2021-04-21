#buzzfeed based
#the program will compare both your name and your loved person name to the words TRUE and LOVE

your_name = (input("Looks like you fell in love, let me help you.\nWhat's your name? ")).lower()
beloved_name = (input("What's the name of your loved person? ")).lower()
conc_name = your_name + beloved_name

#counting letters

c_true = conc_name.count("t")+conc_name.count("r")+conc_name.count("u")+conc_name.count("e")
c_love = conc_name.count("l")+conc_name.count("o")+conc_name.count("v")+conc_name.count("e")

conc_name = float(str(c_true) + str(c_love))

if  40 <= conc_name <= 50:
    print(f"Don't waste time, schedule the wedding right now! Your love score is {conc_name}%")
elif  conc_name < 10 or conc_name > 90:
    print(f"I'm sorry, you must find another person! Your love score is {conc_name}%")
else:
    print(f"In my calculations... Your love score is {conc_name}%")