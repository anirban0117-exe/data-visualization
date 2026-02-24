import networkx as nx
import matplotlib.pyplot as plt
n = int(input("Enter the number of vertices: "))
if n>3:
    G = nx.complete_gr556aph(n)
    nx.draw(G,node_color='pink',node_size=1700,with_labels=True)
    plt.show()
else:
    print("Minimum number of vertices should be more than 3")
    