#try:
    print (undefined_variable)
except NameError as f:
    print(f"NameError: {f}")#

# This program intentionally throws a NameError

def generate_name_error():
    # Trying to access an undefined variable
    print(undefined_variable)

# Calling the function that causes a NameError
generate_name_error()


