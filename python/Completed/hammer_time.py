time = raw_input("What hour is it? (ex. 11AM)")

def what_time(i):
    if i == ('7AM' or '8AM' or "9AM"):
        print("Breakfast")
    elif i == ('12PM' or "1PM" or "2PM"):
        print("Lunch")
    elif i == ("7PM" or "8PM" or "9PM"):
        print("Dinner")
    elif i == ("10PM" or "11PM" or "12PM" or "1AM" or "2AM" or "3AM" or "4AM"):
        print("Hammertime")
    else:
        print("What?")

what_time(time)
