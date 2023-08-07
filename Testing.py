# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:12:26 2023

@author: Riya
"""
import pandas as pd
import phishing_new
import FE_forTesting
#Core Packages
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog
#from keras.models import load_model


def verify_url():
    testing=[]
    inputUrl = str(entry.get('1.0', tk.END))
    
    #Connection
    
    testing.append(FE_forTesting.Feature_Extraction(inputUrl))
    feature_names = ['URL_length', 'depth', 'redirection_pos', 'has_https','host_periods_count', 'host_term_count', 'host_name_length', 'has_@',
                      'has_valid_TLD', 'have_IP', 'short_URL']
    
    
    X_validate = pd.DataFrame(testing, columns= feature_names)
    
    # Multilayer Perceptrons model
    from sklearn.neural_network import MLPClassifier
    
    #predicting the target value from the model for the samples
    y_validate_mlp = phishing_new.mlp.predict(X_validate)
    
    
    result = '\nResult:{}'.format(y_validate_mlp)
    tab1_display.insert(tk.END, result)
    



# Structure and Layout
window = Tk()
window.title("Phishing Detection")
window.geometry("700x400")
window.config(background='black')

# # TAB LAYOUT
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')
#
tab1 = ttk.Frame(tab_control)

# # ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')

label1 = Label(tab1, text='Phished URL Detection',font=("times new roman",15,"bold"), padx=5, pady=5)
label1.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')
#tkinter end

# MAIN NLP TAB
l1 = Label(tab1, text="Enter URL")
l1.grid(row=1, column=0)

entry = Text(tab1, height=10)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

#Clear entry widget
def clear_text():
   entry.delete('1.0', END)


def clear_display_result():
    tab1_display.delete('1.0', END)



# BUTTONS
button1 = Button(tab1, text="Reset", command=clear_text, width=12, bg='#03A9F4', fg='#fff')
button1.grid(row=4, column=0, padx=10, pady=10)

button2 = Button(tab1, text="Verify", command=verify_url, width=12, bg='#00008b', fg='#fac')
button2.grid(row=4, column=1, padx=10, pady=10)

button3 = Button(tab1, text="Clear Result", command=clear_display_result, width=12, bg='#03A9F4', fg='#fff')
button3.grid(row=5, column=0, padx=10, pady=10)






# Display Screen For Result
tab1_display = Text(tab1)
tab1_display.grid(row=7, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
    
    





