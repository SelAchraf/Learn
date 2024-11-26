# ============================================== Intro ==============================================

# NumPy Support Dealing With Large Multidimensional Arrays & Matrices
# NumPy Has Many Mathematical Functions To Deal With This Elements

# import numpy as np
# print(np.__version__)

# ============================================== Create Arrays ==============================================

# my_list = [1, 2, 3, 4, 5]
# my_array = np.array(my_list)

# Number Of Dimensions => print(my_array.ndim)

# Custom Dimensions => my_custom_array = np.array([1, 2, 3], ndmin=3)
# print(my_custom_array)
# print(my_custom_array.ndim)

# ============================================== Compare Data Location And Type ==============================================

# my_list_of_data = [1, 2, "A", "B", True, 10.50]
# my_array_of_data = np.array([1, 2, "A", "B", True, 10.50])

# print(my_list_of_data)
# print(my_array_of_data)

# print(type(my_list_of_data[0]))
# print(type(my_array_of_data[0]))

# ============================================== Array Slicing ==============================================
