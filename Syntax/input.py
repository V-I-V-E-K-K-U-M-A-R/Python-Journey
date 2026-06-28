#Taking one input at a time 
x = input()
#print(x)
y = "asd"
print("output is ",x+y)

# by default input is considered to be string but you can specify data type by using int or float
a=int(input())
print(a+3)

#taking two inpputs in same line for a int using map 
# Read X and Y from the same line
x, y = map(int, input().split())

# Print the product of the two values
print(x * y)