import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Henter inn ett ferdiglaget dataset
G = nx.karate_club_graph()
nodes = G.nodes()

# Printer ut liste over alle noder og kanter
def task1():
    print(G.node_attr_dict_factory(G.nodes()))
    print(G.edge_attr_dict_factory(G.edges()))

# Gir de to forskjellige gruppene i datasettet fargen "blue" eller "orange"
def task2():
    colorNodes = []
    for(k,v) in nodes(data=True):
        if v['club'] == "Mr. Hi":
            colorNodes.append('blue')
        else:
            colorNodes.append('orange')

    nx.draw(G, node_color = colorNodes, with_labels = True)
    plt.show()

# Finner korteste vei fra node 24 til node 16, printer nodene på veien
def task3():
    shortestPath = nx.dijkstra_path(G, source=24, target=16)
    return(shortestPath) 

# Lager en framstilling av datasettet. 
def task4():
    colorNodes = []
    for(k,v) in nodes(data=True):
        if k in task3(): 
            colorNodes.append('red')
        elif v['club'] == "Mr. Hi":
            colorNodes.append('blue')
        else:
            colorNodes.append('orange')

    nx.draw(G, node_color = colorNodes, with_labels = True)
    
    plt.show()
    

#task1()
#task2()
#task3()
task4()
