# src/experiments/exp_basic.py
import matplotlib.pyplot as plt
from src.neuron import Neuron

# Parameters
stimulus = [0,1,1,0,1,1,0,1]
neuron = Neuron(threshold=3, learning_rate=0.1, decay=0.01)

# Simulation
for s in stimulus:
    neuron.receive_input(s)

# Save logs
neuron.save_log(filename="data/logs/phase1_log.csv", stimulus=stimulus)

# Plotting
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.plot(neuron.potentials, label="Potential")
plt.axhline(neuron.threshold, linestyle='--', color='r', label="Threshold")
plt.title("Neuron Potential Over Time")
plt.legend()

plt.subplot(1,2,2)
plt.plot(neuron.weights, label="Synaptic Weight", color='purple')
plt.title("Synaptic Weight Adaptation")
plt.legend()
plt.tight_layout()
plt.show()
