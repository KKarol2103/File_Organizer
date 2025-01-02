# Dokumentacja Projektu: Organizacja Systemu Plików

## Autor
Karol Kuc

## Wprowadzenie
Celem projektu jest napisanie skryptu w wybranym języku (w moim przypadku jest to **Python + Bash**) który umożliwi wykonanie różnych, opisanych w instrukcji operacji na systemie plików prowadzących do porządkowania struktury plików. 

W celu realizacji zadania napisałem opisane poniżej skrypty. 
----------

## Skrypty

- ## Skrypt Uruchamiający Projekt

- ### Opis
**run.sh** : Skrypt Bash odpowiedzialny za stworzenie przykładowej struktury plików i katalogów (przy pomocy opisanego poniżej skryptu **create_fs.sh**) a następnie uruchomieniu na stworzonej strukturze właściwego skryptu **file_organizer.py** odpowiedzialnego za porządkowanie systemu plików. 

- ### Uwaga!!!
Ten skrypt służy do demonstracji działania napisanego programu na przykładowej strukturze plików opisanej poniżej w dokumentacji.

Jeśli chcesz uruchomić file_organizer.py na dowolnej istniejącej strukturze katalogów, możesz to zrobić bez użycia skryptu run.sh. Wystarczy wywołać go w następujący sposób:

python3 ./file_organizer.py <Główny katalog> [Pozostałe katalogi]
Główny katalog: Ścieżka do głównego katalogu, w którym mają się znaleźć wszystkie pliki.
[Pozostałe katalogi] (opcjonalne): Dodatkowe katalogi do uwzględnienia w procesie organizacji.
Przykład użycia:

python3 ./file_organizer.py /home/user/documents /home/user/photos
W powyższym przykładzie skrypt uporządkuje pliki znajdujące się w katalogach /home/user/documents oraz /home/user/photos.

- ## Skrypt Tworzący Strukturę Plików

- ### Opis
**create_fs.sh** : Skrypt Bash tworzy strukturę katalogów i plików z zawartością w odpowiednich miejscach. Struktura zawiera katalogi i pliki przeznaczone do różnych celów, takich jak zdjęcia, dokumenty, dane i inne.

- ### Struktura Katalogów i Plików

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

- ## Skrypt Usuwający Strukturę Plików
- ### Opis
**delete_fs.sh** : Skrypt Bash odpowiada za usunięcie wszystkich wcześniej utworzonych katalogów i plików przy pomocy **create_fs.sh**.


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
