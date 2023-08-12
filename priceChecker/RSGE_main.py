#####################################################
# RSGE_main.py                                      #
# Event loop of the application                     #
#####################################################

import PySimpleGUI as sg

#RSGE files
import RSGE_functions as RSGE_f
import RSGE_lookup as RSGE_look
import RSGE_geSummary as RSGE_sum
import RSGE_item

lookupWindow = RSGE_look.LookupWindow()
summaryWindow = RSGE_sum.GeWindow()

root_window = [[sg.Text(text = RSGE_f.lastUpdate())], [lookupWindow.lookup_frame, summaryWindow.summary_frame]]

window = sg.Window("RuneScape Grand Exchange Checker", root_window)
window.Finalize()

# Event loop
while(1):
    event, values = window.read(timeout = 120)
    if event == sg.WIN_CLOSED:
    	break
    lookupWindow.update_widgets(window, event, values)
    summaryWindow.update_widgets(window, event, values)

    # if event != '__TIMEOUT__':
    #     print(event)
    #     print(values)

window.close()   