
import PySimpleGUI as psg


t1 = psg.Input(visible=False, enable_events=True, key='-T1-', font=('Arial Bold', 10), expand_x=True)
t2 = psg.Input(visible=False, enable_events=True, key='-T2-', font=('Arial Bold', 10), expand_x=True)
t3 = psg.Multiline("", enable_events=True, key='-INPUT-', expand_x=True, expand_y=True, justification='left')
t4 = psg.Button("Clear",key='-clr-')
t5 = psg.Button("About",key='-about-')

layout = [ 
            [t1, psg.FilesBrowse(button_text='Open'), t2, psg.FileSaveAs(),t4 , t5],
            [t3],
            ]

psg.theme("Default 1")
window = psg.Window('Text Editor', layout, size=(715, 580))

while True:
 event, values = window.read()
 if event == '-T1-':
     file = open(t1.get())
     txt = file.read()
     window['-INPUT-'].Update(value=txt)
 if event == '-T2-':
     file = open(t2.get(), "w")
     file.write(t3.get())
     file.close()
 if event == '-clr-':
     txt = " "
     window['-INPUT-'].Update(txt)
 if event == '-about-':
     psg.popup_scrolled('''\tThe Text Editor By Raghul V\n\n This Application was Devoloped To View The \n Text Based Document On The Local System \n\n Python Version : 3.10 Stable \n Application Version : 1.0 '''
    , title=" About ",font=("Arial Bold", 10), size=(50,10))

 if event == psg.WIN_CLOSED or event == 'Exit':
         break

window.close()

