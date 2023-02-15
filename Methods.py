class Tasks:
    def __init__(self):
        self.estimates = []
        self.probabilities = []

    def add_task(self, estimate, probability):
        self.estimates.append(estimate)
        self.probabilities.append(probability)

    def completion_methods(self):
        self.max = 0
        self.min = 0
        minimum = 0
        maximum = 0
        total_time = 0
        count = 0
        for i in range(len(self.estimates)):
            if self.estimates[i] * self.probabilities[i] / 100 > maximum:
                maximum = self.estimates[i] * self.probabilities[i] / 100
            if self.estimates[i] * self.probabilities[i] / 100 < minimum:
                minimum = self.estimates[i] * self.probabilities[i] / 100
            total_time += self.estimates[i] * self.probabilities[i] / 100
            if count == 0:
                minimum = self.estimates[i] * self.probabilities[i] / 100
            count += 1
        self.min = minimum
        self.max = maximum
        return total_time


plan = Tasks()

making_plan = True
while making_plan:
    estimate = int(input("Enter the estimated completion of the task in days: "))
    probability = int(input("Enter the task probability(%): "))
    plan.add_task(estimate, probability)
    more_tasks = input("Add another task? (y/n): ")
    if more_tasks.lower() != "y":
        making_plan = False

average_time = plan.completion_methods()
print("The maximum number of days is ", plan.max)
print("The minimum number of days is", plan.min)
print("The average time to finish the plan is", average_time, "days.")
