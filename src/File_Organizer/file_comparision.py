from pathlib import Path
import os


class FileComparision:
    @staticmethod
    def compare_two_files(file1: Path, file2: Path) -> bool:
        with open(file1, 'rb') as file1_h, open(file2, 'rb') as file2_h:
            return file1_h.read() == file2_h.read()
    
    @staticmethod
    def check_if_file_empty(file: Path) -> bool:
        return True if os.stat(file).st_size == 0 else False

    @staticmethod
    def check_if_file_is_newer_ver_of_other(file1: Path, file2: Path) -> bool:
        return os.stat(file1).st_ctime >= os.stat(file2).st_ctime
    

