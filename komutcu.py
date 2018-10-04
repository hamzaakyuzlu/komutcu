from PyQt5.QtWidgets import QDialog, QApplication
from ui_ana import Ui_dlgAna
from ui_cikti import Ui_dlgCikti
import subprocess
import sys



class CiktiWindow(QDialog, Ui_dlgCikti):
    def __init__(self, komut):
        super(CiktiWindow, self).__init__()
        self.komut = komut
        print komut
        self.setupUi(self)
        self.lblKomut.setText(komut)
        self.calistir()
        self.show()

    def calistir(self):
        try:
            
            self.textCikti.setText(subprocess.check_output(self.komut))
        except:
            self.textCikti.setText("%s calistirilamadi." % self.komut)
            
class MainWindow(QDialog, Ui_dlgAna):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.show()


    def calistir(self):
        k = CiktiWindow(self.editKomut.text())
        x = k.exec_()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    sys.exit(app.exec_())
