# Extracted from https://stackoverflow.com/questions/423379/using-global-variables-in-a-function
Initialized = 0  #Here This Initialized is global variable  

def Initialize():
     print("Initialized!")
     Initialized = 1  #This is local variable and assigning 1 to local variable
while Initialized == 0:  

     Initialize()

#if we do Initialized=1 then loop will terminate  

else:
    print("Lets do something else now!")

