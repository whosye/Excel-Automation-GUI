
from Check import Start
import tkinter as tk 
from tkinter import filedialog
import os 
import re, sys
def inpu1_fn():
    global input1
    input1 = filedialog.askopenfilenames()
    
    pattern = r'[^/]+$'

    label =""
    for name in input1:
        match = re.search(pattern, name)
        if match:
            result = match.group(0)
            label += f"{result}\n"


    label_input1.configure(text= label)
        
def inpu2_fn():
    global input2
    input2 = filedialog.askopenfilenames()
    pattern = r'[^/]+$'
    
    label =""
    for name in input2:
        match = re.search(pattern, name)
        if match:
            result = match.group(0)
            label += f"{result}\n"
    label_input2.configure(text= label)


def Compare():
    global input1, input2
    import shutil
    os.makedirs(exist_ok=True, name="Report")
    if len(os.listdir(os.path.abspath('Report'))) == 0 or len(os.listdir(os.path.abspath('Report'))) == 1 and os.listdir(os.path.abspath('Report'))[0]== "dependencies":
        name = f"report_{1}.html"
        
    else:
        temp = []
        
        for report in (os.listdir(os.path.abspath('Report'))):
            breakBool = False
            temp_num = ""
            for j in range(len(report)):
                if report[j] =="_":
                    
                    for num in range(j+1, len(report)):
                        if report[num] ==".":
                            breakBool = True
                            break
                        else:
                            temp_num += str(report[num])
                if breakBool:
                    break
            try:
                temp.append(int(temp_num))
            except:
                continue
        maxNum  = max(temp)+1
        name    = f"report_{maxNum}.html"
  
    try:
        print(os.path.abspath('dist'))
        current_path = sys.argv[0]
        current_directory = os.path.dirname(current_path)
        path_to_dependencies = f"{current_directory}\\Compare_3000_build\\dependencies"
        path_to_report = f"{current_directory}\\Report\\dependencies"
        shutil.copytree(path_to_dependencies,path_to_report)
            
    except:
        
        pass
    
    if len(input1) != len(input2):
        label_info['bg'] = 'orange'
        label_info['text']= 'number of OLD excels \n doest not match \n number of NEW'
    else:
        try:
            first = False
            for i, names in enumerate(zip(input1,input2)):
                try:
                    name    = f"report_{maxNum + i}.html"
                except:
                    first = True
                if first: 
                    name    = f"report_{1 + i}.html"
                html_report_path = os.path.join(os.path.abspath("Report"),name)
                name1, name2 = names[0], names[1]
                Start(input1=name1, input2= name2, html_report_path=html_report_path)
                label_info['bg'] = 'green'
                label_info['text']= 'Succes'
        except:
            label_info['bg'] = 'red'
            label_info['text']= 'Error'
        

window = tk.Tk()
window.geometry('800x300')
window.title('CompareTool 3000')
window.configure(bg='gray')

window2 = tk.Frame(master=window, borderwidth=5,  bg="lightblue",relief='raised',border=2 )
choose_input1_button = tk.Button(master=window2,text='Choose first excel', command=inpu1_fn)
choose_input2_button = tk.Button(master=window2,text='Choose second excel', command=inpu2_fn)
label_input1         = tk.Label(master=window2,text="placeholder1")
label_input2         = tk.Label(master=window2,text="placeholder2")
label_input1_show    = tk.Label(master=window2, text="Excel Sheet 1 =>")
label_input2_show    = tk.Label(master=window2, text="<= Excel Sheet 2")
Compare_button       = tk.Button(master=window2, text="Compare", command=Compare)
label_OLD            = tk.Label(master=window2, text="OLD VERSION", bg='red')
label_NEW            = tk.Label(master=window2, text="NEW VERSION",bg='red')
label_info  = tk.Label(master=window2, text="Result")
window2.place(anchor='center', relx=0.5, rely=0.5)
label_info.grid(row= 3, column=4,  padx=10,pady=10)
choose_input1_button.grid(row=1, column=2, padx=10,pady=10)
label_input1.grid(row= 2, column=2,  padx=10,pady=10, sticky="nsew")
label_input1_show.grid(row= 2, column=1,  padx=10,pady=10)
Compare_button.grid(row= 2, column=4,  padx=10,pady=10)
choose_input2_button.grid(row= 1, column=6, padx=10,pady=10)
label_input2.grid(row= 2, column=6, padx=10,pady=10,sticky="nsew")
label_input2_show.grid(row= 2, column=7,  padx=10,pady=10)
label_OLD.grid(row=0, column=2, padx=10,pady=10)
label_NEW.grid(row=0, column=6, padx=10,pady=10)
window2.grid_rowconfigure(2, weight=1) 
window2.grid_rowconfigure(2, weight=1) 
"""
# 

label_input2.grid(row= 1, column=3,  pady=10)
label_input1_show.grid(row= 1, column=0,  pady=10)


"""
tk.mainloop()