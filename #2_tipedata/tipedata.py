# BELAJAR TIPE DATA PYTHON
from ctypes import c_double
data_int = 10
print('data = ', data_int, 'bertipe = ', type(data_int))

data_float = 20.4
print('data = ', data_float, 'bertipe = ', type(data_float))

data_str = "aww"
print('data = ', data_str, 'bertipe = ', type(data_str))

data_bool = True
print('data = ', data_bool, 'bertipe = ', type(data_bool))


# TIPE DATA KHUSUScd

# bilangan kompleks
data_complex = complex(5, 10)
print('data = ', data_complex, 'bertipe = ', type(data_complex))

# tipe data dari bahasa C
dataCDouble = c_double(10.50)
print('data = ', dataCDouble, 'bertipe = ', type(dataCDouble))
