import sys
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMessageBox, QTextEdit
import pdfplumber
import re


class MudReport:
    def __init__(self):
        self.variables = {
            'Sample Location': 'Sample_Location',
            'Flowline Temperature °F': 'Flowline_Temperature',
            'Mud Weight (ppg)': 'Mud_Weight',
            'Funnel Vis (sec/qt)': 'Funnel_Vis',
            '600 rpm': '_600_rpm',
            '300 rpm': '_300_rpm',
            '200 rpm': '_200_rpm',
            '100 rpm': '_100_rpm',
            '6 rpm': '_6_rpm',
            '3 rpm': '_3_rpm',
            'Plastic Viscosity': 'Plastic_Vis',
            'Yield Point': 'Yield_Point',
            'Gel Strength (lb/100 ft²) 10 sec / 10 min': ['Gel_10sec', 'Gel_10min'],
            'Gel Strength (lb/100 ft2) 30 min': 'Gel_30min',
            'HTHP Filtrate (cm/30 min)': 'Filtrate_hthp',
            'HTHP Cake Thickness (32nds)': 'Cake_hthp',
            'Retort Solids Content': 'Solids',
            'Corrected Solids (vol%)': 'Solids_corr',
            'Retort Oil Content': 'Oil',
            'Retort Water Content': 'Water',
            'O/W Ratio': ['Oil_ratio', 'Water_ratio'],
            'Whole Mud Chlorides (mg/L)': 'Chlorides',
            'Water Phase Salinity (ppm)': 'WPS',
            'Whole Mud Alkalinity, Pom': 'Mud_alk',
            'Excess Lime (lb/bbl)': 'E_lime',
            'Electrical Stability (volts)': 'E_stability',
            'Average Specific Gravity of Solids': 'AGS',
            'Percent Low Gravity Solids': 'LGS',
            'Percent Barite': 'HGS',
            'Sample Taken By': 'Engineer'
        }
        self.variables_values = {}

    def update_variable(self, variable, value):
        if isinstance(variable, list):
            for var, val in zip(variable, value):
                self.variables_values[var] = val
        else:
            self.variables_values[variable] = value

    def print_variables(self):
        for attr, value in self.variables_values.items():
            print(attr, '=', value)

    def get_all_data(self):
        return self.variables_values

    @staticmethod
    def get_data(arr, data_name):
        for i in range(len(arr)):
            if data_name in arr[i]:
                try:
                    # Extracting numeric values using regular expression
                    value = re.findall(r'[+-]?\d*\.\d+|\d+', arr[i + 1])
                    return float(value[0]) if value else None
                except (IndexError, ValueError):
                    return None
        return None

    def process_pdf(self, pdf_path):
        pdf = pdfplumber.open(pdf_path)
        page = pdf.pages[0]
        extracted_data = page.extract_table()

        for data in extracted_data:
            filtered_list = list(filter(None, data))
            for keyword, attribute in self.variables.items():
                if keyword in filtered_list:
                    value = filtered_list[filtered_list.index(keyword) + 1]
                    if isinstance(attribute, list):
                        values = value.split('/')
                        self.update_variable(attribute, values)
                    else:
                        self.update_variable(attribute, value)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF File Uploader")
        self.setGeometry(100, 100, 600, 400)

        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(50, 50, 500, 200)

        self.upload_button = QPushButton("Upload PDF File", self)
        self.upload_button.setGeometry(100, 270, 200, 50)
        self.upload_button.clicked.connect(self.upload_file)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(300, 270, 200, 50)
        self.exit_button.clicked.connect(self.exit_app)

    def upload_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select PDF File", "", "PDF Files (*.pdf)")
        if file_name:
            result = self.process_pdf(file_name)
            self.text_edit.append(result)

    def process_pdf(self, file_name):
        try:
            # Here you can integrate your algorithm to process the PDF file
            # For example:
            # processed_data = your_pdf_processing_algorithm(file_name)
            # return "Processing complete. Result: {}".format(processed_data)
            mud_rep = MudReport()
            mud_rep.process_pdf(file_name)
            result = mud_rep.get_all_data()
            return "Processing complete. Result: {}".format(result)
        except Exception as e:
            return f"Error processing PDF file: {e}"

    def exit_app(self):
        QApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

