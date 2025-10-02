# src/neuron.py
import csv

class Neuron:
    def __init__(self, threshold=3, weight=1.0, learning_rate=0.1, decay=0.01):
        self.threshold = threshold
        self.potential = 0
        self.weight = weight
        self.learning_rate = learning_rate
        self.decay = decay
        self.firings = []
        self.potentials = []
        self.weights = []

    def receive_input(self, input_signal):
        self.potential += input_signal * self.weight
        fired = 0
        if self.potential >= self.threshold:
            fired = 1
            self.potential = 0
            self.weight += self.learning_rate * input_signal
        else:
            self.weight -= self.decay
        # Store logs
        self.firings.append(fired)
        self.potentials.append(self.potential)
        self.weights.append(self.weight)
        return fired

    def save_log(self, filename="data/logs/phase1_log.csv", stimulus=None):
        with open(filename,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['t','input','potential','weight','fired'])
            for t, val in enumerate(self.firings):
                in_val = stimulus[t] if stimulus else 0
                writer.writerow([t, in_val, self.potentials[t], self.weights[t], self.firings[t]])
