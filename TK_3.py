def tk_3(array):
    average_array = []
    average = sum(array) / len(array)
    for i in array:
        average_array.append(i / average)
    return average_array
