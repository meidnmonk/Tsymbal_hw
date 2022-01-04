# ------------------------------------- 1 ----------------------------------
print("Task 1")
a = "hello"
b = "world!"
print(f"{a}, {b}")
numb1 = int(input("Enter any number: "))
numb2 = int(input("Enter any number once more: "))
print(f"You chose numbers {numb1} and {numb2}")
word = input("Enter any word: ")
print(f"{word} - it's good choice")
print(
)
# ------------------------------------- 2 ----------------------------------
print("Task 2")
time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = time // 3600 - hours * 60
seconds = time % 60
print(f"{hours}:{minutes}:{seconds}")
print(
)
# ------------------------------------- 3 ----------------------------------
print("Task 3")
n = input("Enter integer: ")

while n <= '0':
    print('I asked for number greater than 0. Please try again.')
    n = input('Please enter number greater than 0: ')

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")
print(
)
# ------------------------------------- 4 ----------------------------------
print("Task 4")
num_init = int(input('Insert natural number: '))
greatest_dig = 0
num = num_init

while num > 0:
    digit = num % 10
    if digit > greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    num = num // 10

print(f"The biggest digit in number {num_init} is {greatest_dig}")
print(
)
# ------------------------------------- 5 ----------------------------------
print('Task 5')
revenue = float(input("Insert revenue: "))
costs = float(input('Insert costs: '))
result = revenue - costs
if result > 0:
    print(f"Congrats! Your company workflow is positive - {result}")
    print(f"Profitability equals {100 * result / revenue}%")
    personal_n = int(input("How many employees work in your company? "))
    print(f'Each emploee can get {result / personal_n}')
elif result < 0:
    print(f"Your company has negative result {result}")
else:
    print('0 is also a good result!')
print(
)
# ------------------------------------- 6 ----------------------------------
print('Task 6')

while True:
    days = 1
    start_km = float(input("Start result: "))
    last_km = float(input("Final result: "))
    if start_km <= 0 or last_km < 0:
        print('Result has to be bigger than 0')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1
        print(f'Sportsman will reach the result in {days} days')
        break
