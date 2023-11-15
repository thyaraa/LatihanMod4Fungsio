# Curry function
def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Contoh penggunaan dengan Higher-Order Function (HOF)
def panggil_dengan_HOF():
    multiplier = perkalian(5)  # Menggunakan HOF untuk mendapatkan inner function
    result = multiplier(3)  # Memanggil inner function dengan argumen 3
    print(result)

panggil_dengan_HOF()  # Output: 15

# Contoh penggunaan dengan Currying
def panggil_dengan_currying():
    result = perkalian(5)(3)  # Memanggil langsung menggunakan currying
    print(result)

panggil_dengan_currying()  # Output: 15
