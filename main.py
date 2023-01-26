#!/usr/bin/env python3

from interface import Interface


def main():
    app = Interface()
<<<<<<< HEAD
=======

    def calculate_properties():
        a = float(app.section_param1_entry.get())
        b = float(app.section_param2_entry.get()) if app.section_param2_entry.get().isnumeric() else 0
        ls = [app.section_area_output, app.section_moix_output, app.section_moiy_output, app.section_smx_output, app.section_smy_output]

        # (1) configure a normal state of output fields and clear the contents 
        # (2) calculate properties and fill the textbox content
        # (3) change the state to disabled         
        for each in ls:
            each.configure(state='normal')
            each.delete('0.0', 'end')
            if app.choice_var.get() == 0:
                match each:
                    case app.section_area_output: each.insert('0.0', f'{a * b:.4f}')
                    case app.section_moix_output: each.insert('0.0', f'{b * (a ** 3) / 12:.4f}')
                    case app.section_moiy_output: each.insert('0.0', f'{a * (b ** 3) / 12:.4f}')
                    case app.section_smx_output: each.insert('0.0', f'{b * (a ** 2) / 6:.4f}')
                    case app.section_smy_output: each.insert('0.0', f'{a * (b ** 2) / 6:.4f}') 
            else:
                match each:
                    case app.section_area_output: each.insert('0.0', f'{pi * (a ** 2):.4f}')
                    case app.section_moix_output | app.section_moiy_output: each.insert('0.0', f'{pi * (a ** 4) / 4:.4f}')
                    case app.section_smx_output | app.section_smy_output: each.insert('0.0', f'{pi * (a ** 3) / 2:.4f}')
            each.configure(state='disabled')

    calculate_properties()

    app.bind('<Button-1>', lambda _: calculate_properties())
>>>>>>> 183ae8f (introduced for loops)
    app.mainloop()


if __name__ == '__main__':
    main()
