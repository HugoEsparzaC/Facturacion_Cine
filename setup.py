from cx_Freeze import setup, Executable
setup(
    name = 'Sistema de Facturacion',
    options = {
        'build_exe':{'packages':['tkinter', 'time', 'datetime'],
        'include_files':[r"C:\Users\Lu Zhou\Python\Cine\Cine.ico"]}    
    },
    version = '1.0',
    description = "Mi aplicacion",
    executables = [Executable(r'C:\Users\Lu Zhou\Python\Cine\Customer_Billing_Cine.py',
    icon = r'C:\Users\Lu Zhou\Python\Cine\Cine.ico',
    shortcutDir = 'DesktopFolder',
    base = 'Win32GUI'
    )]
)