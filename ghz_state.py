import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# 動態建構 3 位元 GHZ 巨型糾纏電路
n_qubits = 3
qc = QuantumCircuit(n_qubits)
qc.h(0)
for i in range(n_qubits - 1):
    qc.cx(i, i + 1)

statevector = Statevector.from_instruction(qc)
print("【MIT 8.371 報告：Day 4 GHZ 狀態向量巨型矩陣】")
print(statevector.data)
