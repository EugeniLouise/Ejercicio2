def reverse_string(input_str):
    var2 = ""
    for i in range(len(input_str) - 1, -1, -1):
        var2 += input_str[i]
    return var2

