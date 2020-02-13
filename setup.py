from cx_Freeze import setup, Executable

setup(
    name    = "Automation (Monica)",
    version = "1.0",
    description = "Automation upload to Google Forms through spreadsheet",
    executables = [Executable("index.py")]
)
