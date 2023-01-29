import tkinter as tk
from math import pi

import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.build_interface()
        self.bind('<Button-1>', self.calculate_properties)
        self.calculate_properties()

    def build_interface(self):
        # configure window
        self.title('Section Tool')
        self.geometry('410x260')

        # configure grid layout
        self.grid_columnconfigure((0, 5), weight=0)
        self.grid_rowconfigure((0, 5), weight=0)

        # configure section choice frame (radiobutton frame)
        self.section_choice_frame = ctk.CTkFrame(self, width=200, height=200)
        self.section_choice_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')
        self.section_choice_label = ctk.CTkLabel(master=self.section_choice_frame, text='Cross section shape')
        self.section_choice_label.grid(row=0, column=0, columnspan=2, padx=5, pady=0, sticky='')

        self.choice_var = tk.IntVar()
        self.var1 = ctk.StringVar(value='1')
        self.var2 = ctk.StringVar(value='1')

        def selected_param_entry():
            if self.choice_var.get() == 0:
                self.section_param1_label.configure(text='Width =')
                self.section_param2_entry.configure(textvariable=self.var2, state='normal')
                self.section_param2_label.grid()
                self.section_param2_entry.grid()
            elif self.choice_var.get() == 1:
                self.section_param1_label.configure(text='Radius =')
                self.section_param2_label.grid_remove()
                self.section_param2_entry.grid_remove()

        self.rectangle_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=190,
            text='Rectangle',
            variable=self.choice_var,
            value=0,
            command=selected_param_entry
        )
        self.rectangle_choice_btn.grid(row=1, column=0, padx=5, pady=0, sticky='n')
        self.circle_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=190,
            text='Circle',
            variable=self.choice_var,
            value=1,
            command=selected_param_entry
        )
        self.circle_choice_btn.grid(row=2, column=0, padx=5, pady=5, sticky='n')

        # configure section param frame (entry frame)
        self.section_param_frame = ctk.CTkFrame(self, width=200, height=200)
        self.section_param_frame.grid(row=3, column=0, padx=10, pady=0, sticky='n')
        self.section_param_label = ctk.CTkLabel(master=self.section_param_frame, text='Parameters')
        self.section_param_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0, sticky='')

        self.section_param1_label = ctk.CTkLabel(master=self.section_param_frame)
        self.section_param1_label.grid(row=4, column=0, padx=5, pady=5, sticky='')
        self.section_param1_entry = ctk.CTkEntry(
            self.section_param_frame,
            width=122,
            textvariable=self.var1
        )
        self.section_param1_entry.grid(row=4, column=1, padx=5, pady=5, sticky='')
        self.section_param2_label = ctk.CTkLabel(master=self.section_param_frame, text='Height =')
        self.section_param2_label.grid(row=5, column=0, padx=5, pady=5, sticky='')
        self.section_param2_entry = ctk.CTkEntry(
            self.section_param_frame,
            width=122,
            textvariable=self.var2
        )
        self.section_param2_entry.grid(row=5, column=1, padx=5, pady=5, sticky='')

        selected_param_entry()

        # configure section output frame
        self.section_output_frame = ctk.CTkFrame(self, width=250)
        self.section_output_frame.grid(row=0, column=1, columnspan=2, rowspan=6, padx=0, pady=10, sticky='n')
        self.section_output_label = ctk.CTkLabel(master=self.section_output_frame, text='Properties')
        self.section_output_label.grid(row=0, column=1, columnspan=2, padx=5, pady=0, sticky='n')

        self.section_area_label = ctk.CTkLabel(master=self.section_output_frame, text='Area = ')
        self.section_area_label.grid(row=1, column=1, padx=5, pady=7, sticky='n')
        self.section_area_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2
        )
        self.section_area_output.grid(row=1, column=2, padx=5, pady=5, sticky='n')

        self.section_moix_label = ctk.CTkLabel(master=self.section_output_frame, text='I_xx = ')
        self.section_moix_label.grid(row=2, column=1, padx=5, pady=7, sticky='n')
        self.section_moix_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2
        )
        self.section_moix_output.grid(row=2, column=2, padx=5, pady=5, sticky='n')

        self.section_moiy_label = ctk.CTkLabel(master=self.section_output_frame, text='I_yy = ')
        self.section_moiy_label.grid(row=3, column=1, padx=5, pady=7, sticky='n')
        self.section_moiy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2
        )
        self.section_moiy_output.grid(row=3, column=2, padx=5, pady=5, sticky='n')

        self.section_smx_label = ctk.CTkLabel(master=self.section_output_frame, text='Z_xx = ')
        self.section_smx_label.grid(row=4, column=1, padx=5, pady=7, sticky='n')
        self.section_smx_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2
        )
        self.section_smx_output.grid(row=4, column=2, padx=5, pady=5, sticky='n')

        self.section_smy_label = ctk.CTkLabel(master=self.section_output_frame, text='Z_yy = ')
        self.section_smy_label.grid(row=5, column=1, padx=5, pady=7, sticky='n')
        self.section_smy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2
        )
        self.section_smy_output.grid(row=5, column=2, padx=5, pady=5, sticky='n')

        # Update calculations as soon as the text field changes
        self.var1.trace_add('write', self.calculate_properties)
        self.var2.trace_add('write', self.calculate_properties)

    def calculate_properties(self, *args, **kwargs):
        try:
            a = int(self.section_param1_entry.get())
        except ValueError:
            a = 0

        try:
            b = int(self.section_param2_entry.get())
        except ValueError:
            b = 0

        if a == 0:
            a = 1e-6  # trick to prevent ZeroDivisionError down the road
        if b == 0:
            b = 1e-6  # trick to prevent ZeroDivisionError down the road

        # configure a state of output fields and clear the contents
        self.section_area_output.configure(state='normal')
        self.section_moix_output.configure(state='normal')
        self.section_moiy_output.configure(state='normal')
        self.section_smx_output.configure(state='normal')
        self.section_smy_output.configure(state='normal')

        self.section_area_output.delete('0.0', 'end')
        self.section_moix_output.delete('0.0', 'end')
        self.section_moiy_output.delete('0.0', 'end')
        self.section_smx_output.delete('0.0', 'end')
        self.section_smy_output.delete('0.0', 'end')

        # calculate properties and fill the textbox content
        if self.choice_var.get() == 0:
            self.section_area_output.insert('0.0', f'{int(a * b)}')
            self.section_moix_output.insert('0.0', f'{int(b * (a ** 3) / 12)}')
            self.section_moiy_output.insert('0.0', f'{int(a * (b ** 3) / 12)}')
            self.section_smx_output.insert('0.0', f'{int(((b * (a ** 3) / 12) * 2) / a)}')
            self.section_smy_output.insert('0.0', f'{int(((a * (b ** 3) / 12) * 2) / b)}')
        else:
            self.section_area_output.insert('0.0', f'{int(int(pi) * (a ** 2))}')
            self.section_moix_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
            self.section_moiy_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
            self.section_smx_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')
            self.section_smy_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')

        # change the state to disabled
        self.section_area_output.configure(state='disabled')
        self.section_moix_output.configure(state='disabled')
        self.section_moiy_output.configure(state='disabled')
        self.section_smx_output.configure(state='disabled')
        self.section_smy_output.configure(state='disabled')
