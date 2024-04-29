import tabula
import pdfplumber
import pandas as pd
import matplotlib as mpl

mud_report = {
    "Time": '',
    'Sample_Location': '',
    'Mud_type': '',
    'Mud_company': '',
    'Flowline_Temperature': '',
    'Depth': '',
    'Mud_Weight': '',
    'Funnel_Vis': '',
    '3_rpm': '',
    '6_rpm': '',
    '100_rpm': '',
    '200_rpm': '',
    '300_rpm': '',
    '600_rpm': '',
    'Plastic_Vis': '',
    'Plastic_Temp': '',
    'Yield_Point': '',
    'Gel_10sec': '',
    'Gel_10min': '',
    'Gel_30min': '',
    'Filtrate_hthp': '',
    'Cake_hthp': '',
    'Hthp_temp': '',
    'Filtrate_api': '',
    'Cake_api': '',
    'Solids': '',
    'Oil': '',
    'Water': '',
    'Oil_ratio': '',
    'Water_ratio': '',
    'Solids_corr': '',
    'Chlorides': '',
    'Calcium': '',
    'WPS': '',
    'Sand': '',
    'MBT': '',
    'PH': '',
    'Mud_alk': '',
    'Mud_filt': '',
    'E_lime': '',
    'E_stability': '',
    'AGS': '',
    'LGS': '',
    'HGS': '',
    'Engineer': '',
    'Comment': '',
    'n': '',
    'k': ''
}
class MudReport:
    def __init__(self):
        self.Time = ''
        self.Sample_Location = ''
        self.Mud_type = ''
        self.Mud_company = ''
        self.Flowline_Temperature = ''
        self.Depth = ''
        self.Mud_Weight = ''
        self.Funnel_Vis = ''
        self._3_rpm = ''
        self._6_rpm = ''
        self._100_rpm = ''
        self._200_rpm = ''
        self._300_rpm = ''
        self._600_rpm = ''
        self.Plastic_Vis = ''
        self.Plastic_Temp = ''
        self.Yield_Point = ''
        self.Gel_10sec = ''
        self.Gel_10min = ''
        self.Gel_30min = ''
        self.Filtrate_hthp = ''
        self.Cake_hthp = ''
        self.Hthp_temp = ''
        self.Filtrate_api = ''
        self.Cake_api = ''
        self.Solids = ''
        self.Oil = ''
        self.Water = ''
        self.Oil_ratio = ''
        self.Water_ratio = ''
        self.Solids_corr = ''
        self.Chlorides = ''
        self.Calcium = ''
        self.WPS = ''
        self.Sand = ''
        self.MBT = ''
        self.PH = ''
        self.Mud_alk = ''
        self.Mud_filt = ''
        self.E_lime = ''
        self.E_stability = ''
        self.AGS = ''
        self.LGS = ''
        self.HGS = ''
        self.Engineer = ''
        self.Comment = ''
        self.n = ''
        self.k = ''

    def print_variables(self):
        # Using vars() function
        # variables = vars(self)
        # for var in variables:
        #     print(var, '=', variables[var])

        # Or iterating over attributes directly
        for attr, value in self.__dict__.items():
            print(attr, '=', value)

def get_data(arr, data_name):
    for i in range(len(arr)):
        if data_name in arr[i]:
            try:
                return float(arr[i + 1])
            except (IndexError, ValueError):
                return None
    return None

pdf = pdfplumber.open('041924-17.pdf')

# tables = tabula.read_pdf('040824-12PM.pdf')
print(pdf.pages[0])
page = pdf.pages[0]
extracted_data = page.extract_table()
a = 0

array_data = []
mud_rep = MudReport()

for data in extracted_data:
    a = a + 1
    filtered_list = list(filter(None, data))
    array_data.append(filtered_list)
    print(filtered_list)
    if 'Sample Location' in filtered_list:
        mud_rep.Sample_Location = filtered_list[1]
    if 'Flowline Temperature °F' in filtered_list:
        mud_rep.Flowline_Temperature = filtered_list[1].replace(' °F', '')
    if 'Mud Weight (ppg)' in filtered_list:
        mud_rep.Mud_Weight = filtered_list[1]

    funnel_vis = get_data(filtered_list, 'Funnel Vis (sec/qt)')
    if funnel_vis is not None:
        mud_rep.Funnel_Vis = funnel_vis


    if '600 rpm' in filtered_list:
        mud_rep._600_rpm = filtered_list[1]
    if '300 rpm' in filtered_list:
        mud_rep._300_rpm = filtered_list[1]
    if '200 rpm' in filtered_list:
        mud_rep._200_rpm = filtered_list[1]
    if '100 rpm' in filtered_list:
        mud_rep._100_rpm = filtered_list[1]
    if '6 rpm' in filtered_list:
        mud_rep._6_rpm = filtered_list[1]
    if '3 rpm' in filtered_list:
        mud_rep._3_rpm = filtered_list[1]

    plastic_vis = get_data(filtered_list, 'Plastic Viscosity')
    if plastic_vis is not None:
        mud_rep.Plastic_Vis = plastic_vis

    yield_point = get_data(filtered_list, 'Yield Point')
    if yield_point is not None:
        mud_rep.Yield_Point = yield_point

    if 'Gel Strength (lb/100 ft²) 10 sec / 10 min' in filtered_list:
        mud_rep.Gel_10sec = filtered_list[1][0]
        mud_rep.Gel_10min = filtered_list[1][-1]

    if 'Gel Strength (lb/100 ft2) 30 min' in filtered_list:
        mud_rep.Gel_30min = filtered_list[1]

    hthp_filt = get_data(filtered_list, 'HTHP Filtrate (cm/30 min)')
    if hthp_filt is not None:
        mud_rep.Filtrate_hthp = hthp_filt

    if 'HTHP Cake Thickness (32nds)' in filtered_list:
        mud_rep.Cake_hthp = filtered_list[1]

    if 'Retort Solids Content' in filtered_list:
        mud_rep.Solids = filtered_list[1].replace('%', '')

    if 'Corrected Solids (vol%)' in filtered_list:
        mud_rep.Solids_corr = filtered_list[1].replace('%', '')

    if 'Retort Oil Content' in filtered_list:
        mud_rep.Oil = filtered_list[1].replace('%', '')

    if 'Retort Water Content' in filtered_list:
        mud_rep.Water = filtered_list[1].replace('%', '')

    if 'O/W Ratio' in filtered_list:
        parts = filtered_list[1].split(':')
        oil = parts[0] if parts[0] else 0
        water = parts[1] if parts[1] else 0
        mud_rep.Oil_ratio = oil
        mud_rep.Water_ratio = water

    if 'Whole Mud Chlorides (mg/L)' in filtered_list:
        mud_rep.Chlorides = filtered_list[1].replace(',', '')

    if 'Water Phase Salinity (ppm)' in filtered_list:
        mud_rep.WPS = filtered_list[1].replace(',', '')

    if 'Whole Mud Alkalinity, Pom' in filtered_list:
        mud_rep.Mud_alk = filtered_list[1]

    if 'Excess Lime (lb/bbl)' in filtered_list:
        mud_rep.E_lime = filtered_list[1].replace(' ppb', '')

    if 'Electrical Stability (volts)' in filtered_list:
        mud_rep.E_stability = filtered_list[1].replace(' v', '')

    if 'Average Specific Gravity of Solids' in filtered_list:
        mud_rep.AGS = filtered_list[1]

    if 'Percent Low Gravity Solids' in filtered_list:
        mud_rep.LGS = filtered_list[1].replace('%', '')

    if 'Percent Barite' in filtered_list:
        mud_rep.HGS = filtered_list[1].replace('%', '')

    if 'Sample Taken By' in filtered_list:
        mud_rep.Engineer = filtered_list[1]


mud_rep.print_variables()
df = pd.DataFrame(array_data)
df.to_excel('output.xlsx')




