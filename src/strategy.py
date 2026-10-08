class EventTradingStrategy:
    def __init__(self, symbol, threshold=0.05):
        self.symbol = symbol
        self.threshold = threshold

    def evaluate_signal(self, current_price, target_price):
        price_diff = abs(current_price - target_price) / target_price
        if price_diff >= self.threshold:
            print(f"[SIGNAL] Triggered for {self.symbol}! Diff: {price_diff:.4f}")
            return True
        return False
