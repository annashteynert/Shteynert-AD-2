class Responsibilities:
    def __init__(self):
        self.plans = []
        self.load_plans()

    def add_plan(self, plan):
        self.plans.append(plan)
        self.save_plans()

    def remove_plan(self, plan):
        if plan in self.plans:
            self.plans.remove(plan)
            self.save_plans()

    def display_plans(self):
        for plan in self.plans:
            print(plan)

    def save_plans(self):
        with open('responsibilities.txt', 'w') as f:
            for plan in self.plans:
                f.write(plan + '\n')

    def load_plans(self):
        try:
            with open('responsibilities.txt', 'r') as f:
                self.plans = [line.strip() for line in f]
        except FileNotFoundError:
            pass
my_responsibilities = Responsibilities()
