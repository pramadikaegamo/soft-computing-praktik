"""
nama : pramadika egamo
nim  : 5200411193


2.2 Fuzzification
"""


def fuzzification(crisp_input, batas_nilai, posisi_grafik):
    fuzzy_input = 0

    # jika letak grafik di awal
    if (posisi_grafik == 'awal'):
        if (crisp_input <= batas_nilai[1]):
            fuzzy_input = 1
        elif (crisp_input > batas_nilai[1 and crisp_input < batas_nilai[2]]):
            fuzzy_input = (batas_nilai[2] - crisp_input) / \
                (batas_nilai[2] - batas_nilai[1])
        else:
            fuzzy_input = 0
    # jika letak grafik di tengah
    elif (posisi_grafik == 'tengah'):
        if (crisp_input > batas_nilai[0] and crisp_input < batas_nilai[1]):
            fuzzy_input = (
                crisp_input - batas_nilai[0]) / (batas_nilai[1] - batas_nilai[0])
        elif (crisp_input >= batas_nilai[1] and crisp_input <= batas_nilai[2]):
            fuzzy_input = 1
        elif (crisp_input > batas_nilai[2] and crisp_input < batas_nilai[3]):
            fuzzy_input = (batas_nilai[3] - crisp_input) / \
                (batas_nilai[3] - batas_nilai[2])
        else:
            fuzzy_input = 0
    # jika letak grafik di akhir
    elif (posisi_grafik == 'akhir'):
        if (crisp_input <= batas_nilai[0]):
            fuzzy_input = 0
        elif (crisp_input > batas_nilai[0] and crisp_input < batas_nilai[0] and crisp_input < batas_nilai[1]):
            fuzzy_input = (
                crisp_input - batas_nilai[0]) / (batas_nilai[1] - batas_nilai[0])
        else:
            fuzzy_input = 1

    return fuzzy_input


"""
2.4 Defuzzification
- Mamdani
"""


def defuzzification_mamdani(fuzzy_output, batas_nilai, posisi_grafik):
    x = 0

    # jika letak grafik di awal
    if (posisi_grafik == 'awal'):
        if (fuzzy_output <= batas_nilai[1]):
            x = batas_nilai[1]
        elif (fuzzy_output > batas_nilai[1] and fuzzy_output < batas_nilai[2]):
            x = batas_nilai[2] - \
                (fuzzy_output * (batas_nilai[2] - batas_nilai[1]))
        else:
            x = batas_nilai[2]
    # jika letak grafik di tengah
    elif (posisi_grafik == 'tengah'):
        if (fuzzy_output > batas_nilai[0] and fuzzy_output < batas_nilai[1]):
            x = (fuzzy_output *
                 (batas_nilai[1] - batas_nilai[0])) + batas_nilai[0]
        elif (fuzzy_output >= batas_nilai[1] and fuzzy_output <= batas_nilai[2]):
            x = batas_nilai[2]
        elif (fuzzy_output > batas_nilai[2] and fuzzy_output < batas_nilai[3]):
            x = batas_nilai[3] - \
                (fuzzy_output * (batas_nilai[3] - batas_nilai[2]))
        else:
            x = batas_nilai[3]
    # jika letak grafik di akhir
    elif (posisi_grafik == 'akhir'):
        if (fuzzy_output <= batas_nilai[0]):
            x = batas_nilai[0]
        elif (fuzzy_output > batas_nilai[0] and fuzzy_output < batas_nilai[1]):
            x = (fuzzy_output *
                 (batas_nilai[1] - batas_nilai[0])) + batas_nilai[0]
        else:
            x = 1

    return x


"""
2.5 Studi Kasus
- Durasi mesin cuci
- Seleksi karyawan baru
"""

# input data
berat_pakaian = float(input("Berat pakaian (kg) : "))
intensitas_kotor = float(input("Intensitas kotor (%) : "))

# ===============================================================================
# fuzzification
# ===============================================================================
# fungsi keanggotaan untuk varibel linguistik "berat_pakaian : TRAPESIUM"
batas_var1_ringan = [0, 4, 6]
batas_var1_sedang = [4, 6, 8, 10]
batas_var1_berat = [8, 10, 14]
fuzzy_berat_pakaian = [0, 0, 0]  # ringan, sedang, berat

# hitung fuzzy input "berat_pakaian": "ringan"
fuzzy_berat_pakaian[0] = fuzzification(
    berat_pakaian, batas_var1_ringan, 'awal')

# hitung fuzzy input "berat_pakaian": "sedang"
fuzzy_berat_pakaian[1] = fuzzification(
    berat_pakaian, batas_var1_sedang, 'tengah')

# hitung fuzzy input "berat_pakaian": "berat"
fuzzy_berat_pakaian[2] = fuzzification(
    berat_pakaian, batas_var1_berat, 'akhir')

print(fuzzy_berat_pakaian)

# ----------------------------------------------------------------------------------

# fungsi keanggotaan untuk variabel linguistik "intensitas_kotor" : SEGITIGA
batas_var2_rendah = [0, 20, 60]
batas_var2_tinggi = [20, 60, 100]
fuzzy_intensitas_kotor = [0, 0]  # rendah, tinggi

# hitung fuzzy input "intensitas_kotor": "rendah"
fuzzy_intensitas_kotor[0] = fuzzification(
    intensitas_kotor, batas_var2_rendah, 'awal')

# hitung fuzzy input "intensitas_kotor": "tinggi"
fuzzy_intensitas_kotor[1] = fuzzification(
    intensitas_kotor, batas_var2_tinggi, 'akhir')

print(fuzzy_intensitas_kotor)

"""
inferency
"""
# ===============================================================================
# inferency (fuzzy rules)
# ===============================================================================
# mengisi derajat keanggotaan untuk tiap nilai lingusitik pada variabel 'berat_pakaian'
var1_ringan, var1_sedang, var1_berat = fuzzy_berat_pakaian

# mengisi derajat keanggotaan untuk tiap nilai linguistik pada variabel 'intensitas_kotor'
var2_rendah, var2_tinggi = fuzzy_intensitas_kotor

# nilai linguistik untuk outpus 'durasi_cuci' {'cepat', 'sedang', 'lama'}
output_cepat = [0, 0]
output_sedang = [0, 0]
output_lama = [0, 0]

# inferency dan mengambil nilai minimum antara var1 dan var2
if (var1_ringan > 0 and var2_rendah > 0):
    output_cepat[0] = min(var1_ringan, var2_rendah)
if (var1_ringan > 0 and var2_tinggi > 0):
    output_sedang[0] = min(var1_ringan, var2_tinggi)
if (var1_sedang > 0 and var2_rendah > 0):
    output_cepat[1] = min(var1_sedang, var2_rendah)
if (var1_sedang > 0 and var2_tinggi > 0):
    output_lama[0] = min(var1_sedang, var2_tinggi)
if (var1_berat > 0 and var2_rendah > 0):
    output_sedang[1] = min(var1_berat, var2_rendah)
if (var1_berat > 0 and var2_tinggi > 0):
    output_lama[1] = min(var1_berat, var2_tinggi)

# hitung nilai fuzzy output dengan mengambil nilai maksimum dari hasil inferensi
fuzzy_output_cepat = max(output_cepat)
fuzzy_output_sedang = max(output_sedang)
fuzzy_output_lama = max(output_lama)

print(fuzzy_output_cepat, fuzzy_output_sedang, fuzzy_output_lama)

# ===============================================================================
# defuzzification (weigted average/ Tsukamoto)
batas_out_cepat = [0, 30, 50]
batas_out_sedang = [30, 50, 70, 100]
batas_out_lama = [70, 100, 120]
durasi_cuci = [0, 0, 0]  # cepat, sedang, lama

# hitung nilai 'durasi cuci' dari nilai fuzzy output
# durasi_cuci[0] =
y = [x+2 for x in range(0, 20)]
print(y)
