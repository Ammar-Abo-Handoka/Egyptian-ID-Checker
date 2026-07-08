print ("Please enter your details to apply for your personal ID card.")
is_egyptian = input ("Are you Egyptian? type (Yes) or (No)\n").lower()
if is_egyptian == "yes" :
    print ("Good, this is a first step,")
    age = int(input ("How old are you?\n"))
    if age > 15:
        birth = input ("Do you have a birth certificate? Type (Yes) or (No)\n").lower()
        if birth == "yes":
            print ("Congratulations! You can apply for a national ID card.")
        elif birth == "no" :
            print ("You need a birth certificate before applying.")
        else :
            print ("Please answer with (Yes) or (NO)")
    elif age == 15:
        print ("This is your first ID card.")
        birth = input ("Do you have a birth certificate? Type (Yes) or (No)\n").lower()
        if birth == "yes":
            print ("Congratulations! You can apply for a national ID card.")
        elif birth == "no" :
            print ("You need a birth certificate before applying.")
        else :
            print ("Please answer with (Yes) or (NO)")
    elif age < 15 :
        print ("Sorry, You must be 15 years. \n You can try again when you are 15.")
    else :
        print ("Please answer with your really age")
elif is_egyptian =="no" :
    print("Sorry, The Egyptian ID is only for Egyptians.")
else :
    print ("Please answer with (Yes) or (No)")