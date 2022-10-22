# insialisasi parameter jst
n_input = n_feature  # jumlah neuron pada input layer
n_hidden = 0  # jumlah neuroon pada hidden layer
n_output = 1  # jumlah neuron pada output layer
n_epoch = 0  # jumlah epoch/ iterasi maksimal
alfa = 0  # learning rate

# inisialisasi bobot MLP dalam rentang (-1,1)
w = np.random.rand(n_hidden, n_input) * 2 - 1
b1 = np.random.rand(n_hidden) * 2 - 1
v = np.random.rand(n_output, n_hidden)  # * 2 - 1
b2 = np.random.rand(n_output) * 2 - 1
