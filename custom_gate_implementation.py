#Creating a custom gate
from qiskit import QuantumCircuit
#Making a custom gate
gatesource = QuantumCircuit(2)#initializing two quibits
gatesource.x(0)
gatesource.cx(0,1)
gatesource.x(0)
xcnotxgate = gatesource.to_gate()
gatesource.draw(output="mpl")#drawing the custom gate

#Using the custom gate
customgateqc = QuantumCircuit(2)#initializing two quibits
customgateqc.append(xcnotxgate,[0,1])
customgateqc.draw(output="mpl")#drawing the circuit with custom gate
customgateqc.decompose().draw(output="mpl")#drawing a decomposed version of the gate

