"""Backward-compatible I/O helpers used in soil physics examples."""

import sys
from pathlib import Path

_SRC_DIR = str(Path(__file__).resolve().parent.parent)
if sys.path[0] != _SRC_DIR:
    try:
        sys.path.remove(_SRC_DIR)
    except ValueError:
        pass
    sys.path.insert(0, _SRC_DIR)
from utils.io import read_data_file, read_generic_data_file, scan_data_file


# Backward compatible aliases
scanDataFile = scan_data_file
readDataFile = read_data_file
readGenericDataFile = read_generic_data_file
