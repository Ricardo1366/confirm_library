from confirm_library import ensure_library

numpy = ensure_library("numpy")
if numpy:
    print("Versión de numpy:", numpy.__version__)