
import os
import re


class Tools:



    def createFolder(self, path):

        if not os.path.exists(path):
            os.mkdir(path)

    
    def deleteItem(self, path):

        try:
            os.remove(path)

        except:
            pass

    def is_valid_filename(self, filename):
        # Define forbidden characters for different systems
        windows_forbidden_chars = r'<>:"/\\|?*'
        unix_forbidden_chars = '/'
        
        # Define forbidden names in Windows
        windows_forbidden_names = [
            "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4",
            "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", 
            "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
        ]
        
        # Check for forbidden characters
        if re.search(f'[{windows_forbidden_chars}]', filename):
            return False
        
        if unix_forbidden_chars in filename:
            return False
        
        # Check for forbidden names (case insensitive for Windows)
        if filename.upper() in windows_forbidden_names:
            return False
        
        # Check for length restrictions
        if len(filename) > 255:  # Adjust as needed for specific OS
            return False
        
        return True