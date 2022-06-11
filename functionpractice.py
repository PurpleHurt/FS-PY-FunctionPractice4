#Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
    return max([x, y, z])

print(max_num(1, 2, 3))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(List):
    x = 1
    for i in List:
        x = x * i 
    return x

list1 = [1, 2, 3]
print(mult_list((list1)))


#Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]

print(rev_string("Hello World"))

#Write a Python function called num_within() to check whether a number falls in a given range.
#  The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#  Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x, y, z):
    return x in range(y, z)

print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))


#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#  The function accepts the number n, the number of rows to print
#  Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.


def pascal(n):
    triangle = [1]
    y = [0]
    for x in range(n):
        print(triangle)
        triangle = [left+right for left,right in zip(triangle+y, y+triangle)]
        
    
pascal(6)
