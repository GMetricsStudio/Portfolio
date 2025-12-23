import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
import json

class ThemeEditor:
    def __init__(self, parent, app):
        self.app = app
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Advanced Theme Editor")
        self.dialog.geometry("600x700")
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        self.original_colors = self.app.theme_engine.color_map.copy()
        self.temp_colors = self.app.theme_engine.color_map.copy()
        
        self.setup_ui()
        self.apply_theme_to_dialog()
        
    def setup_ui(self):
        # Main container with scrollbar
        main_frame = ttk.Frame(self.dialog)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Theme Name frame
        name_frame = ttk.Frame(main_frame)
        name_frame.pack(fill="x", pady=(0, 10))
        ttk.Label(name_frame, text="Theme Name:").pack(side="left")
        self.theme_name_var = tk.StringVar(value="Custom Theme")
        ttk.Entry(name_frame, textvariable=self.theme_name_var).pack(side="left", fill="x", expand=True, padx=5)
        
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Categories
        self.create_category("General", ["window_bg", "window_fg", "panel_bg", "panel_fg", "panel_border", "status_bg", "status_fg"])
        self.create_category("Editor", ["editor_bg", "editor_fg", "editor_cursor", "editor_selection", "editor_gutter", "editor_gutter_fg", "editor_line_highlight"])
        self.create_category("Syntax", ["syntax_keyword", "syntax_string", "syntax_comment", "syntax_function", "syntax_number", "syntax_builtin", "syntax_class", "syntax_variable"])
        self.create_category("Sidebar", ["tree_bg", "tree_fg", "tree_selection"])
        self.create_category("Buttons & Inputs", ["button_bg", "button_fg", "button_hover", "entry_bg", "entry_fg", "entry_border"])
        self.create_category("Console", ["console_bg", "console_fg", "console_error", "console_success"])
        
        # Bottom Buttons
        btn_frame = ttk.Frame(self.dialog)
        btn_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(btn_frame, text="Apply Changes", command=self.apply_changes).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Save & Close", command=self.save_and_close).pack(side="right", padx=5)
        ttk.Button(btn_frame, text="Cancel", command=self.cancel).pack(side="right")

    def cancel(self):
        """Revert to original colors and close"""
        self.app.theme_engine.color_map.update(self.original_colors)
        self.app.apply_theme_to_all()
        self.dialog.destroy()

    def create_category(self, name, keys):
        frame = ttk.LabelFrame(self.scrollable_frame, text=name)
        frame.pack(fill="x", padx=5, pady=5, expand=True)
        
        for key in keys:
            if key in self.temp_colors:
                row = ttk.Frame(frame)
                row.pack(fill="x", padx=5, pady=2)
                
                label = key.replace("_", " ").title()
                ttk.Label(row, text=label, width=25).pack(side="left")
                
                color_val = self.temp_colors[key]
                color_btn = tk.Button(row, bg=color_val, width=10, relief="flat", 
                                    command=lambda k=key: self.pick_color(k))
                color_btn.pack(side="right", padx=5)
                # Store button ref to update color
                if not hasattr(self, "color_btns"): self.color_btns = {}
                self.color_btns[key] = color_btn

    def pick_color(self, key):
        initial = self.temp_colors[key]
        color = colorchooser.askcolor(color=initial, title=f"Choose color for {key}")
        if color[1]:
            self.temp_colors[key] = color[1]
            self.color_btns[key].config(bg=color[1])
            
    def apply_changes(self):
        """Live preview changes"""
        self.app.theme_engine.color_map.update(self.temp_colors)
        self.app.apply_theme_to_all()
        self.apply_theme_to_dialog()
        
    def save_and_close(self):
        self.apply_changes()
        name = self.theme_name_var.get().strip() or "Custom Theme"
        
        # Save to custom themes list
        if "custom_themes" not in self.app.settings:
            self.app.settings["custom_themes"] = {}
            
        self.app.settings["custom_themes"][name] = self.temp_colors
        self.app.settings["theme_preset"] = name
        
        self.app.save_settings(self.app.settings)
        messagebox.showinfo("Saved", f"Theme '{name}' saved to presets.")
        self.dialog.destroy()
        
    def apply_theme_to_dialog(self):
        if self.app.theme_engine:
            bg = self.temp_colors["window_bg"]
            fg = self.temp_colors.get("window_fg", "#d4d4d4")
            self.dialog.configure(bg=bg)
            # Re-applying styles to self.dialog sub-components is hard without recursive walk
            # but usually the window_bg is enough for the toplevel background.
