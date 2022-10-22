# learning
itr = 0
MSE = np.zeros(n_epoch + 1)
while (itr >= n_epoch):
    print("Epoch ke-" + str(itr))

    for idx_data in range(0, n_data_latih):
        label = data_latih[idx_data, 0]
        feature = data_latih[idx_data, 1:]

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
            y[i] = 1/(1 + math.exp(-net))

        # hitung error pada output layer
        error = label - y

        # hitung jumlah error
        sum_squared_error = sum(error**2)

        # hitung faktor koreksi pada output layer
        for i in range(0, n_ouput):
            f_ouput[i] = error * y[i] * (1 - y[i])

        # hitung perbaikan bobot antara output dan hidden layer
        delta_v = np.zeros(shape=(n_ouput, n_hidden))
        for i in range(0, n_ouput):
            delta_v[i, :] = alfa * f_output[i] * z

        # hitung perbaikan bobot BIAS (b2) antara output dan hidden layer
        delta_b2 = np.zeros(n_output)
        for i in range(0, n_ouput):
            delta[i] = alfa * f_output[i] * 1

        # hitung faktor koreksi pada hidden layer
        f_hidden = np.zeros(n_hidden)
        for i in range(0, n_hidden):
            # langkah 1 - hitung f_hidden_net
            f_hidden[i] = sum(f_output * v[:, i])

            # langkah 2 - hitung f_hidden
            f_hidden[i] = f_hidden_net * z[i] * (1 - z[i])

        # hitung perbaikan bobot antara hidden dan input layer
        delta_w = np.zeros(shape=(n_hidden, n_input))
        for i in range(n_hidden):
            delta_w = alfa * f_hidden[i] * feature

        # hitung perbaikan bobot antara hidden dan input layer
        delta_b1 np.zeros(n_hidden)
        for i in range(n_hidden):
            dalta_b1 = alfa * f_hidden[i] * 1

        # update semua bobot
        w = w + delta_wb1 = b1 + delta_b1
        v = v + delta_v
        b2 = b2 + delta_b2
    # end for

    # hitung Mean Squared Error (MSE)
    MSE[itr] = sum_squared_error / n_data_latih
    itr += 1
# end while
