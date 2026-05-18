"""
01_run_benchmark.py — Run a benchmark programmatically

Shows how to import and run a single benchmark from qedcbench
after installing with: pip install qedcbench

Prerequisites:
    pip install qedcbench qiskit qiskit-aer
"""

from qedcbench.hidden_shift import hs_benchmark

# Run Hidden Shift benchmark: 2-8 qubits, 3 circuits per width, 100 shots
hs_benchmark.run(
    min_qubits=2,
    max_qubits=8,
    max_circuits=3,
    num_shots=100,
    backend_id="qasm_simulator",
)
