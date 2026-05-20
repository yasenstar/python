from pyvis.network import Network

net = Network(notebook=True)

for i in range(10):
    net.add_node(i, label=f"AI={i}")

for i in range(9):
    net.add_edge(i, i+1)

net.show("network.html")