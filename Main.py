"""
number = 1
ifnumber = number + 5
print ("ok")
"""

""""
#mystring = "this is eshed's string"
print (mystring)"""

"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
print(x)
"""
"""
item1= "Hi, my name is {} and my lucky number is {}".format ("eshed",5)
print (item1)	
"""
"""
a = 3
b = 7
if b > a:
    print ("b is greater than a")
      """
"""
a=200
b=300
c=400
if a > b and c > b:
    print ("True")
"""
"""
a=800
b=990
if not a>b:
	print ("b is greater than a")
 """
"""
x = 30
if x > 10:
     print ("X is above 10",)
     if x > 20:
         print ("and also above 20!")
     else:
         print ("but not above 20.") 
         
         # if else (with also strings)
         """
""""
def my_function (fname):
 print (fname + " Assaraf")
 
my_function ("Eshed")
my_function ("Yarin")
my_function ("Liad")
#Arguments
"""
"""
i = 1
while i < 15:
  print(i)
  i += 1
else:
  print("i is now equal to 15")
"""
"""
for num in range (1, 51):
    print (num, ":", num % 2 == 0)
"""
"""""
for x in range (60):
    print (x)
    #for loop - range function
    """
""""
num = 1
while num <= 50:
    if num % 2 == 0:
        print(num, ": Even")
    else:
        print(num, ": Odd")
    num += 1
"""
 
"""
word = "communication"
num = (1,2,3,4,5,6,7,8,9,10,11,12,13)
i=1
for i in word:
        print (i)
       """ 
"""
x = lambda a: a + 15
print(x(10))
"""
"""""
for num in range (1, 51):
    print (num, ":", num % 2 == 0)
"""
"""
print("Even numbers:")
for i in range(2, 101, 2):
    print(i)

print("\nOdd numbers:")
for i in range(1, 101, 2):
    print(i)
    """
"""
for i in range(1, 101):
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")
# even / odd in range of 1-100 for each number 
    """
"""
number = input("Please enter a number:")
print("The number entered is:", number)
  """
"""
username = input("Please enter username:")
print("Welcome back,", username, "!")
"""


"""
def is_increasing(series):
    n = len(series)
    return all(int(series[i]) < int(series[i + 1]) for i in range(n - 1))

def find_periodic_number(series):
    n = len(series)
    for length in range(1, n // 2 + 1):
        if n % length == 0:
            period = series[:length]
            if period * (n // length) == series and is_increasing(period):
                return period
    return None

def main():
    series = input("Enter the series: ")
    periodic_number = find_periodic_number(series)
    if periodic_number:
        print(f"The periodic number in the series '{series}' is '{periodic_number}'.")
    else:
        print(f"This series '{series}' is not a periodic series that goes up.")

if __name__ == "__main__":
    main()
    """
    
"""
import math

def calculate_circle_area(radius):
    return math.pi * radius * radius

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_circle_area(radius)
    print(f"r = {radius}")
    print(f"Area = {area}")

if __name__ == "__main__":
    main()
"""
"""""
def is_valid_country(country):
    # List of valid countries (in lowercase)
    valid_countries = ["usa", "israel", "uk", "france", "germany", "japan", "china", "australia", "brazil", "india"]
    return country.lower() in valid_countries

def get_first_and_last_countries():
    input_countries = input("Enter up to 3 countries separated by spaces: ").strip().split()
    if len(input_countries) > 3:
        print("Input error: More than 3 countries entered.")
        return None, None

    for country in input_countries:
        if not is_valid_country(country):
            print(f"'{country}' is not a valid country.")
            return None, None

    return input_countries[0], input_countries[-1]

def main():
    input_countries = get_first_and_last_countries()
    if input_countries is not None:
        first_country = input_countries[0]
        last_country = input_countries[-1]
        print("First country is:", first_country)
        print("Last country is:", last_country)

if __name__ == "__main__":
    main()
"""
"""""
from datetime import datetime

date_input = lambda: datetime(*map(int, input("Enter a date (YYYY MM DD): ").split())).date()
date1, date2 = date_input(), date_input()
print("The amount of days between the two dates is:", abs((date2 - date1).days))
"""

"""
def sum_with_condition(num1, num2, num3):
    if num1 == num2 or num2 == num3 or num1 == num3:
        return 0
    else:
        return num1 + num2 + num3

# Get user input for the three integers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Calculate the sum with the condition
result = sum_with_condition(num1, num2, num3)
print("The sum with the condition is:", result)
"""
"""
def sum_with_condition(num):
    nums = num.split()
    if len(nums) != 2:
        return "Error: Only one number inserted"
    num1, num2 = map(int, nums)
    sum_result = num1 + num2
    return 20 if 15 <= sum_result <= 20 else sum_result
num = input("Enter two integers (please separate with space): ")
result = sum_with_condition(num)
print("The sum with the condition is:", result)
"""
"""
def check_values(num1, num2):
    return num1 == num2 or abs(num1 - num2) in {5, -5}
num1, num2 = map(int, input("Enter two numbers (Please separate by space): ").split())
print("Result:", check_values(num1, num2))
"""
"""
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = hours * 3600 + minutes * 60 + seconds

print(f"The total time in seconds is: {total_seconds} seconds")
"""

n = int(input("Enter the value of n: "))
total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of the first {n} positive integers is: {total}")
