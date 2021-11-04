def tk_4(array):
    multiply_array = []
    average = sum(array) / len(array)
    for i in array:
        multiply_array.append(i * average)
    return multiply_array
