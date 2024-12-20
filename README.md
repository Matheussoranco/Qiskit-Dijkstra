# Qiskit-Dijkstra
Dijkstra's algorithm is a classic method for finding the shortest path between nodes in a graph. Translating Dijkstra to quantum computing requires reformulation, as quantum computing operates with qubits, superposed states, and quantum circuits, while Dijkstra is inherently sequential.
Challenges in Adaptation
These are some of the problems i've encountered adapting the algorithm to a quantum state.

    Sequentiality vs. Parallelism:
        Dijkstra relies on sequential updates of minimum distances, whereas quantum computing is naturally parallel.
        To "adapt" the algorithm, i needed to map the process to quantum operations.

    Mathematical Operations:
        Quantum computing works with unitary linear transformations and probabilistic measurements. Simulating comparisons, minimums and value updates requires specific translations.

    Memory and States:
        The state of the graph (distances, nodes visited) must be stored in qubits, which may require many qubits and deep circuits for larger simulations.

    State Measurement and Destruction:
        Measurement on the quantum computer collapses the quantum state, making it difficult to store lossless intermediates.

Mathematical Considerations

Superposition States:
    For nn nodes, the initial state would be ∣ψ⟩=1n∑i=0n−1∣i⟩∣ψ⟩=n

​1​∑i=0n−1​∣i⟩, where each node is represented by a quantum state.

Weights as Rotation:
 I used rotations Ry(θ)Ry​(θ), where θ=2π⋅normalized weightθ=2π⋅normalized weight, to represent edge weights.

Search for the Minimum:
    After measurement, the code analyzed the results to find the state with the lowest weight, interpreted as the shortest path.
