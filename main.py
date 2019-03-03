import os
import sys
from PyQt5 import QtWidgets, uic

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
        self.runHere.clicked.connect(self.showResult)
        self.runCMD.clicked.connect(self.runOnCmdPrompt)
        self.clrButton.clicked.connect(self.clearData)

    # Display Result on QTextEdit
    def showResult(self):
        command = self.lineEditCmd.text()
        print("Entered Command: "+ command)
        os.system(command)

    # Run command on CMD Prompt
    def runOnCmdPrompt(self):
        command = self.lineEditCmd.text()
        os.system("start /B start cmd.exe @cmd /k %s" %command)

    # Clear all data
    def clearData(self):
        self.lineEditCmd.setText("")

run()




