# exceptiontest.py

class A(object):
    def function(self):
        print 'aaaaa'

class B(A):

    def function(self):
        super(A,self).function()
        print 'bbbbb'

