def penjumlahan(a, b):
    return a + b
def pengurangan(a, b):
    return a - b
def perkalian(a, b):
    return a * b   
def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"   
def modulus(a, b):
    return a % b
def pangkat(a, b):
    return a ** b
def akar(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "Error: Negative input for square root"
def faktorial(n):
    if n < 0:
        return "Error: Negative input for factorial"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def logaritma(a, base=10):
    import math
    if a > 0 and base > 1:
        return math.log(a, base)
    else:
        return "Error: Invalid input for logarithm"
def sinus(degrees):
    import math
    radians = math.radians(degrees)
    return math.sin(radians)
def cosinus(degrees):
    import math
    radians = math.radians(degrees)
    return math.cos(radians)
def tangen(degrees):    
    import math
    radians = math.radians(degrees)
    return math.tan(radians)
def cotangen(degrees):
    import math
    radians = math.radians(degrees)
    if math.tan(radians) != 0:
        return 1 / math.tan(radians)
    else:
        return "Error: Cotangent undefined for this angle"
def secan(degrees):
    import math
    radians = math.radians(degrees)
    if math.cos(radians) != 0:
        return 1 / math.cos(radians)
    else:
        return "Error: Secant undefined for this angle"
def cosecan(degrees):
    import math
    radians = math.radians(degrees)
    if math.sin(radians) != 0:
        return 1 / math.sin(radians)
    else:
        return "Error: Cosecant undefined for this angle"
def konversi_suhu(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin
def konversi_panjang(meter):
    kilometer = meter / 1000
    centimeter = meter * 100
    milimeter = meter * 1000
    return kilometer, centimeter, milimeter
def konversi_berat(kg):
    gram = kg * 1000
    miligram = kg * 1_000_000
    pound = kg * 2.20462
    return gram, miligram, pound
def konversi_waktu(detik):
    menit = detik / 60
    jam = detik / 3600
    hari = detik / 86400
    return menit, jam, hari
def konversi_volume(liter):
    mililiter = liter * 1000
    galon = liter / 3.78541
    return mililiter, galon
def konversi_kecepatan(km_per_jam):
    meter_per_detik = km_per_jam / 3.6
    mil_per_jam = km_per_jam / 1.60934
    return meter_per_detik, mil_per_jam
def konversi_data(byte):
    kilobyte = byte / 1024
    megabyte = byte / (1024 ** 2)
    gigabyte = byte / (1024 ** 3)
    return kilobyte, megabyte, gigabyte
