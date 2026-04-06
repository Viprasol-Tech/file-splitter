"""
file-splitter - Split large files into smaller chunks

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import FileSplitter, split, process, main

__all__ = ["FileSplitter", "split", "process", "main"]
