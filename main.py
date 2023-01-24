from math import pi
from interface import Interface

def main():
    app = Interface()

    def calculate_properties():
        a = int(app.section_param1_entry.get())
        b = int(app.section_param2_entry.get()) if app.section_param2_entry.get().isnumeric() else 0
        
        # calculate area
        app.section_area_output.configure(state='normal')
        app.section_area_output.delete('0.0', 'end')
        if app.choice_var.get() == 0:
            app.section_area_output.insert('0.0', f'{int(a * b)}')
        else:
            app.section_area_output.insert('0.0', f'{int(int(pi) * (a ** 2))}')
        app.section_area_output.configure(state='disabled')

        # calculate moi_x
        app.section_moix_output.configure(state='normal')
        app.section_moix_output.delete('0.0', 'end')
        if app.choice_var.get() == 0:
            app.section_moix_output.insert('0.0', f'{int(b * (a ** 3) / 12)}')
        else:
            app.section_moix_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
        app.section_moix_output.configure(state='disabled')

        # calculate moi_y
        app.section_moiy_output.configure(state='normal')
        app.section_moiy_output.delete('0.0', 'end')
        if app.choice_var.get() == 0:
            app.section_moiy_output.insert('0.0', f'{int(a * (b ** 3) / 12)}')
        else:
            app.section_moiy_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
        app.section_moiy_output.configure(state='disabled')

        # calculate sm_x
        app.section_smx_output.configure(state='normal')
        app.section_smx_output.delete('0.0', 'end')
        if app.choice_var.get() == 0:
            app.section_smx_output.insert('0.0', f'{int(((b * (a ** 3) / 12) * 2) / a)}')
        else:
            app.section_smx_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')
        app.section_smx_output.configure(state='disabled')

        # calculate sm_y
        app.section_smy_output.configure(state='normal')
        app.section_smy_output.delete('0.0', 'end')
        if app.choice_var.get() == 0:
            app.section_smy_output.insert('0.0', f'{int(((a * (b ** 3) / 12) * 2) / b)}')
        else:
            app.section_smy_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')
        app.section_smy_output.configure(state='disabled')

    calculate_properties()

    app.bind('<Button-1>', lambda e: calculate_properties())
    app.mainloop()

if __name__ == '__main__':
    main()