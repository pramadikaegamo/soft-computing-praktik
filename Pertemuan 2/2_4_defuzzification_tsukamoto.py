def defuzzification_tsukamoto(fuzzy_output, batas_nilai, posisi_grafik):
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
