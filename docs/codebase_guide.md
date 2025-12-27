# 🎬 CineMatch AI: A Beginner's Guide

Welcome! If you're new to Python or coding in general, this guide is for you. We’ll explain how CineMatch AI works using simple analogies instead of technical jargon.

---

## 🏛️ The Big Picture: "The Gourmet Librarian"

Imagine you’re building a **Super Library** that doesn't just find books by title, but understands *how they make you feel*.

1. **The Researcher (Scraper):** Goes out to the internet (IMDb) and takes photos of every book review they can find.
2. **The Translator (Processor):** Reads those reviews and translates them into a secret code (Numbers) that a computer can search through very quickly.
3. **The Vault (Vector DB):** Stores all those codes in a giant, organized cabinet.
4. **The Librarian (Recommendation Engine):** You walk in and say, "I want something dark but hopeful." The librarian understands your vibe, checks the vault, and brings you the perfect movie.

---

## 🛤️ The Data Journey (Step-by-Step)

How does a movie review become a recommendation?

### Step 1: Gathering (Scraping)
We use a tool called **`bulk_runner.py`**. 
- **What it does:** It visits IMDb, looks up a list of movies, and downloads their details (Title, Year) and what people said about them (Reviews).
- **Result:** You get local files (JSON and CSV) sitting in your `data/` folder.

### Step 2: Cleaning & Coding (Processing)
We use a tool called **`pipeline.py`**.
- **Cleaning:** It removes "junk" words (like "the", "a", "is") so we only keep the important stuff.
- **Coding (Embedding):** It turns text like *"This movie was terrifying and brilliant"* into a long list of numbers. In the computer world, similar "vibes" have similar numbers.
- **Result:** These specific numbers are saved in a **Vector Database** (ChromaDB).

### Step 3: Finding (Recommendation)
When you ask for a movie, the system uses **`recommendation.py`**.
- **Search:** It turns *your* question into numbers too!
- **Matching:** It looks inside the Vector Database to find movies whose "review numbers" are closest to "your question numbers."
- **Result:** It gives you a ranked list of the best matches.

---

## 🗺️ The "Tour Guide" (File Map)

Here is where the important "brains" of the project live:

| Folder / File | Simplified Purpose |
| :--- | :--- |
| `src/cinematch/scraper/` | The "Gathering" tools. This is where we talk to IMDb. |
| `src/cinematch/processing/` | The "Cleaning" tools. This turns text into numbers. |
| `src/cinematch/core/` | The "Thinking" tools. This is where the actual recommendations happen. |
| `src/cinematch/utils/` | Little "Helper" tools (like checking if the database is on). |
| `tests/` | The "Sanity Check" area. We run scripts here to make sure things aren't broken. |

---

## 📖 Beginner's Glossary

- **Scraping:** Automating a browser to "copy-paste" info from a website into your computer.
- **JSON / CSV:** Just fancy names for text files that store data (like a mini spreadsheet).
- **Embedding:** Turning a sentence into a mathematical "coordinate" so the computer can understand its meaning.
- **Vector Database:** A special kind of storage that is really good at finding things based on "meaning" rather than just keywords.
- **Pipeline:** A series of steps that happen automatically, one after another.

---

## 🚦 How to "Run" Things
Even if you don't code, you might see commands like this:
- `python -m cinematch.scraper.bulk_runner`: "Hey Researcher, go get some movies!"
- `python -m cinematch.processing.pipeline --movie "The Matrix"`: "Hey Translator, turn The Matrix reviews into codes!"
