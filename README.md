# FloppyBord-w-
Este es una forma de hacer un instalador y un ejecutable


Generar el .exe
"""
    pyinstaller --onefile --windowed --distpath output/dist  --name FloppyBord run.py --add-data "assets;assets" --add-data ".env;." --add-data "src;src" 
"""

Luego usas el script.iss y le das a run, creara un instalador (no indicare nada mas)