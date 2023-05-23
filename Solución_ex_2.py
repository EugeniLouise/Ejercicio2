from user_input import get_user_input
from reverse_string import reverse_string
from count_vowels import count_vowels
from alter_case_multiple_2 import alter_case_2
from remove_spaces import remove_spaces

# Obtener entrada del usuario
var1 = get_user_input()

# Imprimir la entrada original
print("Original input: {}", var1)

# Invertir la cadena
var2 = reverse_string(var1)
print("Reversed output: {}", var2)

# Contar las vocales
var3 = count_vowels(var1)
print("Number of vowels: {}", var3)

# Alternar mayúsculas y minúsculas
var4 = alter_case_2(var1)
print("Altered case output: {}", var4)

# Eliminar espacios en blanco
var5 = remove_spaces(var1)
print("Output without spaces: {}", var5)