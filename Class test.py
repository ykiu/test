class thisTest:
    def aMethod(self):
        print ('this method')
    def bMethod(self):
        print ('that method')

class thatTest:
    def __init__(self):
        print ('Goodbye World')
    print ("Hello World")


thatTest()
thatTest()
thisTest()
d = thisTest()
d.aMethod()
