
file = 'titanic.csv'
data = np.genfromtxt(file, delimiter=',', names=True, dtype=None)
np.shape(data)
data[0]