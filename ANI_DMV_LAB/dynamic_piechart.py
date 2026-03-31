import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))

arr = []
for i in range(n):
    arr.append(int(input(f"Enter the height for {i+1}: ")))

plt.pie(arr)
plt.show()