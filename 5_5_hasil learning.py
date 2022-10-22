print("--------------RESULT--------------")
print("Mean Squared Error: " + str(MSE[n_epoch]))

# print grafik MSE hasil training
plt.title("Mean Sqared Error hasil training")
plt.plot(MSE)
plt.autoscale(enalble=True, axis='both', tight=None)
plt.show(block=False)
