# Projekt: Filmy z Ostatnich 24 Godzin na YouTube

Projekt umożliwia automatyczne pobieranie listy nowych filmów opublikowanych na kanałach YouTube w ciągu ostatnich 24 godzin. Skrypt obsługuje wiele kanałów, wyodrębnia czas trwania filmów, ich tytuły oraz generuje bezpośrednie linki do filmów.

---

# Project: Recent Videos from the Last 24 Hours on YouTube

This project automates the retrieval of a list of new videos published on YouTube channels within the last 24 hours. The script supports multiple channels, extracts video durations, titles, and generates direct links to the videos.

---

## Spis treści / Table of Contents

- [Opis / Description](#opis--description)
- [Wymagania / Requirements](#wymagania--requirements)
- [Instalacja / Installation](#instalacja--installation)
- [Użycie / Usage](#użycie--usage)
- [Zaawansowane funkcje / Advanced Features](#zaawansowane-funkcje--advanced-features)
- [Contributing](#contributing)
- [Licencja / License](#licencja--license)

---

## Opis / Description

### [PL]
Skrypt w Pythonie umożliwia:
1. Pobieranie listy nowych filmów z kanałów YouTube w ciągu ostatnich 24 godzin.
2. Wyświetlanie tytułów, długości i linków do filmów.
3. Obsługę wielu kanałów zapisanych w pliku `kanaly_youtube.txt`.

### [EN]
The Python script enables:
1. Retrieving a list of new videos from YouTube channels within the last 24 hours.
2. Displaying video titles, durations, and links.
3. Supporting multiple channels listed in the `kanaly_youtube.txt` file.

---

## Wymagania / Requirements

- Python 3.x
- Biblioteki Python:
  - `google-api-python-client`
  - `isodate`
- Klucz API YouTube Data API v3

---

## Instalacja / Installation

1. **Klonowanie repozytorium / Clone the repository**

   ```bash
   git clone https://github.com/radektv/youtube-ostatnie24godziny.git
   cd youtube-ostatnie24godziny
   ```

2. **Instalacja zależności / Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Przygotowanie plików / Prepare files**

   - Utwórz plik `kanaly_youtube.txt` z linkami do kanałów YouTube w formacie:

     ```plaintext
     https://www.youtube.com/channel/UCxxxxxx
     https://www.youtube.com/channel/UCyyyyyy
     ```

   - Podaj swój klucz API w pliku `youtube24h.py` (zamień `TWOJ_KLUCZ_API` na swój klucz API).

4. **Tworzenie klucza API YouTube / Creating a YouTube API Key**

   - Zaloguj się do [Google Cloud Console](https://console.cloud.google.com/).
   - Utwórz nowy projekt lub wybierz istniejący.
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
