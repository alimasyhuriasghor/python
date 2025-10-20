# 5. Data Types

# Integer (whole number)
data_integer = -5
print("The integer value: ", data_integer)
print("The data type of data_integer: ", type(data_integer))

# Float
pi = 3.141592653589
print("The floating point value: ", pi)
print("pi has a data type of: ", type(pi))

# String (str)
data_str = "Ali Ganteng"
print(data_str)
print("data_str has a data type of: ", type(data_str))

# Boolean
is_earth_flat = False
print(is_earth_flat)
print("is_earth_flat has a data type of: ", type(is_earth_flat))

# Spesific Data Types

# Complex number
data_complex = complex(5, 6)
print("Data: ", data_complex)
print("data_complex has a data type of: ", type(data_complex))

# Borrowing data type from C programming language
from ctypes import c_double

data_c_double = c_double(10.5)
print("Data: ", data_c_double)
print("data type: ", type(data_c_double))
