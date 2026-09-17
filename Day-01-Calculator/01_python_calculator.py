while True:
     Num1 = int(input("Enter the First Number : "))
     Operation = input("Enter the Mathmetical Operation + , - , / , * , // , % : ")
     Num2 = int(input("Enter the second Number : "))

     if Operation == ("+") :
            print(Num1 + Num2)
     elif Operation == ("-") : 
        print(Num1 - Num2)
     elif Operation == ("/") : 
        print(Num1 / Num2)
     elif Operation == ("*") : 
        print(Num1 * Num2)
     elif Operation == ("//") : 
        print(Num1 // Num2)
     elif Operation == ("%"): 
        print(Num1 % Num2)
     else : 
         print("Invalid Mathematical Operation")

     Choice = input("Do you want to continue (yes/no) :")    
     if Choice == "no":
              break
     else : 
      continue
