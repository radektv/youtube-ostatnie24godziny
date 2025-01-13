# Projekt: Filmy z Ostatnich 24 Godzin na YouTube
   - Przejdź do zakładki „APIs & Services” > „Enable APIs and Services”.
   - Wyszukaj „YouTube Data API v3” i kliknij „Enable”.
   - Przejdź do „Credentials” i kliknij „Create Credentials”.
   - Wybierz „API Key” i skopiuj wygenerowany klucz.

   Umieść klucz API w pliku `youtube24h.py`:

   ```python
   API_KEY = 'TWOJ_KLUCZ_API'
   ```

---

## Użycie / Usage

1. **Uruchomienie skryptu / Run the script**

   ```bash
   python youtube24h.py
   ```

2. **Przykładowy wynik / Example output**

   ```plaintext
   Sprawdzam filmy z kanału o ID: UCxxxxxx
   Kanał: Example Channel
   Title: Example Video 1
   Długość filmu: 5 minut 23 sekund
   URL: https://www.youtube.com/watch?v=abcd1234
   ------
   Title: Example Video 2
   Długość filmu: 2 minuty 15 sekund
   URL: https://www.youtube.com/watch?v=wxyz5678
   ------
   Podsumowanie: brak filmów w ostatnich 24 godzinach
   ```

---

## Zaawansowane funkcje / Advanced Features

- **Obsługa wielu kanałów / Multiple channel support**
  Skrypt obsługuje dowolną liczbę kanałów zapisanych w pliku `kanaly_youtube.txt`.

- **Czas trwania filmów / Video duration**
  Skrypt automatycznie konwertuje czas trwania filmu z formatu ISO 8601 na minutach i sekundach.

---

## Contributing

If you wish to contribute, please create a pull request. Ensure your code adheres to the style guidelines and includes tests if necessary.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Licencja / License

This project is licensed under the **MIT License.**
