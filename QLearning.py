from collections import defaultdict


class QLearning:
    def __init__(self, learning_rate=0.5, discount_rate=0.5):
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

