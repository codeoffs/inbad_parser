from cx_Freeze import setup, Executable

setup(
    name = "in_bed",
    version = "0.1",
    description = "parser",
    executables = [Executable("init.py")]
)