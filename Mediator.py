from tkinter import Button
from typing import Text


class Form:
    
    
    def __init__(self):
        self.create_widgets()
        self.create_mediator()
        
        
        
    def create_widgets(self):
        self.nameText= Text()
        self.emailText= Text()
        self.okButton= Button("OK")
        self.cancelButtom= Button("Cancel")
        
    def create_mediator(self):