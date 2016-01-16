######## 1

# def some_func(a=9, b=5):
#     c = a - b
#     print(c)
#     return c
#
# some_func(a=3, b=4)
#
# some_func(3, 5)
#
# some_func()
#
#
# def fibo(n):
#     return some_func(400, 200)
#
# fibo(3)

####### 2
# a = 1
# b = 8
# c = 8
# d = 10
# while b > 3:
#     a += 1
#     b -= 1
#
#     while c > 4:
#         b -= 2
#         c -= 1
#         while d > 4:
#             b -= 1
#             d -= 1
#             print ("inner most", a,b)
# print(a,b, c, d)

####### 3
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
#
a = fact(5)
print(a)
####### 4
# a = 1
# print(a)









