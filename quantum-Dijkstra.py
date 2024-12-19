from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def dijkstra_qiskit(graph, start, end):
    num_nodes = len(graph)
    qc = QuantumCircuit(num_nodes)
    
    qc.h(range(num_nodes)) 
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if graph[i][j] > 0:  
                angle = 2 * np.pi * graph[i][j] / np.sum(graph)  
                qc.ry(angle, j)
    
    qc.measure_all()
    
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1024).result()
    counts = result.get_counts()
    
    best_path = min(counts, key=lambda x: sum([int(bit) for bit in x]))
    return best_path

graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 0, 0],
    [0, 2, 3, 0, 0, 1],
    [0, 7, 0, 0, 0, 6],
    [0, 0, 0, 1, 6, 0],
]

path = dijkstra_qiskit(graph, 0, 5)
print("Caminho mínimo estimado:", path)
