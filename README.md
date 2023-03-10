# Section Tool for stress analysis

A tiny simple program dedicated to aid stress analysts to calculate the geometrical properties of a number of cross-section shapes. 

The following shapes are implemented:
- rectangle;
- circle;
- ring;
- i-beam.

The program outputs the following properties:
- area;
- area moment of inertia relative to the major (I_xx) and minor (I_yy) axis;
- section modulus (at extreme fiber) relative to the major (Z_xx) and minor (Z_yy) axis.

**DOCUMENTATION:**
Refer to *Documentation.pdf* in the repository for formulae justification and application examples.

**NOTES:** 
1. Empty and zero geometry parameters are treated as 1e-9 for ZeroDivisionError avoidance. It is users responsibility to check the inputs to avoid inadequate results.
2. Current version does not limit the use of negative values.

# Installation
Clone the repository:  `git clone https://github.com/antonout/section_tool.git`

Please refer to *CustomTkinter* packaging documentation for executable file instructions: `https://github.com/TomSchimansky/CustomTkinter/wiki/Packaging`