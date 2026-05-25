from qiskit import QuantumCircuit
qc = QuantumCircuit(3)
for i in range(3): qc.h(i)
for e in [(0,1), (1,2)]:
    qc.cx(e, e); qc.rz(1.0, e); qc.cx(e, e)
for i in range(3): qc.rx(0.6, i)
print("【Day 8 QAOA 邏輯閘總操作數】:", len(qc.data))
