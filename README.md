# Dokumentacja Projektu: Organizacja Systemu Plików

## Autor
Karol Kuc

## Wprowadzenie
Ten projekt ma na celu demonstrację organizacji systemu plików poprzez utworzenie przykładowej struktury katalogów i plików przy użyciu skryptu Bash. Wygenerowana struktura może być używana jako baza do testowania różnych operacji na systemie plików.

----------

## Skrypty

- ## Skrypt Tworzący Strukturę Plików

### Opis
Skrypt Bash tworzy strukturę katalogów i plików z zawartością w odpowiednich miejscach. Struktura zawiera katalogi i pliki przeznaczone do różnych celów, takich jak zdjęcia, dokumenty, dane i inne.

### Struktura Katalogów i Plików

1.  **test/** - Główny katalog

-  **X/**

-  **some_dir/**

-  **photos/**

- photo1.png

- photo2.png

- photo3.png

-  **docs/**

- trip.docx

- a.txt

- some_dir/empty.dat

-  **Y1/**

- photo_cpy.png

-  **trips/**

- trip_to_US.docx

- Ncosts.txt

-  **Y2/**

-  **photos/**

- photo1.png

- photo2.png

- photo3.png

- photo$4.png

-  **data/**

- a.txt

- b.txt

- c.txt

- d*1!.txt

-  **Y3/**

- empty.dat

- empty1.dat

- empty2.dat

----------
## Struktura Po Wykonaniu Skryptu
Po uruchomieniu skryptu otrzymasz następującą strukturę plików i katalogów:
```
test/

|-- X/

| |-- a.txt

| |-- some_dir/

| | |-- empty.dat

| | `-- photos/

| | |-- photo1.png

| | |-- photo2.png

| | `-- photo3.png

| `-- docs/

| `-- trip.docx

|-- Y1/

| |-- photo_cpy.png

| `-- trips/

| |-- trip_to_US.docx

| `-- Ncosts.txt

|-- Y2/

| |-- photos/

| | |-- photo1.png

| | |-- photo2.png

| | |-- photo3.png

| | `-- photo$4.png

| `-- data/

| |-- a.txt

| |-- b.txt

| |-- c.txt

| `-- d*1!.txt

`-- Y3/

|-- empty.dat

|-- empty1.dat

`-- empty2.dat

```

## Klasy w Projekcie
### FileComparision
Klasa odpowiada za różnorodne operacje porównawcze na plikach.

#### Funkcje:
-   **compare_two_files(file1, file2)**: Porównuje zawartość dwóch plików.
    
-   **check_if_file_empty(file)**: Sprawdza, czy plik jest pusty.
    
-   **check_if_file_is_newer_ver_of_other(file1, file2)**: Sprawdza, czy jeden plik jest nowszą wersją drugiego.
    

### FileSysFinder
Klasa odpowiedzialna za wyszukiwanie plików w systemie plików.

#### Funkcje:
-   **get_all_files_from_dir(dir_path)**: Pobiera wszystkie pliki z danego katalogu.
    
-   **find_empty_files()**: Znajduje wszystkie puste pliki.
    
-   **find_duplicates()**: Znajduje zduplikowane pliki.
    
-   **find_files_with_bad_names()**: Znajduje pliki z nieprawidłowymi nazwami.
    
-   **find_newer_ver_of_file()**: Znajduje nowsze wersje plików.
    

### FileOrganizer
Klasa główna zarządzająca organizacją systemu plików.

#### Funkcje:
-   **organize_fs()**: Główna funkcja organizująca pliki - obsługuje puste pliki, duplikaty i złe nazwy plików.
    
-   **remove_files_from_fs(files_to_remove)**: Usuwa pliki z systemu plików.
    
-   **replace_bad_symbols_with_special_char(f_name, char)**: Zastępuje nieprawidłowe symbole w nazwach plików.
    

### FileOrganizerUI
Klasa obsługująca interfejs użytkownika dla operacji organizacji plików.

#### Funkcje:
-   **show_empty_files(empty_files)**: Wyświetla listę pustych plików.
    
-   **show_duplicates(duplicates)**: Wyświetla listę zduplikowanych plików.
    
-   **show_files_with_bad_names(files_with_bad_names)**: Wyświetla listę plików z nieprawidłowymi nazwami.
    
-   **ask_what_to_do_with_bad_f_names()**: Pyta użytkownika, co zrobić z nieprawidłowymi nazwami plików.
