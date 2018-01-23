def fancy_phone():
    phone_number = input("Please enter your phone number")
    print("({}) {} {}".format(phone_number[0:3], phone_number[3:6], phone_number[6:]))
    print("{}-{}-{}".format(phone_number[0:3], phone_number[3:6], phone_number[6:]))

fancy_phone()
