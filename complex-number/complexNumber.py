# April 17, 2020

# Priyanshul Govil
# 19070124053
# IT - 3

# PPSL Assignment -
# Write a python program to represent complex numbers using class.

class ComplexNumber:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag

    def __checkSign(self) -> str:
        if self.imag >= 0:
            return '+'
        else:
            return '-'

    def returnComplex(self):
        if(self.__checkSign() == '+'):
            return("{} + {}i".format(self.real, self.imag))
        else:
            return("{} - {}i".format(self.real, -self.imag))

    def conjugate(self):
        self.imag = -self.imag

    def addComplex(self, complex_num):
        self.real += complex_num.real
        self.imag += complex_num.imag

    def subComplex(self, complex_num):
        self.real -= complex_num.real
        self.imag -= complex_num.imag

    def mulComplex(self, complex_num):
        real = (self.real * complex_num.real) - (self.imag * complex_num.imag)
        imag = (self.real * complex_num.imag) + (complex_num.real * self.imag)

        self.real = real
        self.imag = imag

    def divComplex(self, complex_num):
        real = ( (self.real * complex_num.real) + (self.imag * complex_num.imag) ) /\
                (complex_num.real * complex_num.real + complex_num.imag * complex_num.imag)
        
        imag = ( (self.imag * complex_num.real) - (self.real * complex_num.imag) ) /\
                (complex_num.real * complex_num.real + complex_num.imag * complex_num.imag)

        self.real = round(real, 2)
        self.imag = round(imag, 2)
    

# driver to test above class
print("Complex numbers are in the form of x + yi")

_inpString = input("Enter x and y for 1st complex number (separated by space) : ")
x1, y1 = (float(x) for x in _inpString.split())

_inpString = input("Enter x and y for 2nd complex number (separated by space) : ")
x2, y2 = (float(x) for x in _inpString.split())

del _inpString

complexNumber1 = ComplexNumber(x1, y1)
complexNumber2 = ComplexNumber(x2, y2)

# testing conjugate
print("Conjugate of ({}) is".format(complexNumber2.returnComplex()), end = " ")
complexNumber2.conjugate()
print("({})".format(complexNumber2.returnComplex()))

# testing addition
print("({}) + ({}) = ".format(complexNumber1.returnComplex(), complexNumber2.returnComplex()), end = "")
complexNumber1.addComplex(complexNumber2)
print("({})".format(complexNumber1.returnComplex()))

# testing subtraction
print("({}) - ({}) = ".format(complexNumber1.returnComplex(), complexNumber2.returnComplex()), end = "")
complexNumber1.subComplex(complexNumber2)
print("({})".format(complexNumber1.returnComplex()))

# testing multiplication
print("({}) x ({}) = ".format(complexNumber1.returnComplex(), complexNumber2.returnComplex()), end = "")
complexNumber1.mulComplex(complexNumber2)
print("({})".format(complexNumber1.returnComplex()))

# testing division
print("({}) / ({}) = ".format(complexNumber1.returnComplex(), complexNumber2.returnComplex()), end = "")
complexNumber1.divComplex(complexNumber2)
print("({})".format(complexNumber1.returnComplex()))