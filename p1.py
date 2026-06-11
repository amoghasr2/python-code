a = 121
if str(a)==str(a)[::-1]:
    print(a,"is a palindrome")
else:
    print(a,"is not a palindrome")


n = list(range(-25,26))
print(n)
negative = [num for num in n if num<0]
print(negative)
positive = [num for num in n if num>0]
print(positive)
zero = [num for num in n if num==0]
print(zero)


