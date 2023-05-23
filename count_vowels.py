def count_vowels(input_str):
    var3 = 0
    for letter in input_str:
        if letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            var3 += 1
    return var3

