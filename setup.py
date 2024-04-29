from cx_Freeze import setup, Executable

setup(
    name="PDF_Uploader",
    version="1.0",
    description="PDF Uploader App",
    executables=[Executable("gui.py")]
)
