is_egyptian = input ("Are you Egyptian? type (Yes) or (No)\n").lower()
if is_egyptian == "yes" :
    print ("Good, this is a first step,")
    is_15 =input ("Are you above 15? Type (Yes) or (No)\n").lower()
    if is_15 == "yes":
        birth = input ("Do you have a birth certificate? Type (Yes) or (No)\n").lower()
        if birth == "yes":
            print ("Congratulations! You can apply for a national ID card.")
        elif birth == "no" :
            print ("You need a birth certificate before applying.")
        else :
            print ("Please answer with (Yes) or (NO)")
    elif is_15 == "no" :
        print ("Sorry, You must be 15 years. \n You can try again when you are 15.")
    else :
        print ("Please answer with (Yes) or (NO).")
elif is_egyptian =="no" :
    print("Sorry, The Egyptian ID is only for Egyptians.")
else :
    print ("Please answer with (Yes) or (No)")