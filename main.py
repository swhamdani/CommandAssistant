import os
import sys
from PyQt5 import QtWidgets, uic
from utils import syscmd

qtCreatorFile = "CMDAssistantUI.ui" #Enter UI file name here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


def run():
    app = QtWidgets.QApplication(sys.argv)
    window = CmdGUI()
    window.show()
    sys.exit(app.exec_())


class CmdGUI(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # PushButtons Click event
        self.runHere.clicked.connect(self.show_result)
        self.runCMD.clicked.connect(self.run_on_cmd_prompt)
        self.clrButton.clicked.connect(self.clear_data)

    # Display Result on QTextEdit
    def show_result(self):
        out = syscmd(self.ui.lineEditCmd.text())
        self.ui.textEdit.setText(out.decode("utf-8"))

    # Run command on CMD Prompt
    def run_on_cmd_prompt(self):
        command = self.lineEditCmd.text()
        os.system("start /B start cmd.exe @cmd /k %s" %command)

    # Clear all data
    def clear_data(self):
        self.lineEditCmd.setText("")
run()



