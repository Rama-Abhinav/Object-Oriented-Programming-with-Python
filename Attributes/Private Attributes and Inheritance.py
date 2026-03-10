class Parent:

    def __init__(self, secret):
        self.__secret = secret

    def reveal_secret(self):
        return self.__secret
    
class Child(Parent):

    def Child_Secret(self):
        return self.__secret
    
C = Child(10)
print(C._Parent__secret) # Python tranform _secret into _Parent__secret to prevent subclasses from accidentally overriding internal state.
print(C.reveal_secret())

