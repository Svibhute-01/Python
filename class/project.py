class Project:
    def __init__(self):
        self.project_name = input("Enter Project Name: ")
        self.project_id = input("Enter Project ID: ")

    def show_project(self):
        print("Project Name:", self.project_name)
        print("Project ID:", self.project_id)


class Module(Project):
    def __init__(self):
        super().__init__()
        self.module_name = input("Enter Module Name: ")

    def show_module(self):
        print("Module Name:", self.module_name)


class Task(Module):
    def __init__(self):
        super().__init__()
        self.task_name = input("Enter Task Name: ")
        self.task_id = input("Enter Task ID: ")

    def show_task(self):
        self.show_project()     
        self.show_module()      
        print("Task Name:", self.task_name)
        print("Task ID:", self.task_id)



task_obj = Task()
print("\n--- Task Details ---")
task_obj.show_task()
