# Connect-dots
## Implementacja algorytmu przewidującego położenie optimum funkcji na podstawie stopniowego odrzucania kolejnych punktów środkowych zbioru punktów próbkującego daną przestrzeń.

### Opis algorytmu
- Dana jest populacja `N` punktów `P0={x1, x2, … xN}` w przestrzeni d-wymiarowej; `N>d` 
- Dla każdego z punktów mamy obliczone wartości funkcji celu `{q1, q2, … qN}`
- Maksymalizujemy funkcję `q` 
- Powtarzamy następujące kroki do momentu, gdy liczebność zbioru Pi spadnie do wartości d 
	1. Wyznaczamy punkt ci będący punktem środkowym zbioru `Pi`
	2. Znajdujemy punkt `xw` dla którego wartość funkcji `qw` jest najmniejsza w zbiorze `Pi` 
	3. zbiór `Pi+1` powstaje poprzez usunięcie punktu `xw` ze zbioru `Pi` 

W ten sposób mamy zdefiniowany ciąg punktów `ci` który przetwarzamy w następujący sposób:  
Dla każdej współrzędnej punktów `ci` analizujemy jej ciąg wartości. Propozycja na dziś jest taka, że konstruujemy funkcję `ci(i)`, robimy regresję liniową względem i, po czym odczytujemy wartość `ci(Nd)`. Wartość tę traktujemy jako estymator położenia optimum lokalnego. 
Otrzymane punkty środkowe wykorzystywane są do wyliczenia regresji liniowych, dla każdego wymiaru oddzielnie.
Regresje przewidują wartość współrzędnej od procenta niewykorzystanych punktów środkowych.
Obliczone regresje służą do predykcji optimum.
Przewidywana wartość danej współrzędnej optimum jest równa wartości wyrazu wolnego regresji liniowej, w tym wymiarze.
W sytuacji, gdy procent niewykorzystanych punktów wynosi 0, wartość predykcji jest równa wartości wyrazu wolnego regresji. 

### Przed uruchomieniem
1. Przejdź do folderu projektu
2. Zainstaluj wymagane biblioteki (`pip install -r requirements.txt`)

### Generacja punktów
Generuje n d-wymiarowych punktów z współrzędnymi w o rozkładzie `U[BOTTOM, TOP]`.  
Oblicza wartość funkcji `q(X)` zdefiniowanej w `config.py` w punkcie o zadanych współrzędnych.  
Zapisuje otrzymane wyniki w pliku o nazwie `file-name.csv` w folderze `./data`.  
Wynik zapisywany jest w wierszach w postaci:
`x1, x2, x3, ..., xd, q(X)`
#### Użycie:
`generate_points.py [-n N] [-d D] [-b BOTTOM] [-t TOP] file-name`
- `N` - liczba punktów do wygenerowania
- `D` - wymiarowość punktów
- `BOTTOM` - minimalna współrzędna generowanych punktów
- `TOP` - maksymalna współrzędna generowanych punktów
- `file-name` - nazwa pliku do którego mają zostać zapisane wyniki generacji

Aby dowiedzieć się o użyciu modułu generującego punkty użyj komendy:
 `python3 generate_points.py -h`

### Connect-dots
Wczytuje informacje o punktach z pliku `file-name.csv` z katalogu `./data`  
Oblicza punkty środkowe zbioru wczytanych punktów powstałe w wyniku iteracyjnego odrzucania punktu o najniższej wartości funkcji celu.
Przewiduje pozycję optimum przy użyciu regresji liniowej oraz przy użyciu uśredniania punktów środkowych.
Rysuje wykresy, przedstawiające błąd predykcji.
Wszystkie wygenerowane wykresy zapisywane są do folderu `./plots`  
#### Użycie:
 `python3 connect_dots.py file-name`
 
 Aby dowiedzieć się więcej użyj komendy:
 `python3 connect-dots.py -h`
