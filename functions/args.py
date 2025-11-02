# Example of function with positional, *args and **kwargs
def func(a,b,*args,**kwargs):
    print(f"a;{a},b:{b}")
    print("args",args)
    print("kwargs",kwargs)



func(1,2,4,5,6,name="karthik",age=23)
