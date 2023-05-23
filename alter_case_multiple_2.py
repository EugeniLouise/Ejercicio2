def alter_case_2(input_str):
    var4 = ""
    for i in range(len(input_str)):
        if i % 2 == 0:
            var4 += input_str[i].upper()
        else:
            var4 += input_str[i].lower()
    return var4

