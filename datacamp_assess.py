'''
This is my Datacamp assessment questions that I got wrong
Broken into: 2 set
'''

#Set 1
#1
with open('hello.txt', 'w') as file:
  file.write("hello!")

print(file.closed)

#2
ints = set([1,1,2,3,3,3,4])
print(len(ints))

#3
letters = ['a', 'b', 'c']
for ii, x in enumerate(letters):
    print(ii, ": ", x)

#4
class Dog:    
    def woof(self):
        return 'woof!'

t = Dog()
t.woof()

#5
def number_squared(x):
    print(x ** 2)
  
number_squared(3)

#6
class Planet:
    def __init__(self, name):
        self.name = name
        
v = Planet('venus')

v.name

#7
[i * 3 for i in range(5)]

#8
class Color:
    def __init__(self, rgb_value):
        self.rgb_value = rgb_value

c = Color('#00ff66')

c.rgb_value

# Set 2
def hours_to_seconds(hours):
    return hours * 60 * 60

hours_to_seconds(8)


car = {
    'brand': 'Ferrari',
    'model': 'model',
    'year': 2019
}

type(car)


[s.upper() for s in ['hello', 'world']]


[i for i in range(5) if i > 2]

class Planet:
    def __init__(self, name, diameter_km):
        self.name = name
        self.diameter_km = diameter_km
        
e = Planet("Earth", 12742)

e.name, e.diameter_km


class AstroBody:
    description = 'Natural entity in the observable universe.'    

class Star(AstroBody):
    pass

sun = Star()

sun.description

# 'Natural entity in the observable universe.'

def make_dict(**kwargs):
    return kwargs

make_dict(a = 1, b = 2)
# {'a': 1, 'b': 2}

def add_many(*args):
    s = 0
    for n in args:
        s += n
    print(s)

add_many(100, 50, 3)

# 153

def factorial(n):
    """returns n!"""
    return 1 if n < 2 else n * factorial(n-1)

factorial.__doc__

# 'returns n!'

import random
random.seed(2427)

def efficient_sample(n):
  x = [random.random() for i in range(n)]
  return x

efficient_sample(20)

d = {
    'apple': 1,
    'banana': 2,
    'coconut': 3
}

d['durian'] = 4

d

# {'apple': 1, 'banana': 2, 'coconut': 3, 'durian': 4}

