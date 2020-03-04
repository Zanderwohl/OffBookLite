from ProgramController import ProgramController
import ProgramWindow
import SkeletonDatabase

# print(SkeletonDatabase.get_persons(2))
# print(SkeletonDatabase.get_persons(3))

controller = ProgramController()
root, app = ProgramWindow.show_window(controller)
# print("app: " + type(app))
