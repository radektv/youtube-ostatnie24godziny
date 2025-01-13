[root@delik ostatnie24godziny]# cat youtube24h.py
import datetime
import re
from googleapiclient.discovery import build
from isodate import parse_duration  # Biblioteka do parsowania formatu ISO 8601

# Wprowadź swój klucz API
API_KEY = 'TWOJ_KLUCZ_API'

# Inicjalizacja klienta YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

# Określenie czasu sprzed 24 godzin
one_day_ago = datetime.datetime.utcnow() - datetime.timedelta(days=1)
published_after = one_day_ago.isoformat("T") + "Z"  # Format ISO 8601 (UTC)

# Funkcja do wyodrębniania ID kanału z URL (np. https://www.youtube.com/channel/UCxxxxxx)
def extract_channel_id(url):
    match = re.search(r"youtube\.com/channel/([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    return None

# Wczytanie kanałów z pliku kanaly_youtube.txt
def load_channels_from_file(file_path):
    with open(file_path, 'r') as file:
        channels = [line.strip() for line in file.readlines() if line.strip()]
    return channels

# Funkcja do konwersji czasu trwania filmu z formatu ISO 8601 na minutach i sekundach
def format_video_duration(duration):
    parsed_duration = parse_duration(duration)
    minutes = parsed_duration.seconds // 60
    seconds = parsed_duration.seconds % 60
    return f"{minutes} minut {seconds} sekund"

# Funkcja do pobierania filmów z YouTube opublikowanych w ciągu ostatnich 24 godzin
def get_recent_videos_from_channels():
    channels = load_channels_from_file('kanaly_youtube.txt')  # Wczytanie kanałów z pliku

    for url in channels:
        # Pobieranie ID kanału z URL
        channel_id = extract_channel_id(url)

        if channel_id:
            print(f"Sprawdzam filmy z kanału o ID: {channel_id}")

            # Zapytanie do API, by pobrać filmy z tego kanału opublikowane w ciągu ostatnich 24 godzin
            request = youtube.search().list(
                part="snippet",
                channelId=channel_id,  # Filtrujemy po ID kanału
                publishedAfter=published_after,
                type="video",  # Tylko filmy
                order="date",  # Sortowanie według daty
                maxResults=10  # Maksymalna liczba wyników na kanał
            )
            response = request.execute()

            # Pobieranie nazwy kanału
            channel_request = youtube.channels().list(
                part="snippet",
                id=channel_id
            )
            channel_response = channel_request.execute()
            channel_name = channel_response['items'][0]['snippet']['title']

            # Wyświetlanie wyników dla każdego kanału
            if 'items' in response and len(response['items']) > 0:
                print(f"Kanał: {channel_name}")
                for item in response['items']:
                    video_title = item['snippet']['title']
                    video_url = f"https://www.youtube.com/watch?v={item['id']['videoId']}"

                    # Pobieranie czasu trwania filmu
                    video_request = youtube.videos().list(
                        part="contentDetails",
                        id=item['id']['videoId']
                    )
                    video_response = video_request.execute()
                    video_duration = video_response['items'][0]['contentDetails']['duration']
                    formatted_duration = format_video_duration(video_duration)

                    print(f"Title: {video_title}")
                    print(f"Długość filmu: {formatted_duration}")
                    print(f"URL: {video_url}")
                    print("------")
            else:
                print(f"Kanał: {channel_name}")
                print("Podsumowanie: brak filmów w ostatnich 24 godzinach")
            print("\n")
        else:
            print(f"Nieprawidłowy link kanału: {url}")

# Uruchomienie funkcji
get_recent_videos_from_channels()
