import bisect
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from collections import defaultdict

# Task Class
class Task:
    def __init__(self, title, task_type, priority, start_time, end_time, deadline):
        self.title = title
        self.task_type = task_type  # 'personal' or 'academic'
        self.priority = priority  # Higher number = higher priority
        self.start_time = start_time
        self.end_time = end_time
        self.deadline = deadline

# Sorting Functions
def merge_sort(tasks):
    if len(tasks) > 1:
        mid = len(tasks) // 2
        left_half = tasks[:mid]
        right_half = tasks[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].priority > right_half[j].priority:
                tasks[k] = left_half[i]
                i += 1
            else:
                tasks[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            tasks[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            tasks[k] = right_half[j]
            j += 1
            k += 1

# Binary Search Function
def binary_search_task(tasks, target_deadline):
    index = bisect.bisect_left([task.deadline for task in tasks], target_deadline)
    if index < len(tasks) and tasks[index].deadline == target_deadline:
        return tasks[index]
    return None

# Task Density Analysis
def task_density_analysis(tasks, interval=timedelta(hours=1)):
    density = defaultdict(int)
    for task in tasks:
        time_slot = task.start_time
        while time_slot < task.end_time:
            density[time_slot] += 1
            time_slot += interval
    return density

# Gantt Chart Display
def display_gantt_chart(tasks):
    fig, ax = plt.subplots(figsize=(10, 6))

    for idx, task in enumerate(tasks):
        color = 'tab:blue' if task.task_type == 'academic' else 'tab:green'
        start_num = mdates.date2num(task.start_time)
        duration = (task.end_time - task.start_time).total_seconds() / 3600  # duration in hours

        ax.broken_barh([(start_num, duration)], 
                       (idx * 10, 9), facecolors=(color,))

    ax.set_yticks([i * 10 + 5 for i in range(len(tasks))])
    ax.set_yticklabels([task.title for task in tasks])
    
    # Setting a locator and formatter for clearer x-axis labels
    ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

    plt.gcf().autofmt_xdate(rotation=45)  # Rotate labels for readability
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()

# Function to find the last non-conflicting task
def find_last_non_conflicting(tasks, i):
    for j in range(i - 1, -1, -1):
        if tasks[j].end_time <= tasks[i].start_time:
            return j
    return -1

# Scheduler Class
class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def optimize_schedule(self):
        # Sort tasks by their end time
        self.sort_tasks_by_priority()  # Ensure tasks are sorted by priority first
        self.tasks.sort(key=lambda task: task.end_time)  # Sort by end time

        n = len(self.tasks)
        dp = [0] * n

        # Fill the dp array
        dp[0] = self.tasks[0].priority  # Base case

        for i in range(1, n):
            # Include the current task
            include_priority = self.tasks[i].priority
            last_non_conflict = find_last_non_conflicting(self.tasks, i)
            if last_non_conflict != -1:
                include_priority += dp[last_non_conflict]

            # Exclude the current task
            exclude_priority = dp[i - 1]

            # Take the maximum of including or excluding the current task
            dp[i] = max(include_priority, exclude_priority)

        # The last entry in dp array will be the maximum priority obtainable
        print(f"Maximum priority obtainable: {dp[-1]}")

    def sort_tasks_by_priority(self):
        merge_sort(self.tasks)

    def find_task_by_deadline(self, target_deadline):
        return binary_search_task(self.tasks, target_deadline)

    def analyze_task_density(self, interval=timedelta(hours=1)):
        return task_density_analysis(self.tasks, interval)

    def display_gantt_chart(self):
        display_gantt_chart(self.tasks)

# Example Usage
if __name__ == "__main__":
    # Define some example tasks
    task1 = Task("Study Session", "academic", 5, datetime(2024, 11, 1, 9), datetime(2024, 11, 1, 11), datetime(2024, 11, 1, 10))
    task2 = Task("Gym", "personal", 3, datetime(2024, 11, 1, 12), datetime(2024, 11, 1, 13), datetime(2024, 11, 1, 12))
    task3 = Task("Project Meeting", "academic", 4, datetime(2024, 11, 1, 15), datetime(2024, 11, 1, 16), datetime(2024, 11, 1, 15))
    
    # Initialize scheduler
    scheduler = Scheduler()
    scheduler.add_task(task1)
    scheduler.add_task(task2)
    scheduler.add_task(task3)

    # Sort tasks by priority
    scheduler.sort_tasks_by_priority()
    
    # Display Gantt Chart
    scheduler.display_gantt_chart()

    # Find task by a specific deadline
    deadline = datetime(2024, 11, 1, 10)
    task = scheduler.find_task_by_deadline(deadline)
    print(f"Task found by deadline: {task.title if task else 'No task found'}")

    # Analyze task density
    density = scheduler.analyze_task_density(interval=timedelta(hours=1))
    print("Task Density Analysis:")
    for time_slot, count in density.items():
        print(f"{time_slot}: {count} tasks")

