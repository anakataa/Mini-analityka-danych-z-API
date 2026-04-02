# Mini-analityka danych z API (Cogitech Task)

## Opis projektu

Prosta i czytelna aplikacja webowa zbudowana w **Pythonie** przy użyciu frameworka **Streamlit**.
Zgodnie z poleceniem, projekt został zrealizowany w sposób modułowy, a kod został podzielony na 3 logiczne sekcje (pobieranie, przetwarzanie, wizualizacja) i udokumentowany w języku angielskim.

**Funkcjonalności:**

1. Pobieranie danych z 4 endpointów publicznego API [JSONPlaceholder](https://jsonplaceholder.typicode.com): `/users`, `/posts`, `/comments` oraz `/todos`.
2. Przetwarzanie danych (Pandas) i wyliczenie 4 metryk, w tym zaawansowanego łączenia danych w celu uzyskania "Top 5 najbardziej komentowanych postów".
3. Wizualizacja wyników w postaci interaktywnych wykresów za pomocą biblioteki **Plotly**.

## 🌐 Demo

Link do działającego dema w chmurze: **[TUTAJ WKLEJ LINK DO STREAMLIT CLOUD PO WDROŻENIU]**

## Zrzut ekranu

![Zrzut ekranu aplikacji](screenshot.png)
_(Aplikacja w działaniu)_

## 🛠 Technologie

- **Python 3.10+**
- **Streamlit** (UI & hosting dema)
- **Pandas** (Przetwarzanie i agregacja danych)
- **Requests** (Pobieranie danych z REST API)
- **Plotly Express** (Interaktywne wykresy słupkowe i kołowe)

## Wykorzystanie AI (Zgodnie z wytycznymi)

Zgodnie z poleceniem w zadaniu, nie używałem AI do wygenerowania gotowego kodu z jednego promptu. Model językowy (ChatGPT) służył mi jako wsparcie w modelu _pair-programming_ krok po kroku:

1. **Pobieranie danych (Caching):** Poprosiłem AI o wskazanie najlepszej praktyki dla Streamlit, aby nie odpytywać API przy każdym kliknięciu. Zastosowałem polecony dekorator `@st.cache_data`.
2. **Przetwarzanie danych (Pandas):** Skonsultowałem z AI optymalny sposób na połączenie (tzw. `merge`) tabeli postów z tabelą komentarzy po kluczu `postId`, aby wydajnie wyliczyć ranking TOP 5 postów.
3. **Wizualizacje (Plotly):** Użyłem AI jako szybkiej dokumentacji, aby dowiedzieć się, jak wymusić konkretne kolory w wykresie kołowym (`color_discrete_map`), by zadania ukończone (True) były zawsze zielone, a nieukończone (False) – czerwone.
4. **Jakość kodu:** Poprosiłem o sprawdzenie moich komentarzy w kodzie i upewnienie się, że podział na sekcje (Part 1, Part 2, Part 3) jest czytelny i zgodny z dobrymi praktykami.
