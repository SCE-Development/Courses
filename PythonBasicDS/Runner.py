import subprocess
from sys import platform
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import time as Time

def on_select_mainfile_clicked():
    file_name = filedialog.askopenfilename(initialdir="./")
    if file_name:
        mainfile.set(file_name)

def on_select_inputdir_clicked():
    dir_name = filedialog.askdirectory(initialdir="./")
    if dir_name:
        inputdir.set(dir_name)

def on_select_outputdir_clicked():
    dir_name = filedialog.askdirectory(initialdir="./")
    if dir_name:
        outputdir.set(dir_name)

def on_run_mainfile():
    global result
    if not mainfile.get():
        error.set("Main File Not selected")
        return
    if not inputdir.get():
        error.set("Input Directory Not selected")
        return
    if not outputdir.get():
        error.set("Output Directory Not selected")
        return
    if timelimit.get() <= 0:
        error.set("Time Limit Invalid")
        return
    if not timelimit.get():
        error.set("Time Limit Not set")
        return
    error.set("")
    result.set("")
    time.set(0)

    dirpath, dirs, files = next(os.walk(inputdir.get()))
    current = 0
    maxtime = 0
    passing = True
    for file in files:
        current += 1
        result.set(str(current)+" / "+str(len(files)))
        print(file)
        start = Time.time()
        temp = subprocess.Popen(
            [cmd_head, mainfile.get()],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        try:
            with open(inputdir.get()+"/"+file, "r") as f:
                data = "".join(f.readlines()).encode("utf-8")
            outs, errs = temp.communicate(
                input=data,
                timeout=timelimit.get()
            )
            print(outs,errs)
            if errs:
                error.set("RE")
                passing = False
                break
            with open(outputdir.get()+"/"+file.replace("input","output"), "r") as f:
                ans = "".join(f.readlines())
            # print([outs, ans.encode("utf-8")])
            # print([outs.decode("utf-8"), ans])
            if outs.decode("utf-8").replace("\r","") != ans:
                error.set("WA")
                passing = False
        except subprocess.TimeoutExpired:
            temp.kill()
            outs, errs = temp.communicate()
            print(outs, errs)
            error.set("TLE")
            passing = False
        end = Time.time()
        maxtime = max(maxtime, end - start)
        if not passing:
            break
    if len(files):
        if passing:
            result.set("AC")
        time.set(maxtime * 1000)
    else:
        error.set("No Files Selected")

if platform.startswith("darwin"):
    cmd_head = "python3"
else:
    cmd_head = "python"

# Main Setup
root = Tk()
root.title("Python Code Runner for Competitive Programming")
root.minsize(width=500, height=500)
root.geometry("+200+200")
root.columnconfigure(0, weight=2)
rowweight = [3,2,1,2]
for i in range(4):
    root.rowconfigure(i, weight=rowweight[i])

# Frame For Files Selection
# Frame Settings
frame_files = ttk.LabelFrame(root, text="Files")
frame_files.grid(row=0, column=0, sticky=(E,W,N,S))
frame_files.columnconfigure(0, weight=1)
frame_files.columnconfigure(1, weight=4)
frame_files.columnconfigure(2, weight=1)
for i in range(3):
    frame_files.rowconfigure(i, weight=1)
# Row 1
row = 0
col = 0
Label_mainfile = ttk.Label(frame_files, padding=1, text="Main File :")
Label_mainfile.grid(row=row, column=col)
col += 1
mainfile = StringVar()
Entry_mainfile = ttk.Entry(frame_files, textvariable=mainfile)
Entry_mainfile.grid(row=row, column=col, sticky=(W,E))
col += 1
Button_mainfile = ttk.Button(frame_files, text="Open File", command=on_select_mainfile_clicked)
Button_mainfile.grid(row=row, column=col)
# Row 2
row += 1
col = 0
Label_inputdir = ttk.Label(frame_files, padding=1, text="Input Directory :")
Label_inputdir.grid(row=row, column=col)
col += 1
inputdir = StringVar()
Entry_inputdir = ttk.Entry(frame_files, textvariable=inputdir)
Entry_inputdir.grid(row=row, column=col, sticky=(W,E))
col += 1
Button_inputdir = ttk.Button(frame_files, text="Open Directory", command=on_select_inputdir_clicked)
Button_inputdir.grid(row=row, column=col)
# Row 3+
row += 1
col = 0
Label_outputdir = ttk.Label(frame_files, padding=1, text="Output Directory :")
Label_outputdir.grid(row=row, column=col)
col += 1
outputdir = StringVar()
Entry_outputdir = ttk.Entry(frame_files, textvariable=outputdir)
Entry_outputdir.grid(row=row, column=col, sticky=(W,E))
col += 1
Button_outputdir = ttk.Button(frame_files, text="Open Directory", command=on_select_outputdir_clicked)
Button_outputdir.grid(row=row, column=col)

# Frame For Options
# Frame Settings
frame_options = ttk.LabelFrame(root, text="Options")
frame_options.grid(row=1, column=0, sticky=(E,W,S,N))
for i in range(4):
    frame_options.columnconfigure(i, weight=1)
# Row 1
row = 0
col = 0
Label_timelimit = ttk.Label(frame_options, padding=1, text="Time Limit:")
Label_timelimit.grid(row=row, column=col)
col += 1
timelimit = IntVar()
timelimit.set(1)
Entry_timelimit = ttk.Entry(frame_options, textvariable=timelimit)
Entry_timelimit.grid(row=row, column=col)

# Run! Button
Button_run = ttk.Button(root, text="Run!", command=on_run_mainfile)
Button_run.grid(row=2, column=0)

# Frame Result
# Frame Settings
frame_result = ttk.LabelFrame(root, text="Result")
frame_result.grid(row=3, column=0, sticky=(N,S,W,E))
colweight = [1,2,1]
for i in range(3):
    frame_result.columnconfigure(i, weight=colweight[i])
# Row 1
row = 0
col = 0
Label_result = ttk.Label(frame_result, padding=1, text="Result:")
Label_result.grid(row=row, column=col, sticky=(W))
col += 1
Label_errormsg = ttk.Label(frame_result, padding=1, text="Error:")
Label_errormsg.grid(row=row, column=col, sticky=(W))
col += 1
Label_time = ttk.Label(frame_result, padding=1, text="Time (ms):")
Label_time.grid(row=row, column=col, sticky=(W))
# Row 2
row += 1
col = 0
result = StringVar()
Result_result = ttk.Label(frame_result, padding=1, textvariable=result)
Result_result.grid(row=row, column=col, sticky=(W))
col += 1
error = StringVar()
Result_errormsg = ttk.Label(frame_result, padding=1, textvariable=error)
Result_errormsg.grid(row=row, column=col, sticky=(W))
col += 1
time = IntVar()
Result_time = ttk.Label(frame_result, padding=1, textvariable=time)
Result_time.grid(row=row, column=col, sticky=(W))

root.mainloop()

# temp = subprocess.run(
#     [cmd_head, mainfile.get()],
#     shell=False,
#     check=False,
#     timeout=timelimit.get(),
#     input=data,
#     # input="hello".encode("utf-8"),
#     stdout=subprocess.PIPE)