class ViewerState:
    def __init__(self):
        self.popularity = 0
        self.carl_popularity = 0
        self.donut_popularity = 4
        self.timeline = []
        self.poll_active = False

    def change(self, amount, reason, target="party"):
        self.popularity = max(0, self.popularity + amount)
        if target == "donut":
            self.donut_popularity = max(0, self.donut_popularity + amount)
        elif target == "carl":
            self.carl_popularity = max(0, self.carl_popularity + amount)
        self.timeline.append(f"{amount:+} popularity: {reason}")

    def sponsor_ready(self):
        return self.popularity >= 10
