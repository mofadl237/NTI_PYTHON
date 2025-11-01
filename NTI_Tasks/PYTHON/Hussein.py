count = 0;
userPassword= input("Enter Password => ")
correctPassword= "123123"
correct = True ;
while correct and count <2 :
    if userPassword == correctPassword:
        print("correct");
        correct = False ;
    else
        count +=1;
        userPassword= input(f"incorrect password count available {3 - count} : ");
