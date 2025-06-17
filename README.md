# 🎵 Music Recommender System (Lyrics-Based)

This project is a **Streamlit-powered music recommendation system** that recommends songs based on lyrics similarity. It uses a hybrid approach, combining content-based filtering (from song lyrics and metadata) with popularity-based weighting to suggest tracks similar to the input song.

<p align="center">
  <img src="https://media.giphy.com/media/JxxkWxHOEDrq0/giphy.gif" width="300" alt="Music Gif"/>
</p>

---

## 🔍 Features

- 🎶 Recommend 5 songs similar to the input, based on lyrics and artist metadata.
- 🧠 Uses precomputed similarity matrix (lyrics embeddings).
- 📊 Popularity-aware ranking for improved results.
- 💡 Interactive Streamlit UI.
- 📀 Album covers fetched dynamically using Spotify API.

---

## 🛠 Tech Stack

- **Python 3**
- **Streamlit**
- **Pandas / NumPy**
- **Scikit-learn**
- **Spotipy (Spotify API wrapper)**
- **TF-IDF / Cosine Similarity**
- **Pickle (for model/data storage)**

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app file |
| `data.pkl` | Pickled DataFrame with songs, artists, albums |
| `similarity.pkl` | Pickled similarity matrix (lyrics-based) |
| `README.md` | Project documentation (this file) |

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/lyrics-music-recommender.git
   cd lyrics-music-recommender
