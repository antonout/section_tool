#!/usr/bin/env python3

from interface import Interface


def main():
    app = Interface()
<<<<<<< HEAD
=======

    def calculate_properties():
        a = int(app.section_param1_entry.get())
        b = int(app.section_param2_entry.get()) if app.section_param2_entry.get().isnumeric() else 0

        # configure a state of output fields and clear the contents    
        ls = [app.section_area_output, app.section_moix_output, app.section_moiy_output, app.section_smx_output, app.section_smy_output]
        
        for each in ls:
            each.configure(state='normal')
            each.delete('0.0', 'end')
        
        # calculate properties and fill the textbox content
        if app.choice_var.get() == 0:
            app.section_area_output.insert('0.0', f'{int(a * b)}')
            app.section_moix_output.insert('0.0', f'{int(b * (a ** 3) / 12)}')
            app.section_moiy_output.insert('0.0', f'{int(a * (b ** 3) / 12)}')
            app.section_smx_output.insert('0.0', f'{int(((b * (a ** 3) / 12) * 2) / a)}')
            app.section_smy_output.insert('0.0', f'{int(((a * (b ** 3) / 12) * 2) / b)}')
        else:
            app.section_area_output.insert('0.0', f'{int(int(pi) * (a ** 2))}')
            app.section_moix_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
            app.section_moiy_output.insert('0.0', f'{int(int(pi) * (a ** 4) / 4)}')
            app.section_smx_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')
            app.section_smy_output.insert('0.0', f'{int(((int(pi) * (a ** 4) / 4) * 2) / a)}')
            
        # change the state to disabled
        for each in ls:
            each.configure(state='disabled')

    calculate_properties()

    app.bind('<Button-1>', lambda _: calculate_properties())
>>>>>>> 183ae8f (introduced for loops)
    app.mainloop()


if __name__ == '__main__':
    main()
