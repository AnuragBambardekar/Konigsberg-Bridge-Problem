import networkx as nx
import matplotlib.pyplot as plt

def plot_konigsberg_bridge_problem():
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

    # Graph
    plt.figure(figsize=(6, 6))
    pos = nx.spring_layout(graph, seed=42) 
    nx.draw(graph, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', width=2.0)
    plt.title("Königsberg Bridge Problem")
    plt.show()

def konigsberg_bridge_problem():
    # Graph
    graph = nx.Graph()
    graph.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

    # Check if the graph has an Eulerian path
    is_eulerian = nx.is_eulerian(graph)

    if is_eulerian:
        print("An Eulerian path exists. The Königsberg Bridge Problem is solvable.")
        eulerian_path = list(nx.eulerian_circuit(graph))
        print("Eulerian Path:")
        print(" -> ".join([node for node, _ in eulerian_path]))
    else:
        print("No Eulerian path exists. The Königsberg Bridge Problem is unsolvable.")

if __name__ == "__main__":
    plot_konigsberg_bridge_problem()
    konigsberg_bridge_problem()
