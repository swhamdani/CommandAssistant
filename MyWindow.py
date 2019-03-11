import sys
import os
from PyQt5.QtWidgets import QDialog, QApplication
from GUI import GuiDialog
from PyQt5.QtCore import pyqtSlot
from utils import syscmd


class AppWindow(QDialog):

    #Run Command on app run / GUI load
    def commands(self):
        out = syscmd("net start")
        self.ui.textEdit.setText(out.decode("utf-8"))

    @pyqtSlot()
    def on_click(self):
        if self.ui.lineEditCmd.text():
            out=syscmd(self.ui.lineEditCmd.text())
        self.ui.textEdit.setText(out.decode("utf-8"))

    # Display Result on QTextEdit
    def show_result(self):
        if self.ui.lineEditCmd.text():
            out = syscmd(self.ui.lineEditCmd.text())
        self.ui.textEdit.setText(out.decode("utf-8"))

    # Run command on CMD Prompt
    def run_on_cmd_prompt(self):
        if self.ui.lineEditCmd.text():
            command = self.ui.lineEditCmd.text()
        os.system("start /B start cmd.exe @cmd /k %s" % command)

    # Clear all data
    def clear_data(self):
        self.ui.lineEditCmd.setText("")
        self.ui.textEdit.setText("")

    def __init__(self): #this is constructor and execution starting point#
        super().__init__()
        self.ui = GuiDialog()
        self.ui.setup_gui(self)
        self.show()

        #To execute method on app run
        self.commands()

        # PushButtons Click event
        self.ui.runHere.clicked.connect(self.on_click)
        self.ui.runCMD.clicked.connect(self.run_on_cmd_prompt)
        self.ui.clrButton.clicked.connect(self.clear_data)


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())