# "Hacking Python" – zadania kwalifikacyjne


## Zamieszczanie rozwiązań

Rozwiązania powinieneś wysłać poprzez aplikację warsztatów
([warsztatywww.pl](https://warsztatywww.pl/2021/workshop/depyton/solution/)).
Możesz je wrzucić jako osobne pliki, albo spakowane w archiwum, nie ma
znaczenia. Proszę jednak, abyś pliki tekstowe zapisał w kodowaniu UTF-8.

**Termin**: 15 maja


# Zadanie "hello world" [0 pkt.]

Napisz coś o sobie. Co cię interesuję, czym się zajmujesz, możesz pochwalić się
jakimś swoim projektem. Nie musisz pisać rozprawki, wystarczą 2-3 zdania. Forma
rozwiązania: dowolna.

<!-- Część rzeczy, które będziemy robić, może być zależna od wersji pythona. Upewnij
   - się, że umiesz pobrać/zainstalować dowolną wersję pythona na swoim systemie
   - operacyjnym.
   -
   - Na Windowsie i macOS-ie można np. pobrać installer z
   - [python.org](https://www.python.org). Na Linuxie można np. skorzystać z
   - [`pyenv`](https://github.com/pyenv/pyenv). Ja używam
   - [`asdf`](https://asdf-vm.com/#/) i polecam. :) -->


# Zadanie "obliczenia" [2 pkt.]

https://github.com/MrQubo/wwi2021-quals/tree/master/obliczenia

Za biedny jestem na hosting, więc serwer musisz sobie postawić lokalnie. Możesz
w tym celu skorzystać ze skryptu `setup.sh`. Powinno działać pod WSL, jak będzie
jakiś problem to proszę o kontakt.

Twoim zadaniem jest napisanie skryptu, który zdobędzie flagę (czyli zawartość
pliku `flag.txt`).  Oczywiście nie możesz przeczytać sobie tej flagi z pliku, po
prostu udawaj, że tego pliku tam nie ma. :P Chodzi o to, abyś połączył się z
serwerem (pod adresem `localhost:1337`) i wszedł z nim w interakcję, przy pomocy
napisanego przez ciebie skryptu. Jako rozwiązanie wyślij skrypt **w pythonie
3**, możesz skorzystać z dowolnych, darmowych i otwartoźródłowych, bibliotek.

**Uwaga**: Pliki serwera możesz modyfikować, aby pomóc sobie w klepaniu
rozwiązania. Pamiętaj jednak, że rozwiązanie, które wyślesz, ma działać z
oryginalnymi plikami serwera.

**Hint**: Do komunikacji z serwerem możesz użyć np.
[`socket`](https://docs.python.org/3/library/socket.html#example) bądź
[`pwntools`](https://docs.pwntools.com/en/latest/tubes/sockets.html?highlight=remote#pwnlib.tubes.remote.remote)
(to drugie trzeba najpierw zainstalować, ale IMO jest wygodniejsze w użyciu).


# Zadanie "bajtsy" [2 pkt.]

https://github.com/MrQubo/wwi2021-quals/tree/master/bajtsy

Cel i opis zadania jest taki sam jak w poprzednim zadaniu. Zmieniłem za to numer
portu na `:1338`.


# Zadanie "maszyna" [6 pkt.]

https://github.com/MrQubo/wwi2021-quals/tree/master/maszyna

**Uwaga**: W swoim rozwiązaniu nie zakładaj, że znasz długość flagi. Rozwiązanie
powinno działać dla flagi dowolnej długości.


# Zadanie z * "maszyna2" [5 pkt.]

https://github.com/MrQubo/wwi2021-quals/tree/master/maszyna2

**Hint**: Zaimportować/skopiować klasę Foo do REPL-a, wpisać `Foo.__` i nacisnąć
dwa razy TAB na klawiaturze.


# Kontakt (Jakub Nowak)

Wszelkie pytania, przemyślenia, niejasności i inne zmartwienia skieruj pod
dowolny z poniższych kanałów:

**Email**: j.nowak26+www2021@student.uw.edu.pl

**Telegram**: [@mrqubo](https://t.me/mrqubo)

**Discord**: MrQubo#2852
