# def factorial(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f
# n = int(input("enter a number:"))
# result = factorial(n)
# print(result)


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# n = int(input("enter a number:"))
# print(is_prime(n))


# def count_vowels(text):
#     count = 0
#     for char in text.lower():
#         if char in "aeiouAEIOU":
#             count += 1
#     return count
# n = input("enter text:")
# print(count_vowels(n))


# def reverse_string(text):
#     return text[::-1]
# n = input("enter text:")
# print(reverse_string(n))

# def reverse_string(text):
#     reverse = ""
#     for char in text:
#         reverse = char + reverse
#     return reverse
# n=input("enter text:")
# print(reverse_string(n))


# def is_palindrome(text):
#     reverse = ""
#     for char in text:
#         reverse = char + reverse
#     if text.lower() == reverse.lower():
#         return True
#     else:
#         return False
# n = input("enter text:")
# print(is_palindrome(n))


# def list_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total
# n = input("enter numbers:")
# numbers = n.split(",")
# numbers = [int(x) for x in numbers]
# print(list_sum(numbers))


# def find_largest(numbers):
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#     return largest
# n = input("enter numbers")
# numbers = [int(x) for x in n.split(",")]
# print(find_largest(numbers))


# def count_even(numbers):
#     count = 0
#     for num in numbers:
#         if num % 2 == 0:
#             count += 1
#     return count
# n = input("enter numbers:")
# numbers = [int(x) for x in n.split(",")]
# print(count_even(numbers))


# def multiplication_table(n):
#     for i in range(1,11):
#         print(f"{i} * {n} = {i*n}")
# n = int(input("enter number:"))
# multiplication_table(n)


# def calculate_result(mark1,mark2,mark3):
#     avg = (mark1 + mark2 + mark3) / 3
#     if avg >= 50:
#         return "pass"
#     else:
#         return "fail"
# n = input("enter numbers:")
# numbers = [int(x) for x in n.split(",") ]
# print(calculate_result(*numbers))




# def is_disarium(number):
#     num_str = str(number)
#     total = 0
#     for i in range(len(num_str)):
#         digit = int(num_str[i])
#         position = i+1
#         total += digit ** position
#     if total == number:
#         return f"{number} is a disarium number"
#     else:
#         return f"{number} is not a disarium number"
# n = int(input("enter number:"))
# print(is_disarium(n))



def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left = 0
    right = len(s_list) - 1

    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return "".join(s_list)
s = input("enter string:")
print(reverse_vowels(s))