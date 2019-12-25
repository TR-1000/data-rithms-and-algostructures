
#FizzBuzz

numbers = [45, 22, 14, 65, 97, 72]

def fizzbuzz_classic(list):
  for n in list:
    if n%3 == 0 and n%5 == 0:
        print("fizzbuzz")

    elif n%5 == 0:
        print("buzz")

    elif n%3 == 0:
        print("fizz")

  print(list)    

  

def fizzbuzz_range(list):
  for i in range(len(list)):
    if list[i]%3==0 and list[i]%5==0:
      list[i] = "fizzbuzz"

    elif list[i]%3==0:
      list[i] = "fizz"

    elif list[i]%5==0:
      list[i] = "buzz"

  print(list)
  

def fizzbuzz_enumerate(list):
  for i,n in enumerate(numbers):
    if n%3==0 and n%5==0:
      list[i] = "fizzbuzz"

    elif n%3==0:
      list[i] = "fizz"

    elif n%5==0:
      list[i] = "buzz"
  
  print(numbers)


######## RECURSION #########

def power(num,pwr):
  if pwr == 0:
    return 1
  return num * power(num,pwr-1)





def factorial(n):
  if n == 1:
    return 1
  return n * factorial(n-1)

# num = int(input("choose a number greater than zero "))  

# print(factorial(num))


#Countdown
counter = 10
def inception():
  global counter
  if counter <= 0:
    return

  print (counter)  
  counter -= 1  
  return inception()





######### List Comprehention ##########

numbers = [x for x in range(1,101)]
squares = {num : num**2 for num in numbers}


# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(squares)


degrees = [ 12, 21, 15, 32 ]

fahreheit = [(9/5)*x+32 for x in degrees]

# n = int(input("Enter a number between 1 and 100: " ))
# divs = [x for x in range(n,101) if x%n==0]
# print(divs)

####### lambdas #######

#print((lambda x: x*2) (7))

####### OOP ########

class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
    self.name = name #attributes
    self.age = age

  def shout(self):
    print(f'my name is {self.name} !')

player1=PlayerCharacter("TR-1000", 38)

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Rags", 7)
cat2 = Cat("Sox", 2)
cat3 = Cat("Boots", 1)

# 2 Create a function that finds the oldest cat
oldest_cat = {}
oldest_age = 0
cats = (cat1, cat2, cat3)
for cat in cats:
  if cat.age > oldest_age:
    oldest_age = cat.age
    oldest_cat = cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# print(f"The oldest cat is {oldest_cat.name}.")

# def say_name(cat):
#   print(cat.name)

# for cat in cats:
#   say_name(cat)


class Animal():

  def make_sound(self):
    print("ROAR")

class Dog(Animal):
  species = 'canine'

# shaster = Dog()

fib_list = []
for index in range(5 + 1):
  if index == 0:
    fib_list.append(index)
  elif index == 1:
    fib_list.append(index)
  else:
    fib_list.append(fib_list[index - 1] + fib_list[index - 2])

print(fib_list[-1])    