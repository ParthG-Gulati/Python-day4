# non keyword variable length argument

def add(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print("Sum:", sum)


add(10, 20)
add(10, 20, 30)

# keyword argument variable length

def my_func(**arg):
    for i, j in arg.items():
        print(i, j)


my_func(Name="Parth", Lastname="Gulati")
