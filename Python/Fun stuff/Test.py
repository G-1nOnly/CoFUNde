class test():

    def __init__(self, str='Hello'):
        self.str = str
        self.__version = 1.0
        # Version could not be set due to property decorator

    @classmethod
    # Write cls instead of self
    def instantiate_from_str(cls, str):
        cls.str = str
        print("Okay, your string would be '"+cls.str+"'.")

    @staticmethod
    # No need to write self
    def get_len(str):
        return len(str)

    @property
    # No need to add() when called
    def test_input(self):
        if self.str == 'Hello':
            return "No input, still Hello."
        else:
            return "Your input would be "+self.str+"."

    @property
    # property decorator = Read_only attribute
    # "_" means protected and "__" means private
    def version(self):
        print("Getting version...")
        return self.__version

    @version.setter
    def version(self, ver):
        if not isinstance(ver,float):
            raise Exception("The version format is not correct, should be float, not others!")
        elif(ver <= 1.0):
            raise Exception("The version you set is not qualified, it is not updated!")
        else:
            print("Version set!")
            self.__version = ver

    @version.deleter
    # Could delete private the property type
    def version(self):
        print("Version deleted!")
        self.__version = 0.0

    def __repr__(self):
        # To customize for print function
        return "Testing "+self.str+'...' + "\n" + "Tested!!!"


test.instantiate_from_str("Nice to meet you!")
# static and class method could directly be called without an instance
t_len = test.get_len(test.str)
print(t_len)
test1 = test()
test2 = test("Hi")
print(test1)
print(test2)
print(test1.test_input)
print(test2.test_input)
print(test1.version)
print(test2.version)
# test1.version = 1
# test1.version = 1.0
test1.version = 2.0
print(test1.version)
del test2.version
print(test2.version)
