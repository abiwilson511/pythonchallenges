print("hi, please choose one of the characters listed, : daphne, velma, fred, shaggy, scooby doo or scrappy doo")
gender = input("are they male or female?")
if gender == "female":
    colour = input("do they wear the colour purple")
    if colour == "yes":
        print("your character is daphne")
    else:
        print("your character is velma")

if gender == "male":
    human = input("are they human?")
    if human == "yes":
        romint = input("is their romantic interest daphne?")
        if romint == "yes":
            print("your character is fred")
        elif romint == "no":
            print("your character is shaggy")
    elif human == "no":
        oggang = input("are they part of the original gang?")
        if oggang == "yes":
            print("you are thinking of scooby doo")
        else:
            print("you are thinking of scrappy doo")
