# Extracted from ./data/repos/black/src/black/__init__.py
# PyInstaller patches multiprocessing to need freeze_support() even in non-Windows
# environments so just assume we always need to call it if frozen.
if getattr(sys, "frozen", False):
    from multiprocessing import freeze_support

    freeze_support()

main()
