from abc import ABC, abstractmethod
import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class Interface(ctk.CTk, ABC):
    def __init__(self):
        super().__init__()
        self.build_interface()
        self.parse_param_entries()
        self.fill_section_output_fields()
        self.auto_calculation()
        self.click_calculation()

    def build_interface(self):
        # configure window
        self.title("Section Tool")
        self.geometry("260x595")
        self.resizable(width=False, height=False)

        # configure grid layout
        self.grid_columnconfigure((0, 1), weight=0)
        self.grid_rowconfigure((0, 14), weight=0)

        # configure section choice frame (radiobutton frame)
        self.section_choice_frame = ctk.CTkFrame(self, width=230, height=106)
        self.section_choice_frame.grid(
            row=0, column=0, columnspan=2, rowspan=3, padx=10, pady=10, sticky="nsew"
        )
        self.section_choice_label = ctk.CTkLabel(
            master=self.section_choice_frame, text="CROSS SECTION SHAPE"
        )
        self.section_choice_label.grid(row=0, column=0, columnspan=2, padx=5, pady=0)

        self.choice_var = tk.IntVar()
        self.var1 = ctk.StringVar(value="0")
        self.var2 = ctk.StringVar(value="0")
        self.var3 = ctk.StringVar(value="0")
        self.var4 = ctk.StringVar(value="0")
        self.var5 = ctk.StringVar(value="0")

        def selected_param_entry():
            # reconfigure the param entries for different section choice values
            section_param_labels_entries = {
                self.section_param1_label: self.section_param1_entry,
                self.section_param2_label: self.section_param2_entry,
                self.section_param3_label: self.section_param3_entry,
                self.section_param4_label: self.section_param4_entry,
                self.section_param5_label: self.section_param5_entry,
            }

            for (label, entry) in section_param_labels_entries.items():

                if self.choice_var.get() == 0:

                    if label == self.section_param1_label:
                        label.configure(text="    Width   ")
                    elif label == self.section_param2_label:
                        label.configure(text="   Height   ")
                        entry.configure(textvariable=self.var2)
                        label.grid()
                        entry.grid()
                    else:
                        label.grid_remove()
                        entry.grid_remove()

                if self.choice_var.get() == 1:

                    if label == self.section_param1_label:
                        label.configure(text="   Radius   ")
                    else:
                        label.grid_remove()
                        entry.grid_remove()

                if self.choice_var.get() == 2:

                    if label == self.section_param1_label:
                        label.configure(text="Outer Radius")
                    elif label == self.section_param2_label:
                        label.configure(text="Inner Radius")
                        entry.configure(textvariable=self.var2)
                        label.grid()
                        entry.grid()
                    else:
                        label.grid_remove()
                        entry.grid_remove()

                if self.choice_var.get() == 3:

                    if label == self.section_param1_label:
                        label.configure(text="Flange Width")
                    elif label == self.section_param2_label:
                        label.configure(text="Total Height")
                        entry.configure(textvariable=self.var2)
                        label.grid()
                        entry.grid()
                    else:
                        label.grid()
                        if label == self.section_param3_label:
                            entry.configure(textvariable=self.var3)
                            entry.grid()
                        elif label == self.section_param4_label:
                            entry.configure(textvariable=self.var4)
                            entry.grid()
                        else:
                            entry.configure(textvariable=self.var5)
                            entry.grid()

        self.rectangle_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=105,
            text="Rectangle",
            variable=self.choice_var,
            value=0,
            command=selected_param_entry,
        )
        self.rectangle_choice_btn.grid(row=1, column=0, padx=10, pady=5)

        self.circle_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=105,
            text="Circle",
            variable=self.choice_var,
            value=1,
            command=selected_param_entry,
        )
        self.circle_choice_btn.grid(row=2, column=0, padx=10, pady=5)

        self.ring_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=105,
            text="Ring",
            variable=self.choice_var,
            value=2,
            command=selected_param_entry,
        )
        self.ring_choice_btn.grid(row=1, column=1, padx=5, pady=5)

        self.ibeam_choice_btn = ctk.CTkRadioButton(
            master=self.section_choice_frame,
            width=105,
            text="I-Beam",
            variable=self.choice_var,
            value=3,
            command=selected_param_entry,
        )
        self.ibeam_choice_btn.grid(row=2, column=1, padx=5, pady=5)

        # configure section param frame (entry frame)
        self.section_param_frame = ctk.CTkFrame(self, width=230, height=200)
        self.section_param_frame.grid(
            row=3, column=0, columnspan=2, rowspan=6, padx=10, pady=0, sticky="nsew"
        )
        self.section_param_label = ctk.CTkLabel(
            master=self.section_param_frame, text="PARAMETERS"
        )
        self.section_param_label.grid(row=3, column=0, columnspan=2, padx=5, pady=0)

        self.section_param1_label = ctk.CTkLabel(master=self.section_param_frame)
        self.section_param1_label.grid(row=4, column=0, padx=10, pady=5)
        self.section_param1_entry = ctk.CTkEntry(
            self.section_param_frame, width=122, textvariable=self.var1
        )
        self.section_param1_entry.grid(row=4, column=1, padx=5, pady=5)

        self.section_param2_label = ctk.CTkLabel(master=self.section_param_frame)
        self.section_param2_label.grid(row=5, column=0, padx=10, pady=5)
        self.section_param2_entry = ctk.CTkEntry(
            self.section_param_frame, width=122, textvariable=self.var2
        )
        self.section_param2_entry.grid(row=5, column=1, padx=5, pady=5)

        self.section_param3_label = ctk.CTkLabel(
            master=self.section_param_frame, text="Web Height"
        )
        self.section_param3_label.grid(row=6, column=0, padx=10, pady=5)
        self.section_param3_entry = ctk.CTkEntry(
            self.section_param_frame, width=122, textvariable=self.var3
        )
        self.section_param3_entry.grid(row=6, column=1, padx=5, pady=5)

        self.section_param4_label = ctk.CTkLabel(
            master=self.section_param_frame, text="Web Thick."
        )
        self.section_param4_label.grid(row=7, column=0, padx=10, pady=5)
        self.section_param4_entry = ctk.CTkEntry(
            self.section_param_frame, width=122, textvariable=self.var4
        )
        self.section_param4_entry.grid(row=7, column=1, padx=5, pady=5)

        self.section_param5_label = ctk.CTkLabel(
            master=self.section_param_frame, text="Flange Thick."
        )
        self.section_param5_label.grid(row=8, column=0, padx=10, pady=5)
        self.section_param5_entry = ctk.CTkEntry(
            self.section_param_frame, width=122, textvariable=self.var5
        )
        self.section_param5_entry.grid(row=8, column=1, padx=5, pady=5)

        selected_param_entry()

        # configure section output frame
        self.section_output_frame = ctk.CTkFrame(self, width=230, height=310)
        self.section_output_frame.grid(
            row=9, column=0, columnspan=2, rowspan=6, padx=10, pady=10, sticky="nsew"
        )
        self.section_output_label = ctk.CTkLabel(
            master=self.section_output_frame, text="PROPERTIES"
        )
        self.section_output_label.grid(row=9, column=0, columnspan=2, padx=5, pady=0)

        self.section_area_label = ctk.CTkLabel(
            master=self.section_output_frame, text="Area"
        )
        self.section_area_label.grid(row=10, column=0, padx=10, pady=7)
        self.section_area_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=172,
            height=18,
            border_width=2,
            state="disabled",
        )
        self.section_area_output.grid(row=10, column=1, padx=10, pady=5)

        self.section_moix_label = ctk.CTkLabel(
            master=self.section_output_frame, text="I_xx"
        )
        self.section_moix_label.grid(row=11, column=0, padx=10, pady=7)
        self.section_moix_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=172,
            height=18,
            border_width=2,
            state="disabled",
        )
        self.section_moix_output.grid(row=11, column=1, padx=10, pady=5)

        self.section_moiy_label = ctk.CTkLabel(
            master=self.section_output_frame, text="I_yy"
        )
        self.section_moiy_label.grid(row=12, column=0, padx=10, pady=7)
        self.section_moiy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=172,
            height=18,
            border_width=2,
            state="disabled",
        )
        self.section_moiy_output.grid(row=12, column=1, padx=10, pady=5)

        self.section_smx_label = ctk.CTkLabel(
            master=self.section_output_frame, text="Z_xx"
        )
        self.section_smx_label.grid(row=13, column=0, padx=10, pady=7)
        self.section_smx_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=172,
            height=18,
            border_width=2,
            state="disabled",
        )
        self.section_smx_output.grid(row=13, column=1, padx=10, pady=5)

        self.section_smy_label = ctk.CTkLabel(
            master=self.section_output_frame, text="Z_yy"
        )
        self.section_smy_label.grid(row=14, column=0, padx=10, pady=7)
        self.section_smy_output = ctk.CTkTextbox(
            master=self.section_output_frame,
            width=172,
            height=18,
            border_width=2,
            state="disabled",
        )
        self.section_smy_output.grid(row=14, column=1, padx=10, pady=5)

    def parse_param_entries(self):
        # parse the param entry strings, convert to floats and return as tuple
        # ValueError raise if not pure numeric values
        try:
            param1 = float(self.section_param1_entry.get())
        except ValueError:
            param1 = 1e-9

        try:
            param2 = float(self.section_param2_entry.get())
        except ValueError:
            param2 = 1e-9

        try:
            param3 = float(self.section_param3_entry.get())
        except ValueError:
            param3 = 1e-9

        try:
            param4 = float(self.section_param4_entry.get())
        except ValueError:
            param4 = 1e-9

        try:
            param5 = float(self.section_param5_entry.get())
        except ValueError:
            param5 = 1e-9

        return (param1, param2, param3, param4, param5)

    """For methods below see child class implemented in main"""

    @abstractmethod
    def calc_rectangle(self):
        pass

    @abstractmethod
    def calc_circle(self):
        pass

    @abstractmethod
    def calc_ring(self):
        pass

    @abstractmethod
    def calc_ibeam(self):
        pass

    def fill_section_output_fields(self, *args):
        # create a dict of dict with values assigned to corresponding radiobutton choice keys
        # then use the dict of dict to fill the output text fields, note the state change
        section_outputs = {
            self.section_area_output: {
                "null": self.calc_rectangle()["area"],
                "one": self.calc_circle()["area"],
                "two": self.calc_ring()["area"],
                "three": self.calc_ibeam()["area"],
            },
            self.section_moix_output: {
                "null": self.calc_rectangle()["moi_x"],
                "one": self.calc_circle()["moi_x"],
                "two": self.calc_ring()["moi_x"],
                "three": self.calc_ibeam()["moi_x"],
            },
            self.section_moiy_output: {
                "null": self.calc_rectangle()["moi_y"],
                "one": self.calc_circle()["moi_y"],
                "two": self.calc_ring()["moi_y"],
                "three": self.calc_ibeam()["moi_y"],
            },
            self.section_smx_output: {
                "null": self.calc_rectangle()["sm_x"],
                "one": self.calc_circle()["sm_x"],
                "two": self.calc_ring()["sm_x"],
                "three": self.calc_ibeam()["sm_x"],
            },
            self.section_smy_output: {
                "null": self.calc_rectangle()["sm_y"],
                "one": self.calc_circle()["sm_y"],
                "two": self.calc_ring()["sm_y"],
                "three": self.calc_ibeam()["sm_y"],
            },
        }

        for (text_field, output) in section_outputs.items():
            text_field.configure(state="normal")
            text_field.delete("0.0", "end")
            if self.choice_var.get() == 0:
                text_field.insert("0.0", output["null"])
            elif self.choice_var.get() == 1:
                text_field.insert("0.0", output["one"])
            elif self.choice_var.get() == 2:
                text_field.insert("0.0", output["two"])
            elif self.choice_var.get() == 3:
                text_field.insert("0.0", output["three"])
            text_field.configure(state="disabled")

    def auto_calculation(self):
        # update section property fields as soon as the param entry text field changes
        entry_variable_ls = (self.var1, self.var2, self.var3, self.var4, self.var5)
        for entry_variable in entry_variable_ls:
            entry_variable.trace_add("write", self.fill_section_output_fields)

    def click_calculation(self):
        # update section property fields on a mouse click, note the action during radiobutton switch
        self.bind("<Button-1>", self.fill_section_output_fields)
