"""
2.3 Inference
"""
# mengisi derajat keanggotaan untuk tiap nilai linguistik pada variabel 'berat_pakaian'
var1_ringan, var1_sedang, var1_berat = fuzzy_berat_pakaian

# mengisi derataj keanggotaan untuk tiap nilai linguistik pada variabel 'intensitas_kotor'
var2_rendah, var2_tinggi = fuzzy_intensitas_kotor

# nilai linguistik untuk output 'durasi_cuci' ('cepat', 'sedang', 'lama')
output_cepat = [0, 0]
output_sedang = [0, 0]
output_lama = [0, 0]

# inferecy dan mengambil nilai minimum antara varl dan var2
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

# hitung nilai fuzy output dengan mengambil nilai maksimum dari hasil inferensi
fuzzy_output_cepat = max(output_cepat)
fuzzy_output_sedang = max(output_sedang)
fuzzy_output_lama = max(output_lama)
