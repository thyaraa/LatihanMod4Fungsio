def point(x, y):
    return x, y


def line_equation_of(p1, m):
    # Inner function untuk menghitung nilai C
    def calculate_c(x, y):
        return y - m * x

    # Mendapatkan nilai C dengan memanggil inner function
    C = calculate_c(*p1)

    return f"y = {m:.2f}x + {C:.2f}"


# Menampilkan persamaan garis yang melalui titik (6,-2) dan bergradien -2
print("Persamaan garis yang melalui titik (0,6) dan bergradien 9:")
print(line_equation_of(point(0, 6), 9))
