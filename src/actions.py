import pyautogui
import time

class WindowsShortcuts:
    """A class that provides methods for common Windows shortcuts."""

    @staticmethod
    def show_desktop():
        """Show the desktop (Windows + D)."""
        pyautogui.hotkey('win', 'd')

    @staticmethod
    def open_file_explorer():
        """Open File Explorer (Windows + E)."""
        pyautogui.hotkey('win', 'e')

    @staticmethod
    def switch_window():
        """Switch to the next window (Alt + Tab)."""
        pyautogui.hotkey('alt', 'tab')

    @staticmethod
    def switch_tab():
        """Switch to the next tab (Ctrl + Tab)."""
        pyautogui.hotkey('ctrl', 'tab')

    @staticmethod
    def open_task_view():
        """Open Task View (Windows + Tab)."""
        pyautogui.hotkey('win', 'tab')

    @staticmethod
    def close_window():
        """Close the current window (Alt + F4)."""
        pyautogui.hotkey('alt', 'f4')

    @staticmethod
    def take_screenshot():
        """Take a screenshot (Windows + PrtScn)."""
        pyautogui.hotkey('win', 'prtscn')


class KeyPress:
    """A class that provides methods for pressing individual keys."""

    @staticmethod
    def arrow_up():
        """Press the up arrow key."""
        pyautogui.press('up')
    
    @staticmethod
    def arrow_down():
        """Press the down arrow key."""
        pyautogui.press('down')
    
    @staticmethod
    def arrow_left():
        """Press the left arrow key."""
        pyautogui.press('left')
    
    @staticmethod
    def arrow_right():
        """Press the right arrow key."""
        pyautogui.press('right')
    
    @staticmethod
    def press_tab():
        """Press the Tab key."""
        pyautogui.press('tab')
    
    @staticmethod
    def press_enter():
        """Press the Enter key."""
        pyautogui.press('enter')
    
    @staticmethod
    def open_start_menu():
        """Open the Start menu (Windows key)."""
        pyautogui.press('win')


class ZoomAndScroll:
    """A class that provides methods for zooming and scrolling."""

    @staticmethod
    def zoom_in():
        """Zoom in (Ctrl + mouse wheel up)."""
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(120)
        pyautogui.keyUp('ctrl')
    
    @staticmethod
    def zoom_out():
        """Zoom out (Ctrl + mouse wheel down)."""
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-120)
        pyautogui.keyUp('ctrl')
    
    @staticmethod
    def scroll_up():
        """Scroll up (mouse wheel up)."""
        pyautogui.scroll(100)
    
    @staticmethod
    def scroll_down():
        """Scroll down (mouse wheel down)."""
        pyautogui.scroll(-100)


class GoogleChrome:
    """A class that provides methods for controlling Google Chrome."""

    @staticmethod
    def start_chrome():
        """Start Google Chrome."""
        pyautogui.hotkey('win')
        pyautogui.typewrite('Google Chrome')
        pyautogui.press('enter')

    @staticmethod
    def open_new_tab():
        """Open a new tab (Ctrl + T)."""
        pyautogui.hotkey('ctrl', 't')
    
    @staticmethod
    def close_tab():
        """Close the current tab (Ctrl + W)."""
        pyautogui.hotkey('ctrl', 'w')
    
    @staticmethod
    def next_tab():
        """Switch to the next tab (Ctrl + Tab)."""
        pyautogui.hotkey('ctrl', 'tab')
    
    @staticmethod
    def previous_tab():
        """Switch to the previous tab (Ctrl + Shift + Tab)."""
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    
    @staticmethod
    def open_downloads():
        """Open the download manager (Ctrl + J)."""
        pyautogui.hotkey('ctrl', 'j')
    
    @staticmethod
    def toggle_bookmarks():
        """Toggle the bookmarks bar (Ctrl + Shift + B)."""
        pyautogui.hotkey('ctrl', 'shift', 'b')