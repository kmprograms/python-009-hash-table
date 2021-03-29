# ==================================================================================================
# ==================================================================================================
# Co to jest HASH FUNCTION?

# Funkcja ktora przyporzadkowuje dowolnej wartosci wejsciowej ( np. napisowi lub liczbie ) wartosc
# o stalym rozmiarze. Taka wartosc nazywana jest HASH VALUE.

# ==================================================================================================
# ==================================================================================================
# Jakie cechy posiada HASH FUNCTION?

# a. Jest szybka

# b. Jest deterministyczna czyli za kazdym razem kiedy podasz ten sam argument otrzymasz taka sama wartosc

# c. Niezaleznie od wielkosci danych wejsciowych zawsze zwraca wartosci o konkretnej ustalonej wielkosci

# d. Czesto hash function pozwala dla podanego argumentu wyliczyc wartosc hash ale juz nie pozwala
#    dokonac przeksztalcenia w druga strone czyli z hash value nie potrafi odzyskac napisu - nie musi
#    byc tak zawsze, ale czesto tak wlasnie jest zaimplementowana hash function. Wlasciwosc jest
#    przydatna w kryptografi, przy szyfrowaniu hasel.


# ==================================================================================================
# ==================================================================================================

# Python posiada wbudowana funkcje hash().
# Generuje ona hash value dla podanego jako argument obiektu.
# Wewnatrz funkcja ta odwoluje sie do funkcji __hash__() obiektu.
# Dlatego jezeli chcesz zeby obiekt Twojej klasy byl hashtable to musisz
# mu taka funkcje dostarczyc.

# Ponizej kilka przykladow, ktore pokazuja wykorzystanie funkcji hash.
print(hash(1))          # hash value dla integer-a to ta sama wartosc
print(hash(1.0))        # float o calkowitej wartosc tez ma taki sam hash value jak jego wartosc
# Dwa powyzsze przyklady pokazuja ze masz dwa rozne obiekty a wartosc hash jest taka sama. Czyli nie uda
# sie na podstawie hash odtworzyc obiektu, ktory byl hashowany.

# Kolejna ciekawostka jest zachowanie hash w stosunku do wartosci zmiennoprzecinkowych.
h1 = hash(1.5)
print(h1)
print(hash(h1))
print(hash(h1) == hash(1.5))  # Taki sam hash value dla liczby wejsciowej oraz jej wartosci hash
# To pokazuje ze moze sie zdarzyc ze dla dwoch roznych obiektow wejsciowych mozemy uzyskac taka sama
# wartosc hash i taka sytuacje nazywamy kolizja

# W przypadku napisow mamy kolejna wlasciwosc
# Kazdorazowe uruchomienie skrytpu powoduje ze masz calkiem inna wartosc hash dla napisu
# W przypadku napisow przed wyliczaniem wartosci hash losowana jest pewna wartosc (tzw. salt)
# o ktora napis jest modyfikowany i dopiero tak zmodyfikowany napis jest hashowany. Losowana
# wartosc jest przy kazdym uruchomieniu skryptu inna i to daje rozny wynik. Mozna zmienic to
# zachowanie za pomoca zmiennej srodowiskowej PYTHONHASHSEED. Taka dodatkowa operacja ma na celu
# zwiekszenie bezpieczenstwa. Kiedy przechowujemy haslo ktore zostalo wczesniej zahashowane
# to podczas potencjalnego ataku istnieje mozliwosc jego odszyfrowania na podstawie ogromnej
# ilosci innych szyfrowanych do tej pory napisow. Wprowadzenie losowosci do procesu szyfrowania
# utrudnia ten proces.
print('STR:')
print(hash('ala'))

# ==================================================================================================
# ==================================================================================================
# Jakie typy w Python sa hashtable?

# a. Typy immutable w Python sa hashtable

# b. Kiedy uzywasz sekwencje typow immutable np sekwencje tuple to ona tez jest hashtable

# c. Kiedy starsz sie uzyskac hasv value z typu ktory nie jest hashtable dostajesz
#    wyjatek TypeError
#    W przykladzie ponizej lista nie jest hashtable dlatego bedzie wyjatek
#    hash(['a', 'l', 'a'])

# d. Kazdy obiekt w Python jest hashtable poniewaz domyslnie jego wartosc hash
#    jest wyznaczana na podstawie jego id. To oznacza ze dwa rozne obiekty tej
#    samej klasy musza miec rozne hash values


class Product:
    name: ''
    quantity: 0


print('OBJECT:')
prod1 = Product()
prod2 = Product()
print(id(prod1))
print(id(prod2))
print(hash(prod1))
print(hash(prod2))

# Mozesz zmieniac zachowanie pod katem wyliczania hash za pomoca napisania w klasie wlasnej
# wersji metody __hash__

# ==================================================================================================
# ==================================================================================================
# Co to jest hash table?

# Jest to kolekcja ktora pozwala przechowywac informacje postaci klucz - wartosc
# W tej kolekcji kazdy klucz musi byc hashtable. Jest tak poniewaz pary
# przechowywane w hashtable sa indeksowane wlasnie za pomoca hash values wyliczanych na
# podstawie kluczy. Takie przechowywanie elementow pozwala na ich bardzo szybkie wyszukiwanie
# wlasnie na podstawie indeksow.

# Pamietaj ze stosujac do wyznaczania hash value wbudowana funkcje hash i tak nie jestes
# w stanie wyeliminowac sytuacji w ktorej dojdzie do kolizji. Mozesz zwiekszac ilosc bucketow
# ktorym przypoarzadkowujesz poszczegolne obiekty, jedna to z drugiej strony spowoduje zwiekszenie
# miejsca w pamieci, ktore potrzebujesz do przechowania hash table. Poza tym zwiekszenie ilosci
# buckets zmniejszy prawdopodobienstow kolizi ale go nie wyeliminuje.

# W jaki sposob rozwiazywac problemy zwiazane z kolizjami?
# Mamy dwa podejscia:

# => open addressing - jezeli pod bucket, ktory wlasnie wyznaczono do przechowania elementu jest juz
#    inny element nalezy wyszukac kolejny bucket, ktory akurat jest wolny
#    Istnieja 3 metody realizujace mechanizm open addressing:

#    -> linear probing    -> hi(x) = (hash(x) + i)  % size_of_hash_table

#    14, 33, 21, 39

#    Wstawiamy 14 do hash table
#    h0(14) = (14 + 0) % 6 = 2
#    0
#    1
#    2 -> 14
#    3
#    4
#    5

#    Wstawiamy 33 do hash table
#    h0(33) = (33 + 0) % 6 = 3
#    0
#    1
#    2 -> 14
#    3 -> 33
#    4
#    5

#    Wstawiamy 21 do hash table
#    h0(21) = (21 + 0) % 6 = 3
#    Poruszamy sie po hash table dopoki nie znajdziemy wolnego bucketa
#    h1(21) = (21 + 1) % 6 = 4
#    0
#    1
#    2 -> 14
#    3 -> 33
#    4 -> 21
#    5

#    Wstawiamy 39 do hash table
#    h0(39) = (39 + 0) % 6 = 3
#    Poruszamy sie po hash table dopoki nie znajdziemy wolnego bucketa
#    h1(39) = (39 + 1) % 6 = 4
#    h2(39) = (39 + 2) % 6 = 5
#    0
#    1
#    2 -> 14
#    3 -> 33
#    4 -> 21
#    5 -> 39

#    Inne sposoby:
#    -> quadratic probing
#    -> double hashing


# => separate chaining - dla konkretnego bucketa tworzysz strukture, np liste, ktora przechowuje
#    obiekty o takiej samej hash value; lista jest przeszukiwana w celu odnalezienia konkretnego
#    elementu


# ==================================================================================================
# ==================================================================================================
# Zastosowanie hash table w Python

# Dictionary - uzywa hash table oraz open addressing do rozwiazywania kolizji.

people_with_hobbies = {
    'ADAM': 'SPORT',
    'EWA': 'MUSIC',
    'TOMASZ': 'SPORT',
    'KASIA': 'BOOKS'
}

print(people_with_hobbies['ADAM'])  # podajesz klucz do uzyskania wartosci
del people_with_hobbies['ADAM']  # tak naprawde w tym momencie nie mamy usuwania elementu
# poniewaz dziala mechanizm oppen addressing - w tym podejsciu zamiast usuwac element
# podstawiana jest pod klucz pewna "dummy value", ktora powoduje ze podczas wyszukiwania
# elementu o takim usunietym kluczu jest on ignorowany ale ciage jest w dictionary - jest to
# wada podejscia open addressing
print(people_with_hobbies)
