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
        max_reward = max(keys, key=lambda action: self.values[state][action])
        return max_reward
        # Returns the best action based off current QValues information.
        # defaultdict calls a factory function to supply missing values.
        # Thus, if we call values[state][action] for some unestablished
        # combination, it will give us a max_reward of 0.

    def update_table(self, state, action, reward, next_state):
        # Get current value, next value, and next q state
        cur_val = self.values[state][action]
        next_val = list(self.values[next_state].values())
        next_q = max(next_val) if next_val else 0

        # Bellman equation to update Q Table values
        self.values[state][action] = cur_val + self.learning_rate * \
                                     (reward + self.discount_rate * next_q - cur_val)

