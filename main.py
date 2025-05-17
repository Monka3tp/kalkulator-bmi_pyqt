import sys

from PyQt6.QtWidgets import QApplication, QDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.obliczButton.clicked.connect(self.oblicz)
        self.show()
    def oblicz(self):
        waga = self.ui.wagaBox.value()
        wzrost = self.ui.wzrostBox.value()
        bmi = waga/(wzrost/100)**2
        wynik_bmi = round(float(bmi), 2)

        self.ui.wynikLabel.setText(str(wynik_bmi))

        if float(bmi) < 18.5:
            self.ui.czyPrawdilowaLabel.setStyleSheet("background-color: blue")
            self.ui.czyPrawdilowaLabel.setText("Niedowaga")
        if float(bmi) >= 18.5 and float(bmi) < 25:
            self.ui.czyPrawdilowaLabel.setStyleSheet("background-color: green")
            self.ui.czyPrawdilowaLabel.setText("Waga prawidłowa")
        if float(bmi) >= 25 and float(bmi) < 30:
            self.ui.czyPrawdilowaLabel.setStyleSheet("background-color: orange")
            self.ui.czyPrawdilowaLabel.setText("Nadwaga")
        if float(bmi) >= 30:
            self.ui.czyPrawdilowaLabel.setStyleSheet("background-color: red")
            self.ui.czyPrawdilowaLabel.setText("Otyłość")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    sys.exit(app.exec())