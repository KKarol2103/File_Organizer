import pytest
import os
from file_organizer import (get_all_files_from_dir, 
                            check_if_file_empty,
                             organize_fs, 
                             find_empty_files,
                             compare_two_files,
                             get_all_fs_files,
                             find_duplicates,
                             check_if_file_is_newer_ver_of_other,
                             Path)
from messy_fs import messy_fs, small_fs

def test_get_all_files_from_dir(messy_fs):
    files = get_all_files_from_dir(Path('Y1'))
    assert Path('Y1/photo_cpy.png') in files
    assert Path('Y1/trips/trip_to_US.docx') in files
    assert Path('Y1/trips/Ncosts.txt') in files
    assert len(files) == 3


def test_get_all_files_from_complex_dir(messy_fs):
    files = get_all_files_from_dir(Path('X'))
    assert Path('X/some_dir/photos/photo1.png') in files
    assert len(files) == 6

def test_if_file_is_empty(messy_fs):
    assert check_if_file_empty(Path('X/some_dir/empty.dat')) is True
    assert check_if_file_empty(Path('X/a.txt')) is False

def test_find_empty_files_in_small_fs(messy_fs):
    all_files = get_all_fs_files(Path('X'), Path('Y1'))
    empty_files = list(find_empty_files(all_files))
    assert Path('X/some_dir/empty.dat') in empty_files
    assert len(empty_files) == 1

def test_find_empty_files_in_fs(messy_fs):
    all_files = get_all_fs_files(Path('X'), Path('Y1'), Path('Y2'), Path('Y3'))
    empty_files = list(find_empty_files(all_files))
    assert Path('X/some_dir/empty.dat') in empty_files
    assert Path('Y3/empty.dat') in empty_files
    assert Path('Y3/empty1.dat') in empty_files
    assert Path('Y3/empty2.dat') in empty_files
    assert len(empty_files) == 4


def test_check_if_two_files_are_same(messy_fs):
    assert compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y2/photos/photo1.png')) is True
    assert compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y1/photo_cpy.png')) is True
    assert compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y2/data/a.txt')) is False
    assert compare_two_files(Path('Y2/data/b.txt'), Path('Y2/data/a.txt')) is False

def test_find_duplicates(messy_fs):
    all_files = get_all_fs_files(Path('X'), Path('Y1'), Path('Y2'), Path('Y3'))
    duplicates = find_duplicates(all_files)
    assert len(duplicates.keys()) == 6
    

def test_remove_empty_files_from_fs(messy_fs, monkeypatch):
    fs_size_before = len(get_all_fs_files(Path('X'), Path('Y1'), Path('Y2'), Path('Y3')))
    monkeypatch.setattr('builtins.input', lambda _: "1")
    organize_fs(Path('X'), Path('Y1'), Path('Y2'), Path('Y3'))
    fs_size_after = len(get_all_fs_files(Path('X'), Path('Y1'), Path('Y2'), Path('Y3')))

    assert messy_fs.exists('X/some_dir/empty.dat') is False
    assert messy_fs.exists('Y3/empty1.dat') is False
    assert fs_size_after == fs_size_before - 4


def test_detect_newer_ver_of_file(small_fs):
    assert check_if_file_is_newer_ver_of_other('Y/my_doc.pdf', 'X/my_doc.pdf') is True