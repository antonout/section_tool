import tkinter as tk
from math import pi

import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Interface(ctk.CTk):
    def __init__(self, calculation='auto'):
        super().__init__()
        self.build_interface()
        self.parse_param_entries()
        self.calc_rectangle()
        self.calc_circle()
        self.fill_section_output_fields()
        
        self.calculation = calculation
        if self.calculation == 'auto':
            self.auto_calculation()
        elif self.calculation == 'click': 
            self.click_calculation()

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
        self.var1 = ctk.StringVar(value='0')
        self.var2 = ctk.StringVar(value='0')

        def selected_param_entry():
            # reconfigure the param entries for different section choice values
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
            border_width=2,
            state='disabled'
        )
        self.section_area_output.grid(row=1, column=2, padx=5, pady=5, sticky='n')

        self.section_moix_label = ctk.CTkLabel(master=self.section_output_frame, text='I_xx = ')
        self.section_moix_label.grid(row=2, column=1, padx=5, pady=7, sticky='n')
        self.section_moix_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2,
            state='disabled'
        )
        self.section_moix_output.grid(row=2, column=2, padx=5, pady=5, sticky='n')

        self.section_moiy_label = ctk.CTkLabel(master=self.section_output_frame, text='I_yy = ')
        self.section_moiy_label.grid(row=3, column=1, padx=5, pady=7, sticky='n')
        self.section_moiy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2,
            state='disabled'
        )
        self.section_moiy_output.grid(row=3, column=2, padx=5, pady=5, sticky='n')

        self.section_smx_label = ctk.CTkLabel(master=self.section_output_frame, text='Z_xx = ')
        self.section_smx_label.grid(row=4, column=1, padx=5, pady=7, sticky='n')
        self.section_smx_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2,
            state='disabled'
        )
        self.section_smx_output.grid(row=4, column=2, padx=5, pady=5, sticky='n')

        self.section_smy_label = ctk.CTkLabel(master=self.section_output_frame, text='Z_yy = ')
        self.section_smy_label.grid(row=5, column=1, padx=5, pady=7, sticky='n')
        self.section_smy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=122,
            height=18,
            border_width=2,
            state='disabled'
        )
        self.section_smy_output.grid(row=5, column=2, padx=5, pady=5, sticky='n')
       
    def parse_param_entries(self):
        # parse the param etnry strings, convert to floats and return as tuple
        try:
            param1 = float(self.section_param1_entry.get())
        except ValueError:
            param1 = 1e-9

        try:
            param2 = float(self.section_param2_entry.get())
        except ValueError:
            param2 = 1e-9
        
        return (param1, param2)

    def calc_rectangle(self):
        # calculate rectangle section properties and return dict
        b_x, h_y = self.parse_param_entries()
        return {
            'area': f'{b_x * h_y:.4f}', 
            'moi_x': f'{b_x * (h_y ** 3) / 12:.4f}', 
            'moi_y': f'{h_y * (b_x ** 3) / 12:.4f}', 
            'sm_x': f'{b_x * (h_y ** 2) / 6:.4f}', 
            'sm_y': f'{h_y * (b_x ** 2) / 6:.4f}'
        }

    def calc_circle(self):
        # calculate circle section properties and return dict
        r = self.parse_param_entries()[0]
        return {
            'area': f'{pi * (r ** 2):.4f}',
            'moi_x': f'{pi * (r ** 4) / 4:.4f}', 
            'moi_y': f'{pi * (r ** 4) / 4:.4f}', 
            'sm_x': f'{pi * (r ** 3) / 2:.4f}', 
            'sm_y': f'{pi * (r ** 3) / 2:.4f}'
        }

    def fill_section_output_fields(self, *args):
        # create a dict of dict with values assigned to corresponding radiobutton choice keys
        # then use the dict of dict to fill the output text fields, note the state change
        widget_params = {
            self.section_area_output: {
                'null': self.calc_rectangle()['area'],
                'one': self.calc_circle()['area']  
            },
            self.section_moix_output: {
                'null': self.calc_rectangle()['moi_x'],
                'one': self.calc_circle()['moi_x']
            }, 
            self.section_moiy_output: {
                'null': self.calc_rectangle()['moi_y'],
                'one': self.calc_circle()['moi_y']
            },
            self.section_smx_output: {
                'null': self.calc_rectangle()['sm_x'],
                'one': self.calc_circle()['sm_x']
            },
            self.section_smy_output: {
                'null': self.calc_rectangle()['sm_y'],
                'one': self.calc_circle()['sm_y']
            }
        }

        for (text_field, output) in widget_params.items():
            text_field.configure(state='normal')
            text_field.delete('0.0', 'end')
            if self.choice_var.get() == 0:
                text_field.insert('0.0', output['null'])
            elif self.choice_var.get() == 1:
                text_field.insert('0.0', output['one'])
            text_field.configure(state='disabled')
    
    def auto_calculation(self):
        # update section property fields as soon as the param entry text field changes
        self.var1.trace_add('write', self.fill_section_output_fields)
        self.var2.trace_add('write', self.fill_section_output_fields)
    
    def click_calculation(self):
        # update section property fields on a mouse click
        self.bind('<Button-1>', self.fill_section_output_fields)
