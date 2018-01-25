number = int(input("What Hour?"))
am_pm = input("AM or PM?")

def what_time(i,ii):
    if i >= 7 and i <= 9 and ii == "AM":
        print("Breakfast")
    elif (i == 12 or (i >= 1 and i <= 3)) and ii == "PM":
        print("Lunch")
    elif i >= 7 and i <= 1 and ii == "PM":
        print("Dinner")
    elif i >= 10 and i <= 13 and ii == "PM":
        print("Hammertime")
    elif i >= 1 and i <= 4 and ii == "PM":
        print("Hammertime")
what_time(number,am_pm)
