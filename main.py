#FarellPriaAdhitama_2B_23090125
def konversi_biner(decimal):
    return bin(decimal)

def konversi_heksa(decimal):
    return hex(decimal)

def konversi_oktal(decimal):
    return oct(decimal)


bilangan_decimal = [23090125, 23090122, 23090142, 23090122, 23090235, 23090223]


for decimal in bilangan_decimal:
    print("Decimal:", decimal)
    print("Biner:", konversi_biner(decimal))
    print("Heksadesimal:", konversi_heksa(decimal))
    print("Oktal:", konversi_oktal(decimal))