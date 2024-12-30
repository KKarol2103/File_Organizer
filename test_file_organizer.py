import pytest
import os
from file_organizer import FileOrganizer, Path
from file_finder import FileSysFinder
from file_comparision import FileComparision
from messy_fs import messy_fs, small_fs


@pytest.fixture
def f_finder() -> FileSysFinder:
    return FileSysFinder([Path('X')])


def test_get_all_files_from_dir(messy_fs, f_finder):
    files = f_finder.get_all_files_from_dir(Path('Y1'))
    assert Path('Y1/photo_cpy.png') in files
    assert Path('Y1/trips/trip_to_US.docx') in files
    assert Path('Y1/trips/Ncosts.txt') in files
    assert len(files) == 3


def test_get_all_files_from_complex_dir(messy_fs, f_finder):
    files = f_finder.get_all_files_from_dir(Path('X'))
    assert Path('X/some_dir/photos/photo1.png') in files
    assert len(files) == 6

def test_if_file_is_empty(messy_fs):
    assert FileComparision.check_if_file_empty(Path('X/some_dir/empty.dat')) is True
    assert FileComparision.check_if_file_empty(Path('X/a.txt')) is False

def test_find_empty_files_in_small_fs(messy_fs):
    f_finder = FileSysFinder([Path('X'), Path('Y1')])
    all_files = f_finder.get_all_files()
    empty_files = list(f_finder.find_empty_files())
    assert Path('X/some_dir/empty.dat') in empty_files
    assert len(empty_files) == 1

def test_find_empty_files_in_fs(messy_fs):
    f_finder = FileSysFinder([Path('X'), Path('Y1'), Path('Y2'), Path('Y3')])
    empty_files = list(f_finder.find_empty_files())
    assert Path('X/some_dir/empty.dat') in empty_files
    assert Path('Y3/empty.dat') in empty_files
    assert Path('Y3/empty1.dat') in empty_files
    assert Path('Y3/empty2.dat') in empty_files
    assert len(empty_files) == 4


def test_check_if_two_files_are_same(messy_fs):
    assert FileComparision.compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y2/photos/photo1.png')) is True
    assert FileComparision.compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y1/photo_cpy.png')) is True
    assert FileComparision.compare_two_files(Path('X/some_dir/photos/photo1.png'), Path('Y2/data/a.txt')) is False
    assert FileComparision.compare_two_files(Path('Y2/data/b.txt'), Path('Y2/data/a.txt')) is False

def test_find_duplicates(messy_fs):
    f_finder = FileSysFinder([Path('X'), Path('Y1'), Path('Y2'), Path('Y3')])
    all_files = f_finder.get_all_files()
    duplicates = f_finder.find_duplicates()
    assert len(duplicates.keys()) == 6
    

def test_remove_empty_files_from_fs(messy_fs):
    f_organizer = FileOrganizer(Path('X'), Path('Y1'), Path('Y2'), Path('Y3'))
    fs_size_before = len(f_organizer.file_finder.get_all_files())
    f_organizer.remove_files_from_fs(f_organizer.file_finder.find_empty_files())
    fs_size_after = len(f_organizer.file_finder.get_all_files())
    assert messy_fs.exists('X/some_dir/empty.dat') is False
    assert messy_fs.exists('Y3/empty1.dat') is False
    assert fs_size_after == fs_size_before - 4



def test_remove_duplicates(messy_fs):
    f_organizer = FileOrganizer(Path('X'), Path('Y1'), Path('Y2'), Path('Y3'))
    duplicates = f_organizer.file_finder.find_duplicates()
    f_organizer.remove_duplicates(Path('X'), duplicates)
    duplicates_after = f_organizer.file_finder.find_duplicates()
    assert not duplicates_after.values()

def test_check_if_name_contains_bad_symbol(f_finder):
    bad_f_names = ["file:new","file”new","file;new","*filenew","?f?lenew","f$lenew","#flenew","flenew‘","fle|ne|w" ,"fle\\new"]
    valid_name = "file_new"
    bad_name_fun = f_finder.check_if_name_contains_bad_symbol
    assert all(bad_name_fun(f_name) for f_name in bad_f_names)
    assert bad_name_fun(valid_name) is False



def test_detect_newer_ver_of_file(small_fs):
    assert FileComparision.check_if_file_is_newer_ver_of_other('Y/my_doc.pdf', 'X/my_doc.pdf') is True