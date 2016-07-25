import math
class Complex():
    def __init__(self, real, comp):
        self.real = float(real)
        self.comp = float(comp)

    def __add__(self,that):
        r1 = self.real + that.real
        c1 = self.comp + that.comp
        return Complex(r1,c1)

    def __sub__(self,that):
        r1 = self.real - that.real
        c1 = self.comp - that.comp
        return Complex(r1,c1)
    
    def __mul__(self,that):
        r1 = self.real*that.real - self.comp*that.comp
        c1 = self.real*that.comp + self.comp*that.real
        return Complex(r1,c1)

    def __div__(self, that):
        den = that.real**2 + that.comp**2
        num = Complex(self.real, self.comp) * Complex(that.real, -1*that.comp)
        res = Complex(num.real/den, num.comp/den)
        return res 

    
    def mod(self):
        sol = math.sqrt(self.real**2 + self.comp**2)
        return Complex(sol, 0) 

    def __repr__(self):
        rs = "{0:.2f}".format(self.real)
        cs = "{0:.2f}".format(self.comp)
        sign = '+' if self.comp >= 0 else ''
        return str(rs) +sign + str(cs)+"i"


if __name__=="__main__":
    num1 = Complex(2,3)
    num2 = Complex(1,6)
    print num1, num2
    print num1+num2
    print num1-num2
    print num2-num1
    print num1*num2
    print num1.mod()
    print num2.mod()
    print num1/num2
