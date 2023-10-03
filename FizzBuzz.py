class FizzBuzz:
    def affiche (self, n1,n2):

        for i in range(n1, n2 + 1):
            output = ""
            if i % 3 == 0 and i % 5 == 0:
                output ="FrisBee"
            elif i % 3 == 0:
                output ="Fizz"
            elif i % 5 == 0:
                output ="Buzz"
            else:
                output = str(i)

            print(output)

FB = FizzBuzz()

FB.affiche(55,70)








