# Extracted from https://stackoverflow.com/questions/1436703/what-is-the-difference-between-str-and-repr
class C1:pass

class C2:        
    def __str__(self):
        return str(f"{self.__class__.__name__} class str ")

class C3:        
    def __repr__(self):        
         return str(f"{self.__class__.__name__} class repr")

class C4:        
    def __str__(self):
        return str(f"{self.__class__.__name__} class str ")
    def __repr__(self):        
         return str(f"{self.__class__.__name__} class repr")


ci1 = C1()    
ci2 = C2()  
ci3 = C3()  
ci4 = C4()

print(ci1)       #<__main__.C1 object at 0x0000024C44A80C18>
print(str(ci1))  #<__main__.C1 object at 0x0000024C44A80C18>
print(repr(ci1)) #<__main__.C1 object at 0x0000024C44A80C18>
print(ci2)       #C2 class str
print(str(ci2))  #C2 class str
print(repr(ci2)) #<__main__.C2 object at 0x0000024C44AE12E8>
print(ci3)       #C3 class repr
print(str(ci3))  #C3 class repr
print(repr(ci3)) #C3 class repr
print(ci4)       #C4 class str 
print(str(ci4))  #C4 class str 
print(repr(ci4)) #C4 class repr

