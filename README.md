# 🎬 CineMatch AI (IMDb-Driven Recommendation Bot)

> An AI-powered chatbot that recommends movies based on user prompts, built for integration into a streaming platform (e.g., Netflix-like).  
> Data is sourced from IMDb reviews (feature, critics, and users), processed into embeddings, and served through a conversational interface.

---

### 📖 New to the project?
Check out our beginner-friendly **[Codebase Guide](docs/codebase_guide.md)** to understand how everything works under the hood!

---

## � Development Status
**Current Phase:** Phase 1: Planning & Setup  
**Goal:** Initialize project structure and build basic scraping prototypes.

---

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **API Framework:** FastAPI + Uvicorn
- **Vector Database:** ChromaDB
- **ML/Embeddings:** Sentence Transformers (`all-MiniLM-L6-v2`), PyTorch
- **Scraping:** BeautifulSoup4, Requests
- **Frontend:** (Planned) React/Vue.js widget

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- `pip`

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/StarLord1808/CineMatch_AI.git
   cd CineMatch_AI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application (Coming Soon):
   ```bash
   # uvicorn app.main:app --reload
   ```

---

## 📖 Roadmap & Architecture

### 1. Phase 1: Strategy & Architecture Planning
**Goal:** Define the system prompts and high-level data flow.
- [x] Define Prompt Categories (Mood, Vibe, Comparative)
- [x] Design System Architecture

### 2. Phase 2: Data Acquisition Strategy (Scraping)
**Goal:** Build a robust, ethical scraping pipeline.
- **Tools:** `BeautifulSoup4`, `requests` (with rate limiting)
- **Targets:** Metadata (Title, Year, Cast), User Reviews, Critic Reviews.

### 3. Phase 3: Data Processing & Vectorization
**Goal:** Convert raw text into searchable vectors.
- **Cleaning:** Lemmatization, stopword removal.
- **Embedding:** `sentence-transformers` to generate dense vectors.
- **Storage:** ChromaDB local persistence.

### 4. Phase 4: Recommendation Engine Logic
**Goal:** Match user prompts to movie vectors.
- **Search:** Cosine similarity.
- **Re-Ranking:** Diversity filters, availability checks.

### 5. Phase 5: Chatbot Interface
**Goal:** User-facing interaction.
- **Backend:** FastAPI endpoints for `/recommend` and `/chat`.
- **Frontend:** Simple chat widget.

### 6. Phase 6: Deployment
- Docker containerization.
- Cloud deployment (AWS/GCP).

---

## ⚠️ Challenges & Mitigations
- **Scraping Legality:** We strictly respect `robots.txt` and use delays.
- **Cold Start:** Fallback to metadata-based recommendations for new movies.
- **Compute:** Using lightweight models (`MiniLM`) to keep inference fast on CPU.

---

### High-Level System Architecture
```
[IMDb.com] -> [Scraping Engine] -> [Raw Text Data (Reviews)]
[Raw Text Data] -> [Processing Engine] -> [Vector Database]
[User Prompt] -> [Chatbot Interface] -> [Recommendation Engine] -> [Vector DB]
[Recommendation Engine] -> [Ranked Movies] -> [Chatbot Interface] -> [User]
```
