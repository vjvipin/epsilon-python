class Complex():
    def __init__(self, real1 = 0.0, img1=0.0):  ##construtor method
        self.real = real1
        self.img = img1
        print ("I am printing from the constructor", self.real, self.img)

    def printcomplex(self):
        print (self.real,"+ i",self.img)

X = Complex(3,4)

X.printcomplex();

#    def __add__(self, other):
#        print ("Within Addition method")
#        real1 = self.real + other.real
#        img1 = self.img + other.img
#        Z = Complex(real1,img1)
#        return Z
#        # return Complex(self.real + other.real,
#        #                self.img + other.img)
#    def __str__(self):
#        # return '%d + i %d' % (self.real, self.img)
#        return str(self.real) + '+ i' + str(self.img) 
#
#
#    def __sub__(self, other):
#        return Complex(self.real - other.real,
#                       self.img - other.img)
#
#
#    def __mul__(self, other):
#        return Complex(self.real*other.real - self.img*other.img,
#                       self.img*other.real + self.real*other.img)

'''
    def distance(self,other):
    def __div__(self, other):
        sr, si, otr, oi = self.real, self.img, \
                            other.real, other.img # short forms
        r = float(otr**2 + oi**2)
        return Complex((sr*otr+si*oi)/r, (si*otr-sr*oi)/r)

    def __abs__(self):
        return sqrt(self.real**2 + self.img**2)

    def __neg__(self):
        return Complex(-self.real, -self.img)

    def __eq__(self, other):
        return self.real == other.real and self.img == other.img

    def __ne__(self, other): # !=
        return not self.__eq__(other)

'''
