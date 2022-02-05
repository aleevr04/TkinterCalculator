import tkinter as tk

# COLORS
DARK_GREY = '#222'
LIGHT_GREY = '#3f3f3f'
LIGHT_GREEN = '#1de9b0'
WHITE = '#fafafa'

# FONTS
LARGE_FONT = ('JetBrains Mono', 22, 'bold')
MID_FONT = ('JetBrains Mono', 18, 'bold')
SMALL_FONT = ('JetBrains Mono', 16, 'bold')

# CALCULATOR
class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Calculator')
        self.window.iconbitmap('./calculator.ico')
        self.window.config(bg=DARK_GREY)
        self.window.resizable(0, 0)
    
    def show_digit(self, digit):
        current_num = self.entry.get()
        self.clear()
        self.entry.insert(0, current_num + digit)

    def clear(self):
        self.entry.delete(0, tk.END)
    
    def delete(self):
        self.entry.delete(len(self.entry.get()) - 1, tk.END)
    
    def calc(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.clear()
            self.entry.insert(0, result)
        except SyntaxError:
            self.clear()
            self.entry.insert(0, 'SyntaxError')
        except ZeroDivisionError:
            self.clear()
            self.entry.insert(0, 'Undefined')
    
    def create_entry(self):
        self.entry = tk.Entry(
            self.window, 
            fg=LIGHT_GREEN, 
            bg=DARK_GREY, 
            font=MID_FONT, 
            borderwidth=0
        )
        self.entry.grid(
            row=0, 
            column=0, 
            columnspan=4, 
            padx=20, 
            pady=20
        )

    def create_digits_buttons(self):
        digits = {
            '7': (1, 0), '8': (1, 1), '9': (1, 2), '/': (1, 3),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '*': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '-': (3, 3),
            '.': (4, 0), '0': (4, 1),              '+': (4, 3)
        }

        for digit, grid_value in digits.items():
            button = tk.Button(
                self.window,
                text=digit,
                bg=DARK_GREY, 
                fg=LIGHT_GREEN, 
                font=SMALL_FONT, 
                borderwidth=0, 
                command=lambda x=digit: self.show_digit(x)
            )

            button.grid(
                row=grid_value[0], 
                column=grid_value[1], 
                sticky='nsew', 
                ipady=15
            )

    def create_clear_button(self):
        clear_button = tk.Button(
            self.window, 
            text='C', 
            bg=DARK_GREY, 
            fg=LIGHT_GREEN, 
            font=SMALL_FONT, 
            borderwidth=0, 
            command=self.clear
        )
        clear_button.grid(
            row=4, 
            column=2, 
            sticky='nsew', 
            ipady=15
        )

    def create_del_button(self):
        del_button = tk.Button(
            self.window, 
            text='DEL', 
            bg=LIGHT_GREY, 
            fg=LIGHT_GREEN, 
            font=SMALL_FONT, 
            borderwidth=0,
            command=self.delete
        )
        del_button.grid(
            row=5, 
            column=0, 
            columnspan=2, 
            sticky='nsew', 
            ipady=20
        )
    
    def create_equal_button(self):
        equal_button = tk.Button(
            self.window, 
            text='=', 
            bg=LIGHT_GREEN, 
            fg=DARK_GREY, 
            font=LARGE_FONT, 
            borderwidth=0, 
            command=self.calc
        )
        equal_button.grid(
            row=5, 
            column=2, 
            columnspan=2, 
            sticky='nsew'
        )

    def run(self):
        self.create_entry()
        self.create_digits_buttons()
        self.create_clear_button()
        self.create_del_button()
        self.create_equal_button()
        self.window.mainloop()

calc = Calculator()
calc.run()