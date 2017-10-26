# Imports for pyQuil (ignore for now)
import numpy as np
from pyquil.quil import Program
import pyquil.api as api
quantum_simulator = api.SyncConnection()

# pyQuil is based around operations (or gates) so we will start with the most
# basic one: the identity operation, called I. I takes one argument, the index
# of the qubit that it should be applied to.
from pyquil.gates import I

# Make a quantum program that allocates one qubit (qubit #0) and does nothing to it
p = Program(I(0))

# Quantum states are called wavefunctions for historical reasons.
# We can run this basic program on our connection to the simulator.
# This call will return the state of our qubits after we run program p.
# This api call returns a tuple, but we'll ignore the second value for now.
wavefunc, _ = quantum_simulator.wavefunction(p)
# wavefunc is a Wavefunction object that stores a quantum state as a list of amplitudes
alpha, beta = wavefunc
print "Our qubit is in the state alpha={} and beta={}".format(alpha, beta)
print "The probability of measuring the qubit in outcome 0 is {}".format(abs(alpha)**2)
print "The probability of measuring the qubit in outcome 1 is {}".format(abs(beta)**2)

# We can import the qubit "flip" operation, called X, and see what it does.
# We will learn more about this operation in the next section.
from pyquil.gates import X
p = Program(X(0))

wavefunc, _ = quantum_simulator.wavefunction(p)
alpha, beta = wavefunc
print "Our qubit is in the state alpha={} and beta={}".format(alpha, beta)
print "The probability of measuring the qubit in outcome 0 is {}".format(abs(alpha)**2)
print "The probability of measuring the qubit in outcome 1 is {}".format(abs(beta)**2)

# Multiple qubits also produce the expected scaling of the state.
p = Program(I(0), I(1))
wvf, _ = quantum_simulator.wavefunction(p)
print "The quantum state is of dimension:", len(wvf.amplitudes)

p = Program(I(0), I(1), I(2), I(3))
wvf, _ = quantum_simulator.wavefunction(p)
print "The quantum state is of dimension:", len(wvf.amplitudes)

p = Program()
for x in range(10):
    p.inst(I(x))
wvf, _ = quantum_simulator.wavefunction(p)
print "The quantum state is of dimension:", len(wvf.amplitudes)
