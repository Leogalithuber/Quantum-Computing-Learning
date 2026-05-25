import qiskit
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

# 建立 2 個量子位元的電路
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

state = Statevector.from_instruction(qc)
print("【MIT 實驗室報告：Day 2 貝爾態狀態向量矩陣】")
print(state.data)
