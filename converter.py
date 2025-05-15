from PyQt5 import QtWidgets, QtCore
import sys

class UnitConverter(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Конвертер единиц")
        self.setGeometry(100, 100, 300, 150)

        layout = QtWidgets.QVBoxLayout()

        # Выбор категории
        self.category = QtWidgets.QComboBox()
        self.category.addItems(["Длина", "Масса"])
        self.category.currentTextChanged.connect(self.update_units)
        layout.addWidget(self.category)

        # Ввод значения
        self.input_field = QtWidgets.QLineEdit()
        self.input_field.setPlaceholderText("Введите значение")
        layout.addWidget(self.input_field)

        # Выбор единиц
        unit_layout = QtWidgets.QHBoxLayout()
        self.from_unit = QtWidgets.QComboBox()
        self.to_unit = QtWidgets.QComboBox()
        unit_layout.addWidget(self.from_unit)
        unit_layout.addWidget(self.to_unit)
        layout.addLayout(unit_layout)

        # Кнопка конвертации
        self.convert_button = QtWidgets.QPushButton("Конвертировать")
        self.convert_button.clicked.connect(self.convert)
        layout.addWidget(self.convert_button)

        # Результат
        self.result_label = QtWidgets.QLabel("")
        layout.addWidget(self.result_label)

        self.setLayout(layout)
        self.update_units("Длина")

    def update_units(self, category):
        if category == "Длина":
            units = ["м", "км", "см"]
        else:
            units = ["г", "кг", "т"]
        self.from_unit.clear()
        self.to_unit.clear()
        self.from_unit.addItems(units)
        self.to_unit.addItems(units)

    def convert(self):
        try:
            value = float(self.input_field.text())
        except ValueError:
            self.result_label.setText("Ошибка: введите число")
            return

        category = self.category.currentText()
        from_u = self.from_unit.currentText()
        to_u = self.to_unit.currentText()

        factor = self.get_conversion_factor(category, from_u, to_u)
        result = value * factor
        self.result_label.setText(f"{result:.4f} {to_u}")

    def get_conversion_factor(self, category, from_unit, to_unit):
        if category == "Длина":
            units = {"м": 1, "км": 1000, "см": 0.01}
        else:
            units = {"г": 1, "кило": 1000, "т": 1000000}
        return units[from_unit] / units[to_unit]

app = QtWidgets.QApplication(sys.argv)
window = UnitConverter()
window.show()
sys.exit(app.exec_())
