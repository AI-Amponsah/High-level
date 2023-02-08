""""
getters and setters are used to acess and change the values of private attributes
"""
class Square:
    __side = 50
   
    def get_it(self):
        return self.__side
    def set_it(self, value):
        self.__side = value
Square1 = Square()
Square1.set_it(100)
print(Square1.get_it())