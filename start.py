from ProgramController import ProgramController
import ProgramWindow

# print(SkeletonDatabase.get_persons(2))
# print(SkeletonDatabase.get_persons(3))

controller = ProgramController('Dark')
root, app = ProgramWindow.show_window(controller)
# print("app: " + type(app))
