#
# Open an existing workbook
#
import traceback

import sys
import win32com.client as win32
import os

folder = "C:\\Users\\vgorbachev\\project\\source\\parser\\xlsxtopdf\\Расчет задолженности АСВ"
file_type = 'xlsx'
out_folder = folder + "\\pdf"

os.chdir(folder)

if not os.path.exists(out_folder):
    print('Creating output folder...')
    os.makedirs(out_folder)
    print(out_folder, 'created.')
else:
    print(out_folder, 'already exists.\n')

excel = win32.DispatchEx('Excel.Application')
excel.Visible = False
for files in os.listdir("."):
    if files.endswith(".xlsx") and files[1] != "$":
        out_name = files.replace(file_type, r"pdf")
        in_file = os.path.abspath(folder + "\\" + files)
        print("From: ", in_file)
        out_file = os.path.abspath(out_folder + "\\" + out_name)
        print("To: ", out_file)
        try:
            wb = excel.Workbooks.Open(in_file, CorruptLoad=1)
            ws = wb.Worksheets["Лист1"]
            ws.PageSetup.Zoom = False
            ws.PageSetup.FitToPagesTall = 20
            ws.PageSetup.FitToPagesWide = 1
            # = print_area


            ws.Rows("%d:%d" % (1, 1)).Delete()
            xlUp = -4162
            lastrow = ws.Cells(ws.Rows.Count, "A").End(xlUp).Row + 1

            for i in range(2, lastrow):
                value = ws.Range("A" + str(i)).Value
                if value == "Задолженность по основному долгу:":
                    summ = ws.Range("F" + str(i)).Value
                    print("Задолженность по основному долгу:", summ)
                if value == "Текущая задолженность по процентам:":
                    percent = ws.Range("M" + str(i)).Value
                    print("Текущая задолженность по процентам:", percent)
                if value == "Пени на просроченный основной долг":
                    ws.Range("L" + str(lastrow)).Value = percent + summ
                    ws.Rows("%d:%d" % (i, lastrow - 1)).Delete()
                    print("Общая задолженность: ", str(percent + summ))
                    break

            ws.ExportAsFixedFormat(0, out_file)
            wb.Close(SaveChanges=False)
        except Exception as e:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
            print (''.join('[ERROR] ' + line for line in lines))  # Log it or whatever here

excel.Quit()
