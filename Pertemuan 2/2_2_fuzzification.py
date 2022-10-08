def fuzification(crisp_input, batas_nilai, posisi_grafik):
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
