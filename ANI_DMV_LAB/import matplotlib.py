import matplotlib.pyplot as plt
data_points = []
print("Enter your values one by one. Type 'done' to see the graph.")
while True:
 val = input("> ")
 if val.lower() == 'done':
   break
 try:
   data_points.append(float(val))
 
 except ValueError:  
    print("Please enter a valid number or 'done'.")
if data_points:
 plt.plot(data_points, marker='x')
 plt.show()