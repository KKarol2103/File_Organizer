from pathlib import Path
from collections import defaultdict
from itertools import chain
import os
from File_Organizer.file_comparision import FileComparision

class FileSysFinder:
    def __init__(self, directories: list[Path]) -> None:
        self.directories = directories
        self.files = self.get_all_files()

    @property
    def get_files(self):
        return self.files

    def get_all_files_from_dir(self, dir_path: Path) -> list[Path]:
        return [path for path in dir_path.glob('**/*') if path.is_file()]

    def update(self):
        self.files = list(filter(os.path.exists, self.files))


    def get_all_files(self) -> list[Path]:
        dir_files = [self.get_all_files_from_dir(dir) for dir in self.directories]
        return list(chain.from_iterable(dir_files))


    def find_empty_files(self) -> list[Path]:
        return list(filter(FileComparision.check_if_file_empty, self.files))

    def find_duplicates(self) -> dict[Path, list[Path]]:
        duplicates = defaultdict(list)
        for index, file in enumerate(self.files):
            if file in list(chain.from_iterable(duplicates.values())):
                continue

            for another_file in self.files[index+1:]:
                if FileComparision.compare_two_files(file, another_file):
                    duplicates[file].append(another_file)

        return duplicates

    def check_if_name_contains_bad_symbol(self, file_name: str) -> bool:
        bad_symbols = [":", "”", ";", "*", "?", "$", "#", "‘", "|", "\\"]
        return any(char in bad_symbols for char in file_name)


    def find_files_with_bad_names(self) -> list[Path]:
        files_with_bad_names = []
        for file in self.files:
            if self.check_if_name_contains_bad_symbol(file.name):
                files_with_bad_names.append(file)

        return files_with_bad_names

    def find_newer_ver_of_file(self):
        newer_ver = defaultdict(list)
        for index, file in enumerate(self.files):
            if file in list(chain.from_iterable(newer_ver.values())):
                continue

            for another_file in self.files[index+1:]:
                if FileComparision.check_if_file_is_newer_ver_of_other(file, another_file):
                    newer_ver[file].append(another_file)

        return newer_ver
