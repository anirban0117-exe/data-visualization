import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Cherry', 'Mango']
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels)
plt.title("Fruit Distribution")
plt.show()
