def point(x, y):
    return x, y


def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    # Hitung gradien (m)
    m = (y2 - y1) / (x2 - x1)

    # Gunakan salah satu titik untuk menghitung konstanta (c)
    c = y1 - m * x1

    return f"y = {m:.2f}x + {c:.2f}"


# Titik A dan B
A = point(1, 0)
B = point(6, 9)

# Temukan persamaan garis yang melalui titik A dan B
equation_AB = line_equation_of(A, B)

# Tampilkan hasil
print("Persamaan garis yang melalui titik A dan B:")
print(equation_AB)
