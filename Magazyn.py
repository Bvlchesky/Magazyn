import streamlit as st

# --- Konfiguracja i Inicjalizacja Danych ---

# Inicjalizacja listy towarów w sesji stanu, jeśli jeszcze nie istnieje
if 'towary' not in st.session_state:
    st.session_state.towary = [] # Pusta lista do przechowywania nazw towarów

def dodaj_towar(nazwa):
    """Dodaje nowy towar do listy."""
    if nazwa and nazwa.strip() not in st.session_state.towary:
        st.session_state.towary.append(nazwa.strip())
        st.success(f"Dodano towar: **{nazwa.strip()}**")
    elif nazwa.strip() in st.session_state.towary:
        st.warning("Ten towar już jest na liście!")
    else:
        st.error("Nazwa towaru nie może być pusta.")

def usun_towar(nazwa):
    """Usuwa towar z listy."""
    try:
        st.session_state.towary.remove(nazwa)
        st.info(f"Usunięto towar: **{nazwa}**")
    except ValueError:
        st.error(f"Błąd: Nie znaleziono towaru **{nazwa}**.")

# --- Interfejs Użytkownika Streamlit ---

st.title("📦 Prosty Magazyn")
st.markdown("### Zarządzanie Towarami (bez zapisu do plików)")

# 1. Dodawanie Towarów
st.header("➕ Dodaj Nowy Towar")
nowy_towar = st.text_input("Nazwa Towaru:", key="input_dodaj")

if st.button("Dodaj do Magazynu"):
    dodaj_towar(nowy_towar)

st.divider()

# 2. Wyświetlanie i Usuwanie Towarów
st.header("📝 Aktualny Stan Magazynu")

if st.session_state.towary:
    st.dataframe({
        'Lp.': list(range(1, len(st.session_state.towary) + 1)),
        'Nazwa Towaru': st.session_state.towary
    }, hide_index=True)

    st.subheader("➖ Usuń Towar")
    # Tworzenie listy rozwijanej z aktualnymi towarami
    towar_do_usuniecia = st.selectbox(
        "Wybierz towar do usunięcia:",
        options=st.session_state.towary,
        key="select_usun"
    )

    if st.button("Usuń Wybrany Towar"):
        usun_towar(towar_do_usuniecia)
else:
    st.info("Magazyn jest pusty. Dodaj pierwszy towar!")

# Oczyszczenie pola tekstowego po dodaniu (nie jest obowiązkowe, ale poprawia UX)
# Streamlit automatycznie resetuje widgety, gdy skrypt się uruchamia od nowa,
# więc to jest bardziej demonstracyjne.
