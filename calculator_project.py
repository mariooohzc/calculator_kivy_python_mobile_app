'''
The addition, subtraction, division, multiplication, remainder function is defined below
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from math import sin, cos, tan

Builder.load_file('calculator_project.kv')

class MyGrid(GridLayout):

    #method for the button
    def pressed(self, button):
        current_text = self.ids.screen.text
        try:
            if current_text == "0":
                self.ids.screen.text = f"{button}"
            else:
                self.ids.screen.text = f"{current_text}{button}"
        except:
            self.ids.screen.text = "0"

    def clear(self):
        self.ids.screen.text = '0'
    
    def math_f(self, f_name):
        try:
            self.ids.screen.text = f"{f_name}("
        except:
            self.ids.screen.text = "0"
    
    def operator(self, operator_name):
        current_text = self.ids.screen.text
        try:
            self.ids.screen.text = f"{current_text}{operator_name}"
        except:
            self.ids.screen.text = "0"

    #function is called when the user hits the "=" button
    def result(self):
        current_text = self.ids.screen.text
        try:
            #identify if the trigonometric function is in the string
            if "cos" in current_text or "sin" in current_text or "tan" in current_text:
                new_text = current_text + ")"
                self.ids.screen.text = str(eval(new_text))
            else:
                # identify the operators that is in the string and find its position/index
                if "+" in current_text:
                    operator_index = current_text.index("+")
                    self.ids.screen.text = str(addition(int(current_text[:operator_index]), int(current_text[operator_index+1:])))
                elif "-" in current_text:
                    operator_index = current_text.index("-")
                    self.ids.screen.text = str(subtraction(int(current_text[:operator_index]), int(current_text[operator_index+1:])))
                elif "*" in current_text:
                    operator_index = current_text.index("*")
                    self.ids.screen.text = str(multiplication(int(current_text[:operator_index]), int(current_text[operator_index+1:])))
                elif "/" in current_text:
                    operator_index = current_text.index("/")
                    self.ids.screen.text = str(division(int(current_text[:operator_index]), int(current_text[operator_index+1:])))
                elif "%" in current_text:
                    operator_index = current_text.index("%")
                    self.ids.screen.text = str(remainder(int(current_text[:operator_index]), int(current_text[operator_index+1:])))
                else:
                    self.ids.screen.text = "0"

        except:
            self.ids.screen.text = "0"

#defining addition, subtraction, multiplication, division, modulos (remainder)
def addition(x, y):
    while y != 0:
        x += 1
        y -= 1
    return x

def subtraction(x, y):
    while y > 0:
        x -= 1
        y -= 1
    return x

def multiplication(x, y):
    ans = 0
    while y > 0:
        ans += x
        y -= 1
    return ans

def division(x, y):
    if x < y:
        print("working : division")
        return f"0 Remainder {x}"
    else:
        quotient = 0
        while x >= y:
            quotient += 1
            x -= y
        return f"{quotient} R {x}"

def remainder(x, y):
    if x < y:
        return f"Remainder {x}"
    else:
        while x >= y:
            x -= y
        return f"Remainder {x}"

class MyApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    MyApp().run()