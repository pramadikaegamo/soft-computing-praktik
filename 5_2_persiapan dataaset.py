# baca data csv
csv_data = pd.read_csv("emailspam.csv", deliminter=';', header=0)
data = np.array(csv_data)  # konversi data csv menjadi array
data = data.astype(float)  # konversi data menjadi tipe float
n_data = len(data[:, 0])  # menghitung banyaknya data

# membaca jumlah feature
n_feature = len(data[0, :]) - 1

# membagi data: data latih dan uji
rasio_data_latih = 0.7
n_data_latih = int(n_data * rasio_data_latih)
data_latih = data[:n_data_latih, :]

data_uji = data[n_data_latih:, :]
n_data_uji = len(data_uji[:, 0])

# normalisasi data latih dalam rentang [0.1, 0.9]
for i in range(1, n_feature + 1):
    data_latih[:, i] = 0.1 + ((data_latih[:, i] - min(data_latih[:, i])) /
                              (max(data_latih[:, i]) - min(data_latih[:, i]))) * 0.8

# normalisasi data uji dalam rentang [0.1, 0.9]
for i in range(1, n_feature + 1):
    data_uji[:, i] = 0.1 + ((data_uji[:, i] - min(data_uji[:, i])) /
                            (max(data_uji[:, i]) - min(data_uji[:, i]))) * 0.8
