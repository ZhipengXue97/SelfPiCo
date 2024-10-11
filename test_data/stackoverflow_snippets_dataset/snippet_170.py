# Extracted from https://stackoverflow.com/questions/2709821/what-is-the-purpose-of-the-self-parameter-why-is-it-needed
class foo:
      def __init__(self, num1, num2):
             self.n1 = num1 #now in this it will make the perimeter num1 and num2 access across the whole class
             self.n2 = num2
      def add(self):
             return self.n1 + self.n2 # if we had not written self then if would throw an error that n1 and n2 is not defined and we have to include self in the function's perimeter to access it's variables

