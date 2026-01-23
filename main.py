import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from users.form_users import FormUsers
from projects.form_projects import FormProjects
from tags.form_tags import FormTags
from tasks.form_tasks import FormTasks
from sub_tasks.form_sub_tasks import FormSubTasks
from task_tags.form_task_tags import FormTaskTags


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.resize(1200, 800)
        self.setWindowTitle("Task Tracker System")
        self.setWindowIcon(QIcon("icon.svg"))

        self.page_users = FormUsers()
        self.stack.addWidget(self.page_users)

        self.page_projects = FormProjects()
        self.stack.addWidget(self.page_projects)

        self.page_tags = FormTags()
        self.stack.addWidget(self.page_tags)

        self.page_tasks = FormTasks()
        self.stack.addWidget(self.page_tasks)

        self.page_sub_tasks = FormSubTasks()
        self.stack.addWidget(self.page_sub_tasks)

        self.page_task_tags = FormTaskTags()
        self.stack.addWidget(self.page_task_tags)

        self.connect_sidebar(self.page_users)
        self.connect_sidebar(self.page_projects)
        self.connect_sidebar(self.page_tags)
        self.connect_sidebar(self.page_tasks)
        self.connect_sidebar(self.page_sub_tasks)
        self.connect_sidebar(self.page_task_tags)
        self.stack.setCurrentIndex(0)

    def connect_sidebar(self, page_obj):
        nav_buttons = {
            "pushButton": 0,
            "pushButton_4": 1,
            "pushButton_5": 2,
            "pushButton_2": 3,
            "pushButton_6": 4,
            "pushButton_3": 5,
        }

        for btn_name, idx in nav_buttons.items():
            if hasattr(page_obj, btn_name):
                btn = getattr(page_obj, btn_name)
                try:
                    btn.clicked.disconnect()
                except:
                    pass

                btn.clicked.connect(lambda _, x=idx: self.stack.setCurrentIndex(x))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
