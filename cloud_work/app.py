import streamlit as st
import random

# Page Config
st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎵",
    layout="centered"
)

# Title
st.title("🎵 AI Mood Music Recommender")
st.write("Enter your mood and get songs + quotes!")

# Input
mood = st.text_input("How are you feeling today?")

# Data
happy_songs = [
    "Happy - Pharrell Williams",
    "On Top Of The World - Imagine Dragons",
    "Can't Stop The Feeling - Justin Timberlake"
]

sad_songs = [
    "Fix You - Coldplay",
    "Someone Like You - Adele",
    "Let Her Go - Passenger"
]

angry_songs = [
    "Believer - Imagine Dragons",
    "Numb - Linkin Park",
    "Stronger - Kanye West"
]

relaxed_songs = [
    "Perfect - Ed Sheeran",
    "Photograph - Ed Sheeran",
    "Let It Be - Beatles"
]

quotes = {
    "happy": [
        "Keep smiling 😊",
        "Happiness is contagious!"
    ],
    "sad": [
        "Bad days don’t last forever.",
        "Stay strong 💪"
    ],
    "angry": [
        "Take a deep breath.",
        "Control your emotions."
    ],
    "relaxed": [
        "Peace begins with a smile.",
        "Stay calm and enjoy life."
    ]
}

# Button
if st.button("Recommend"):

    mood = mood.lower()

    if "happy" in mood:

        st.success("You seem HAPPY 😊")

        st.subheader("🎵 Songs")
        for song in happy_songs:
            st.write("•", song)

        st.subheader("💬 Quote")
        st.info(random.choice(quotes["happy"]))

    elif "sad" in mood:

        st.warning("You seem SAD 😔")

        st.subheader("🎵 Songs")
        for song in sad_songs:
            st.write("•", song)

        st.subheader("💬 Quote")
        st.info(random.choice(quotes["sad"]))

    elif "angry" in mood:

        st.error("You seem ANGRY 😠")

        st.subheader("🎵 Songs")
        for song in angry_songs:
            st.write("•", song)

        st.subheader("💬 Quote")
        st.info(random.choice(quotes["angry"]))

    else:

        st.success("You seem RELAXED 😌")

        st.subheader("🎵 Songs")
        for song in relaxed_songs:
            st.write("•", song)

        st.subheader("💬 Quote")
        st.info(random.choice(quotes["relaxed"]))

# Footer
st.markdown("---")
st.caption("Created using Python & Streamlit")