def takeInput():
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
    operator = input("Enter the operator +,-,*,/: ")

    return (num_1,num_2,operator)


(num_1,num_2,operator)= takeInput()

def displayResult(num_1,num_2,operator):
   if(operator=="+"):
       print(num_1,operator,num_2,"=",num_1+num_2)
   elif(operator=="-"):
          print(num_1,operator,num_2,"=",num_1-num_2)
   elif(operator=="*"):
           print(num_1,operator,num_2,"=",num_1*num_2)
   elif(operator=="/"):
           print(num_1,operator,num_2,"=",num_1/num_2)
   else:
         print("invalid")       
displayResult(num_1,num_2,operator)