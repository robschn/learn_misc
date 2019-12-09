# Closures

# def out_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = out_function('Hi')
# bye_func = out_function('Bye')

# hi_func()
# bye_func()

# Decorators

def decorator_function(orginal_function):
    def wrapper_function():
        print(f'wrapper executed this before {orginal_function.__name__}')
        return orginal_function()
    return wrapper_function

def display():
    print('display function ran')

decorator_display = decorator_function(display)

decorator_display()
