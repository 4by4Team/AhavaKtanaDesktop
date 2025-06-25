import tkinter as tk
from tkinter import font
import tkinter.messagebox as messagebox


class ModernApp:
    def __init__(self):
        self.window = tk.Tk()
        self.setup_window()
        self.setup_styles()
        self.create_widgets()

    def setup_window(self):
        """Configure the main window"""
        self.window.title("אוטומצית גרפיקת המדבקות")
        self.window.state('zoomed')  # Full screen on Windows
        # For cross-platform full screen, you can also use:
        # self.window.attributes('-zoomed', True)  # Windows
        # self.window.attributes('-fullscreen', True)  # Linux/Mac
        self.window.configure(bg="#1a1a2e")
        self.window.resizable(True, True)

        # Center the window
        self.center_window()

    def center_window(self):
        """Center the window on screen"""
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def setup_styles(self):
        """Define colors and fonts"""
        self.colors = {
            'primary': '#6c5ce7',
            'secondary': '#a29bfe',
            'success': '#00b894',
            'warning': '#fdcb6e',
            'danger': '#e17055',
            'dark': '#1a1a2e',
            'light': '#ffffff',
            'gray': '#636e72',
            'background': '#16213e',
            'card': '#0f3460',
            'accent': '#74b9ff',
            'gradient_start': '#6c5ce7',
            'gradient_end': '#a29bfe'
        }

        self.fonts = {
            'title': font.Font(family="Segoe UI", size=24, weight="bold"),
            'subtitle': font.Font(family="Segoe UI", size=14),
            'button': font.Font(family="Segoe UI", size=12, weight="bold"),
            'text': font.Font(family="Segoe UI", size=11)
        }

    def create_widgets(self):
        """Create and arrange all widgets"""
        # Main container
        main_frame = tk.Frame(self.window, bg=self.colors['background'])
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        # Header section
        self.create_header(main_frame)

        # Content section
        self.create_content(main_frame)

        # Footer section
        self.create_footer(main_frame)

    def create_header(self, parent):
        """Create the header section"""
        header_frame = tk.Frame(parent, bg=self.colors['background'])
        header_frame.pack(fill='x', pady=(0, 30))

        # Title
        title_label = tk.Label(
            header_frame,
            text="ברוכים הבאים",
            font=self.fonts['title'],
            fg=self.colors['light'],
            bg=self.colors['background']
        )
        title_label.pack()

        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="אוטומצית גרפיקת המדבקות",
            font=self.fonts['subtitle'],
            fg=self.colors['gray'],
            bg=self.colors['background']
        )
        subtitle_label.pack(pady=(5, 0))

        # Decorative line
        line_frame = tk.Frame(header_frame, height=3, bg=self.colors['primary'])
        line_frame.pack(fill='x', pady=(15, 0))

    def create_content(self, parent):
        """Create the main content area"""
        content_frame = tk.Frame(parent, bg=self.colors['card'], relief='flat')
        content_frame.pack(fill='both', expand=True, pady=(0, 20))

        # Add padding inside content frame
        inner_frame = tk.Frame(content_frame, bg=self.colors['card'])
        inner_frame.pack(fill='both', expand=True, padx=50, pady=50)

        # Action buttons container
        buttons_frame = tk.Frame(inner_frame, bg=self.colors['card'])
        buttons_frame.pack(expand=True)

        # Create modern buttons
        self.create_modern_button(
            buttons_frame,
            "📊 להורדת קובץ XL",
            self.download_xl,
            self.colors['success'],
            row=0
        )

        self.create_modern_button(
            buttons_frame,
            "📄 להורדת קובץ JSON",
            self.download_json,
            self.colors['primary'],
            row=1
        )

    def create_modern_button(self, parent, text, command, color, row):
        """Create a modern styled button"""
        btn_frame = tk.Frame(parent, bg=self.colors['card'])
        btn_frame.pack(fill='x', pady=8)

        button = tk.Button(
            btn_frame,
            text=text,
            command=command,
            font=self.fonts['button'],
            bg=color,
            fg=self.colors['light'],
            activebackground=self.lighten_color(color),
            activeforeground=self.colors['light'],
            relief='flat',
            bd=0,
            padx=40,
            pady=15,
            cursor='hand2'
        )
        button.pack(fill='x')

        # Add hover effects
        self.add_hover_effect(button, color)

    def create_footer(self, parent):
        """Create the footer section"""
        footer_frame = tk.Frame(parent, bg=self.colors['background'])
        footer_frame.pack(fill='x')

        footer_label = tk.Label(
            footer_frame,
            text="© 2024 - אוטומצית גרפיקת המדבקות",
            font=self.fonts['text'],
            fg=self.colors['gray'],
            bg=self.colors['background']
        )
        footer_label.pack()

    def add_hover_effect(self, button, original_color):
        """Add hover effects to buttons"""

        def on_enter(e):
            button.configure(bg=self.lighten_color(original_color))

        def on_leave(e):
            button.configure(bg=original_color)

        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)

    def lighten_color(self, color):
        """Lighten a hex color"""
        color_map = {
            '#6c5ce7': '#7d6ef0',
            '#00b894': '#00d2a7',
            '#fdcb6e': '#fed481',
            '#e17055': '#e68368'
        }
        return color_map.get(color, color)

    def download_xl(self):
        """Download XL file"""
        from tkinter import filedialog
        file_path = filedialog.asksaveasfilename(
            title="שמור קובץ Excel",
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")]
        )
        if file_path:
            # כאן תוכל להוסיף את הלוגיקה ליצירת קובץ Excel
            messagebox.showinfo(
                "הצלחה",
                f"קובץ Excel נשמר בהצלחה!\n{file_path} 📊",
                icon='info'
            )

    def download_json(self):
        """Download JSON file"""
        from tkinter import filedialog
        import json

        file_path = filedialog.asksaveasfilename(
            title="שמור קובץ JSON",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if file_path:
            # דוגמה ליצירת קובץ JSON
            sample_data = {
                "app_name": "אוטומצית גרפיקת המדבקות",
                "version": "1.0",
                "created_date": "2024",
                "stickers": []
            }
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(sample_data, f, ensure_ascii=False, indent=2)
                messagebox.showinfo(
                    "הצלחה",
                    f"קובץ JSON נשמר בהצלחה!\n{file_path} 📄",
                    icon='info'
                )
            except Exception as e:
                messagebox.showerror("שגיאה", f"שגיאה בשמירת הקובץ:\n{str(e)}")

    def run(self):
        """Start the application"""
        self.window.mainloop()


# Create and run the application
if __name__ == "__main__":
    app = ModernApp()
    app.run()
