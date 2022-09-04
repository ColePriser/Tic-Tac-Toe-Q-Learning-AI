from collections import defaultdict


class QLearning:
    def __init__(self, learning_rate=0.5, discount_rate=0.5):
        # How much weight we give new value
        self.learning_rate = learning_rate

        # Discount factor
        self.discount_rate = discount_rate

        # Table of Q values
        self.values = defaultdict(lambda: defaultdict(lambda: 0.0))

    def best_action(self, state):
        keys = list(self.values[state].keys())
        if not keys:
            return None
        max_reward = max(keys, key=lambda x: self.values[state][x])
        return max_reward

