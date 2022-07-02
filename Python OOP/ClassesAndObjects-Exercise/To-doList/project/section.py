from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        task_details = f"Name: {new_task.name} - Due Date: {new_task.due_date}"
        return f"Task {task_details} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        removed_tasks = 0
        for idx in range(len(self.tasks)):
            task = self.tasks[idx]
            if task.completed:
                self.tasks.pop(idx)
                removed_tasks += 1
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        info = f"Section {self.name}:\n"
        for task in self.tasks:
            info += f"Name: {task.name} - Due Date: {task.due_date}\n"
        return info
