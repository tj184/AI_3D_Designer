"""
Theme Manager

Creates the main application window and
configures the global ttkbootstrap theme.
"""

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import font


# ==========================================================
# Theme Configuration
# ==========================================================

DEFAULT_THEME = "darkly"

DEFAULT_FONT = "Segoe UI"

DEFAULT_FONT_SIZE = 10

HEADING_FONT_SIZE = 12

TITLE_FONT_SIZE = 14


# ==========================================================
# Create Window
# ==========================================================

def create_window():

    root = ttk.Window(
        themename=DEFAULT_THEME
    )

    configure_fonts()

    configure_styles()

    return root


# ==========================================================
# Fonts
# ==========================================================

def configure_fonts():

    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(
        family=DEFAULT_FONT,
        size=DEFAULT_FONT_SIZE
    )

    text_font = font.nametofont("TkTextFont")
    text_font.configure(
        family=DEFAULT_FONT,
        size=DEFAULT_FONT_SIZE
    )

    menu_font = font.nametofont("TkMenuFont")
    menu_font.configure(
        family=DEFAULT_FONT,
        size=DEFAULT_FONT_SIZE
    )

    heading_font = font.Font(
        family=DEFAULT_FONT,
        size=HEADING_FONT_SIZE,
        weight="bold"
    )

    title_font = font.Font(
        family=DEFAULT_FONT,
        size=TITLE_FONT_SIZE,
        weight="bold"
    )

    # Store globally for later use
    tk._heading_font = heading_font
    tk._title_font = title_font


# ==========================================================
# Styles
# ==========================================================

def configure_styles():

    style = ttk.Style()

    # General widget padding
    style.configure(
        "TButton",
        padding=6
    )

    style.configure(
        "TLabelframe",
        padding=8
    )

    style.configure(
        "Treeview",
        rowheight=24
    )

    style.configure(
        "TNotebook.Tab",
        padding=(12, 6)
    )

    style.configure(
        "Status.TLabel",
        padding=4
    )


# ==========================================================
# Theme Utilities
# ==========================================================

def set_theme(window, theme_name):
    """
    Change application theme at runtime.

    Example:
        set_theme(root, "cosmo")
    """

    style = ttk.Style(window)

    style.theme_use(theme_name)


def get_available_themes():
    """
    Return all installed ttkbootstrap themes.
    """

    style = ttk.Style()

    return style.theme_names()