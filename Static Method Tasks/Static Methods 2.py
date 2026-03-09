from math import sqrt
class MathUtils:

    @staticmethod
    def is_even(n):
        if n%2 == 0:
            print(f"{n} is Even")
        else:
            print(f"{n} is odd")

    @staticmethod
    def is_prime(m):
        if m <= 1 :
            print("Not Prime !!")
        elif m == 2:
            print(f"{m} is the only even prime number !!")
        else:
            for i in range(2,int(sqrt(m))):
                if m%i == 0:
                    print(f"{m} is not prime")
                    break
            else:
                print(f"{m} is prime number")

MathUtils.is_even(24)
MathUtils.is_prime(13)       