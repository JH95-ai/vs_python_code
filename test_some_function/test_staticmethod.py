#@staticmethod是把函数嵌入到类中的一种方式，函数就属于类，
#同时表明函数不需要访问这个类。通过子类的继承覆盖，能更好的组织代码。
class A(object):
    def foo(self, x):
        print("executing foo(%s,%s)" % (self, x))
        print('self:', self)
    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s,%s)" % (cls, x))
        print('cls:', cls)
    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)    
a = A()
print(a.foo)
print(a.class_foo)
print(a.static_foo)
print(A.static_foo)
