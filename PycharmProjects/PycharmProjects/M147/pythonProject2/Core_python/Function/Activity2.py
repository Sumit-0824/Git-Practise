# 1.Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True
def check_sequence(nums):
    return [1, 2, 3] in [nums[i:i+3] for i in range(len(nums)-2)]

print(check_sequence([1, 1, 2, 3, 1]))  # True
print(check_sequence([1, 1, 2, 4, 1]))  # False
print(check_sequence([1, 1, 2, 1, 2, 3]))# True

#2. Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(s):
    return s[::2]

print(stringBits('Hello'))      # 'Hlo'
print(stringBits('Hi'))         #'H'
print(stringBits('Heeololeo'))  #'Hello'


# 3.Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(s1, s2):
    return s1.lower().endswith(s2.lower())

print(end_other('Hiabc', 'abc'))    #True
print(end_other('AbC', 'HiaBc'))    # True
print(end_other('abc', 'abXabc'))   # True




# 4.Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(s):
    return ''.join([char * 2 for char in s])
print(doubleChar('The'))               #TThhee
print(doubleChar('AAbb'))              #AAAAbbbb
print(doubleChar('Hi-There'))          #HHii--TThheerree

#5. teen -- in the range 13-19[13,14,17,18,19] inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def fix_teen(n):
    if 13 <= n <= 19 and n not in [15, 16]:
        return 0
    return n

def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

print(no_teen_sum(1, 2, 3))   #6
print(no_teen_sum(2, 13, 1))  #3
print(no_teen_sum(2, 1, 14))  #3


# 6.Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
    return sum(1 for num in nums if num % 2 == 0)
print(count_evens([2, 1, 2, 3, 4]))  #3
print(count_evens([2,2,0]))          #3
print(count_evens([1,3,5]))          #3
