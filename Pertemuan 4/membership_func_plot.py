from pyit2fls import zero_mf, singleton_mf, const_mf, tri_mf, ltri_mf, rtri_mf, trapezoid_mf, gaussian_mf
import matplotlib.pyplot as plt
from numpy import linspace

domain = linspace(0., 15, 1000)
# mySet = T1FS(domain, trapezoid_mf, [4, 6, 8, 10, 1.0])
# mySet.plot()


trapezoid = trapezoid_mf(domain, [4, 6, 8, 10, 1.0])
ltri = tri_mf(domain, [0, 4, 5, 1.0])
rtri = tri_mf(domain, [8, 10, 14, 1.0 ])

plt.figure()
plt.plot(domain, ltri, label="Ringan")
plt.plot(domain, trapezoid, label="Sedang")
plt.plot(domain, rtri, label="Berat")
plt.grid(True)
plt.legend()
plt.xlabel("Berat Pakaian")
plt.ylabel("Membership function")
plt.show()
