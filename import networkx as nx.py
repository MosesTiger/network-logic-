import networkx as nx
import matplotlib.pyplot as plt

vertics = range(1, 10)
edges = [(7, 2), (2, 3), (7, 4), (4, 5), (7, 3), (7, 5), (1, 6), (1, 7), (2, 8), (2, 9)]

G = nx.Graph()
G.add_nodes_from(vertics)
G.add_edges_from(edges)

pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, nodelist=[1, 4, 3, 8, 9], node_color='g', node_size=1300)
nx.draw_networkx_nodes(G, pos, nodelist=[2, 5, 6, 7], node_color='r', node_size=1300)

nx.draw_networkx_edges(G, pos, edges, width=3, alpha=0.5, edge_color='b')

labels = {}
labels[1] = r'1 NF'
labels[2] = r'2 F'
labels[3] = r'3 NF'
labels[4] = r'4 NF'
labels[5] = r'5 NF'
labels[6] = r'6 NF'
labels[7] = r'7 NF'
labels[8] = r'8 NF'
labels[9] = r'9 NF'

nx.draw_networkx_labels(G, pos, labels, font_size=16)

plt.show()