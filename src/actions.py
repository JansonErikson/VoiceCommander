import pyautogui
import time

screen_width, screen_height = pyautogui.size()


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
        """Take a screenshot (Windows + shift + S)."""
        x = screen_width - 100
        y = screen_height - 120
        pyautogui.hotkey('win', 'shift', 's')
        time.sleep(1)
        pyautogui.press('tab', presses=4, interval=0.2)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('alt', 'f4')

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
        pyautogui.scroll(200)
        pyautogui.keyUp('ctrl')
    
    @staticmethod
    def zoom_out():
        """Zoom out (Ctrl + mouse wheel down)."""
        pyautogui.keyDown('ctrl')
        pyautogui.scroll(-200)
        pyautogui.keyUp('ctrl')
    
    @staticmethod
    def scroll_up():
        """Scroll up (mouse wheel up)."""
        pyautogui.scroll(500)
    
    @staticmethod
    def scroll_down():
        """Scroll down (mouse wheel down)."""
        pyautogui.scroll(-500)


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
        """Toggle the bookmarks bar (Ctrl + Shift + O)."""
        pyautogui.hotkey('ctrl', 'shift', 'o')

def execute_action(command, window_instance):
    """Execute the action corresponding to the given command."""
    command = command.lower()
    if command in actions:
        if command == "kommandos":
            window_instance.toggle_commands()
        else:
            actions[command]()
    else:
        print(f"Unbekannter Befehl: {command}")

# Dictionary to map commands to actions
actions = {
    "desktop": WindowsShortcuts.show_desktop,
    "explorer": WindowsShortcuts.open_file_explorer,
    "switchen": WindowsShortcuts.switch_window,
    "tab wechseln": WindowsShortcuts.switch_tab,
    "übersicht": WindowsShortcuts.open_task_view,
    "fenster schließen": WindowsShortcuts.close_window,
    "screenshot": WindowsShortcuts.take_screenshot,
    "pfeil hoch": KeyPress.arrow_up,
    "pfeil runter": KeyPress.arrow_down,
    "pfeil links": KeyPress.arrow_left,
    "pfeil rechts": KeyPress.arrow_right,
    "weiter": KeyPress.press_tab,
    "enter": KeyPress.press_enter,
    "windows": KeyPress.open_start_menu,
    "plus": ZoomAndScroll.zoom_in,
    "minus": ZoomAndScroll.zoom_out,
    "hoch": ZoomAndScroll.scroll_up,
    "runter": ZoomAndScroll.scroll_down,
    "internet": GoogleChrome.start_chrome,
    "neuer tab": GoogleChrome.open_new_tab,
    "tab schließen": GoogleChrome.close_tab,
    "nächster tab": GoogleChrome.next_tab,
    "tab zurück": GoogleChrome.previous_tab,
    "downloads öffnen": GoogleChrome.open_downloads,
    "lesezeichen": GoogleChrome.toggle_bookmarks
}
