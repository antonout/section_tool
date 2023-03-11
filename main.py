#!/usr/bin/env python3

from math import pi

from interface import Interface


def main():
    class SectionProps(Interface):
        def __init__(self):
            super().__init__()

        def calc_rectangle(self):
            # calculate rectangle section properties and return dict
            b, h = self.parse_param_entries()[:2]
            return {
                "area": f"{b * h:.4f}",
                "moi_x": f"{b * (h ** 3) / 12:.4f}",
                "moi_y": f"{h * (b ** 3) / 12:.4f}",
                "sm_x": f"{b * (h ** 2) / 6:.4f}",
                "sm_y": f"{h * (b ** 2) / 6:.4f}",
            }

        def calc_circle(self):
            # calculate circle section properties and return dict
            r = self.parse_param_entries()[0]
            return {
                "area": f"{pi * (r ** 2):.4f}",
                "moi_x": f"{pi / 4 * (r ** 4):.4f}",
                "moi_y": f"{pi / 4 * (r ** 4):.4f}",
                "sm_x": f"{pi / 4 * (r ** 3):.4f}",
                "sm_y": f"{pi / 4 * (r ** 3):.4f}",
            }

        def calc_ring(self):
            # calculate ring section properties and return dict
            # ZeroDivisionError can be raised due to r_o
            r_o, r_i = self.parse_param_entries()[:2]

            calc_ring_output = {
                "area": f"{pi * (r_o ** 2 - r_i ** 2):.4f}",
                "moi_x": f"{pi / 4 * (r_o ** 4 - r_i ** 4):.4f}",
                "moi_y": f"{pi / 4 * (r_o ** 4 - r_i ** 4):.4f}",
            }

            try:
                calc_ring_output[
                    "sm_x"
                ] = f"{pi / (4 * r_o) * (r_o ** 4 - r_i ** 4):.4f}"
                calc_ring_output[
                    "sm_y"
                ] = f"{pi / (4 * r_o) * (r_o ** 4 - r_i ** 4):.4f}"
            except ZeroDivisionError:
                r_o = 1e-9
                calc_ring_output[
                    "sm_x"
                ] = f"{pi / (4 * r_o) * (r_o ** 4 - r_i ** 4):.4f}"
                calc_ring_output[
                    "sm_y"
                ] = f"{pi / (4 * r_o) * (r_o ** 4 - r_i ** 4):.4f}"

            return calc_ring_output

        def calc_ibeam(self):
            # calculate symmetrical i-beam section properties and return dict
            # ZeroDivisionError can be raised due to b or h
            b, h, h_w, t_w, t_f = self.parse_param_entries()

            calc_ibeam_output = {
                "area": f"{2 * (b * t_f) + (h_w * t_w):.4f}",
                "moi_x": f"{((b * h ** 3) - (b * h_w ** 3) + (t_w * h_w ** 3)) / 12:.4f}",
                "moi_y": f"{((h * b ** 3) - (h_w * b ** 3) + (h_w * t_w ** 3)) / 12:.4f}",
            }

            try:
                calc_ibeam_output[
                    "sm_x"
                ] = f"{((b * h ** 2) - (h_w ** 3 / h) * (b - t_w)) / 6:.4f}"
            except ZeroDivisionError:
                h = 1e-9
                calc_ibeam_output[
                    "sm_x"
                ] = f"{((b * h ** 2) - (h_w ** 3 / h) * (b - t_w)) / 6:.4f}"

            try:
                calc_ibeam_output[
                    "sm_y"
                ] = f"{((h * b ** 2) - h_w * (b ** 2 - (t_w ** 3 / b))) / 6:.4f}"
            except ZeroDivisionError:
                b = 1e-9
                calc_ibeam_output[
                    "sm_y"
                ] = f"{((h * b ** 2) - h_w * (b ** 2 - (t_w ** 3 / b))) / 6:.4f}"

            return calc_ibeam_output

    app = SectionProps()
    app.mainloop()


if __name__ == "__main__":
    main()
