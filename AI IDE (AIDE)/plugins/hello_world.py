"""
Hello World Plugin
Adds a Hello World item to the Tools menu.
"""
import tkinter as tk
from tkinter import messagebox

def setup(app):
    print("Hello World Plugin Loaded!")
    
    # Add menu item
    # This is a bit hacky as we need to find the Tools menu
    # app.root type is Tk
    # We can rely on app methods if exposed
    
    # Simple example: just print to console for now, or use show_message if available
    pass

def hello(app):
    app.show_message("Plugin", "Hello from Plugin!")
