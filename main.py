import PySimpleGUI as sg    
import parseTaskList
import time
import datetime

sg.theme('DarkBlue2')

comboClass = ['機能設計', '実装', 'その他', '休憩']

nameCombo = parseTaskList.readNameList()
kindCombo = parseTaskList.readKindList()

tab1_layout =  [
    [sg.Multiline('', size=(30,18))],
]    

tab2_layout = [
    [sg.Text('タスク追加', size=(10,2))],    
    [sg.Text('分類',    size=(10,4)), sg.Combo(comboClass, key='taskClass',        size=(20,4))],
    [sg.Text('種類',    size=(10,2)), sg.Combo(kindCombo,  key='taskKind',                     size=(20,4))],
    [sg.Text('タスク名', size=(10,2)), sg.Combo(nameCombo,  key='taskName',                 size=(20,4))],
    [sg.Text('', size=(30,2), key='time')],
    [sg.Button('追加'), sg.Button('終了'), sg.Button('データ'), sg.Button('更新')]
]

layout = [
    [sg.TabGroup([[sg.Tab('Tab 1', tab2_layout), sg.Tab('Tab 2', tab1_layout)]])]
]    

window = sg.Window('ストップウォッチ', layout, default_element_size=(12, 1), no_titlebar=True, keep_on_top=True, grab_anywhere=True)
timer_running, counter = True, 0
start, timer = False, 0

while True:    
    event, values = window.read(timeout=10)

    # × もしくは Quitで終了
    if event in (None, 'Quit'):
        break

    elif event == '追加':
        start = True
        starttime = datetime.datetime.now()
        parseTaskList.start(starttime)
    
    elif event == '終了':
        parseTaskList.end(values['taskClass'],
                          values['taskKind'],
                          values['taskName'],
                          starttime)
        start = False
        counter = 0

    elif event == "add":
        print(values['_OUTPUT_'])

    elif event == "データ":
        parseTaskList.openData()
    
    elif event == "更新":
        nameCombo = parseTaskList.readNameList()
        kindCombo = parseTaskList.readKindList()
        window['taskKind'].update(values=kindCombo)
        window['taskName'].update(values=nameCombo)

    if start:
        timer = (datetime.datetime.now() - starttime).total_seconds()
        window['time'].update('{:02d}:{:02d}:{:02d}'.format(round(timer // 60) // 60, round(timer // 60) % 60, round(timer % 60)))