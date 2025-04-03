import threading
import concurrent.futures


def simple_number(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_simple_numbers(numbers):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(simple_number, numbers))
    return results

num_list = [17, 25, 74, 199, 101, 41, 39, 50, 20, 19, 51]

simple_results = check_simple_numbers(num_list)

for num, result in zip(num_list, simple_results):
    print(f"{num} is {'simple' if result else 'not simple'} number.")

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = list(executor.map(simple_number, num_list))

# for num, result in zip(num_list, results):
#     print(f"{num} is {' simple' if result else 'not a simple'} number.")

num = int(input("Enter a number: "))
if simple_number(num):
    print(f"{num} is a simple number.")
else:
    print(f"{num} is not a simple number.")