label = data_uji[idx_data, 0]
feature = data_uji[idx_data, 1:]

# hitung nilai pada hidden layer
z = np.zeros(n_hidden)
for i in range(0, n_hidden):
    net = np.sum(feature * w[i]) + b1[i]
    z[i] = 1 / (1 + math.exp(-net))

# hitung nilai pada output layer
y = np.zeros(n_output)
f_output = np.zeros(n_output)
for i in range(0, n_output):
    net = np.sum(z * v[i]) + b2[i]
    y[i] = 1 / (1 + math.exp(-net))

    # pembulatan y[i] ke 0 atau 1
    if (y[i] >= 0.5):
        y[i] = 1
    else:
        y[i] = 0
