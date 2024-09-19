import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")
        
        # Create display
        self.display = tk.Entry(master, width=30, justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=5, pady=5)
        
        # Create buttons
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'sqrt',
            '1', '2', '3', '-', 'x^2',
            '0', '.', '=', '+', 'sin',
            '(', ')', 'pi', 'cos', 'tan',
            'c', 'G', 'h', 'm_e', 'q',  # New row for physical constants
            "$\epsilon_0$", "$\mu_0$", "R", "N_A", "k", "e"  # New row for physical constants
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            tk.Button(master, text=button, command=cmd, width=10).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 4:
                col = 0
                row += 1

        # Physical constants
        self.constants = {
            'c': 299792458,  # Speed of light in m/s
            'G': 6.67430e-11,  # Gravitational constant in m^3 kg^-1 s^-2
            'h': 6.62607015e-34,  # Planck's constant in J⋅s
            'm_e': 9.1093837015e-31,  # Electron mass in kg
            'q': 1.602176634e-19,  # Elementary charge in C
            "$\epsilon_0$": 8.8541878128e-12,  # Vacuum permittivity in F/m
            "$\mu_0$": 1.25663706212e-6,  # Vacuum permeability in N/A^2
            "R": 8.314462618,  # Gas constant in J/(mol K)
            "N_A": 6.02214076e23,  # Avogadro's number in mol^-1
            "k": 1.380649e-23,  # Boltzmann constant in J/K
            "e": 2.718281828459045,  # Euler's number
            
            


        }

    def click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'C':
            self.display.delete(0, tk.END)
        elif key == 'sqrt':
            try:
                result = math.sqrt(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'x^2':
            try:
                result = float(self.display.get()) ** 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key in ('sin', 'cos', 'tan'):
            try:
                num = float(self.display.get())
                if key == 'sin':
                    result = math.sin(math.radians(num))
                elif key == 'cos':
                    result = math.cos(math.radians(num))
                else:
                    result = math.tan(math.radians(num))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif key == 'pi':
            self.display.insert(tk.END, str(math.pi))
        elif key in self.constants:
            self.display.insert(tk.END, str(self.constants[key]))
        else:
            self.display.insert(tk.END, key)

root = tk.Tk()
my_calculator = ScientificCalculator(root)
root.mainloop()