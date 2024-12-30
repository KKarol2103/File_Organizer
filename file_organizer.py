import os
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path
from file_finder import FileSysFinder
from fileOrganizerUI import FileOrganizerUI
import time

class FileOrganizer:
    def __init__(self, main_dir: Path, *args: tuple[Path]):
        self._main_dir = main_dir
        self._other_directories = list(args)
        self.file_finder = FileSysFinder(self._other_directories + [main_dir])


    def organize_fs(self):
        empty_files = self.file_finder.find_empty_files()
        if empty_files:
            FileOrganizerUI.show_empty_files(empty_files)
            dec = FileOrganizerUI.get_decision_from_user()
            FileOrganizerUI.show_action(dec)
            if dec == 1:
                self.remove_files_from_fs(empty_files)

            if dec == 3:
                files_indx_to_remove = FileOrganizerUI.ask_which_files_to_remove()
                files_to_remove = [empty_files[index] for index in files_indx_to_remove]
                self.remove_files_from_fs(files_to_remove)

            print('Files removed') if dec != 2 else print("Files not changed")
            time.sleep(1)

        duplicates = self.file_finder.find_duplicates()
        if duplicates:
            FileOrganizerUI.show_duplicates(duplicates)
            dec = FileOrganizerUI.ask_what_to_do_with_duplicates(self._main_dir)
            if dec == 1:
                self.remove_duplicates(self._main_dir, duplicates)

    def remove_files_from_fs(self, files_to_remove: list[Path]):
        for file in list(files_to_remove):
            os.remove(Path.absolute(file))
        self.file_finder.update()

    def remove_duplicates(self, main_dir: Path, duplicates: defaultdict[Path, list[Path]]):
        for file, f_duplicates in duplicates.items():
            same_files = f_duplicates + [file]
            for duplicate in same_files:
                if str(main_dir) not in str(duplicate):
                    os.remove(duplicate)
        self.file_finder.update()



def main():
    parser = ArgumentParser()
    parser.add_argument("dst_dir", help="Main dir where you want to organize your files", type=Path)
    parser.add_argument("other_dir", help="Other dirs", nargs='+', type=Path)
    args = parser.parse_args()


    absolute_paths = [Path.absolute(dir) for dir in args.other_dir]

    print(f'Main Directory Selected: {args.dst_dir}')
    print(f'Other Directories: ')
    print([str(dir) for dir in args.other_dir])

    print('Welcome to the file organizer!')
    print("Starting organizing!")
    file_organizer = FileOrganizer(args.dst_dir.absolute(), *absolute_paths)
    file_organizer.organize_fs()

if __name__ == "__main__":
    main()

