import importlib
import subprocess
import sys

def ensure_library(lib_name: str):
    """
    Comprueba si una librería está instalada.
    Si no lo está, intenta instalarla con pip y la importa.
    Devuelve el módulo o None si falla.
    """
    try:
        return importlib.import_module(lib_name)
    except ImportError:
        print(f"La librería '{lib_name}' no está instalada. Intentando instalarla...")

        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", lib_name],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            print("Error instalando la librería:")
            print(result.stderr)
            return None

        print(f"Librería '{lib_name}' instalada correctamente. Importando...")
        return importlib.import_module(lib_name)