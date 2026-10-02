from PyQt6.QtWidgets import (
  QMainWindow,
  QApplication,
  QWidget,
  QGridLayout,
  QVBoxLayout,
  QHBoxLayout,
  QToolBar
)

from PyQt6.QtCore import (
  Qt,
  QPropertyAnimation,
  QEasingCurve
)

from PyQt6.QtGui import (
  QFontDatabase
)

from config import configs
import sys
from math import floor

from widgets.shuffleButton import ShuffleButton

class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    config = configs()
    self.setContentsMargins(0,0,0,0)

    # Fonts
    fontId = QFontDatabase.addApplicationFont("AtkynsonMonoNerdFont-Regular.otf")
    fontFamily = QFontDatabase.applicationFontFamilies(fontId)

    # Central Widget
    central = QWidget()
    central.setStyleSheet(f"font-family: {fontFamily}")
    self.setCentralWidget(central)

    # 3 Column grid
    grid = QGridLayout(central)
    grid.setSpacing(0)
    grid.setContentsMargins(0,0,0,0)

    # -----------
    # LEFT COLUMN
    # -----------

    leftColumn = QWidget()
    leftColumn.setContentsMargins(0,0,0,0)
    leftColumn.setStyleSheet(f"background-color: {config.MainWindow.leftSection}")
    leftLayout = QVBoxLayout(leftColumn)
    

    # -------------
    # MIDDLE COLUMN
    # -------------

    middleColumn = QWidget()
    middleColumn.setContentsMargins(0,0,0,0)
    middleColumn.setStyleSheet(f"background-color: {config.MainWindow.middleSection}")

    # ------------
    # RIGHT COLUMN
    # ------------

    self.rightColumn = QWidget()
    self.rightColumn.setStyleSheet(f"background-color: {config.MainWindow.rightSection}")

    # Vertical widget to store the buttons
    self.rightLayout = QVBoxLayout(self.rightColumn)
    self.rightLayout.setContentsMargins(0,0,0,0)

    shuffleButton = ShuffleButton()
    self.rightLayout.addWidget(shuffleButton, alignment = Qt.AlignmentFlag.AlignTop)
  
    # ------
    # BOTTOM
    # ------

    self.bottomRow = QWidget()
    self.bottomRow.setStyleSheet(f"background-color: {config.MainWindow.bottomSection}")
    self.bottomRowLayout = QHBoxLayout(self.bottomRow)
    self.bottomRowLayout.setContentsMargins(0,0,0,0)

    # -----------
    # ADD LAYOUTS
    # -----------

    grid.addWidget(leftColumn, 0, 0)
    grid.addWidget(middleColumn, 0, 1)
    grid.addWidget(self.rightColumn, 0, 2)
    grid.addWidget(self.bottomRow, 1,0,1,3)

    grid.setColumnStretch(0,0)
    grid.setColumnStretch(1,1)
    grid.setColumnStretch(2,0)

    grid.setRowStretch(0,11)
    grid.setRowStretch(1,1)

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = MainWindow()
  window.show()
  app.exec()