# Poe Discord Bot

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Discord.py](https://img.shields.io/badge/discord.py-1.7.3-yellow?style=for-the-badge)

Poe Bot is a multi-purpose Discord bot designed for server moderation, user engagement, and entertainment.

---

## 🚀 Features

### Moderation
* **Automated Filtering:** Real-time detection and deletion of offensive language and external advertisement links.
* **Administrative Controls:** Integrated commands for banning, kicking, muting, and managing user roles.
* **Server Setup:** Configurable welcome channels and automated role assignment (Auto-role) upon member join.

### Entertainment & Engagement
* **Interactive Commands:** A wide array of social interaction commands including hugs, slaps, and roleplay actions.
* **Leveling System:** An automated experience (XP) and leveling mechanism that tracks user activity across the server.
* **Dynamic Visuals:** Generates dynamic welcome images and rank cards using `Pillow` (PIL) for personalized user feedback.

### General Utilities
* **Currency Tracking:** Real-time USD to TRY conversion.
* **Translation:** Multi-language text translation support.
* **User Analytics:** Detailed insight into member account creation dates, join dates, and rank progression.

---

## 🏗️ Technical Architecture

* **Core:** Python 3.x with `discord.py`.
* **Data Persistence:** Persistent storage using JSON-based data structures for user profiles, experience points, and server configurations.
* **Image Processing:** Dynamic generation of status cards via `Pillow` (PIL) library.
* **Scraping:** `BeautifulSoup` and `requests` for fetching real-time financial data.

---

## ⚙️ Project Structure

The project maintains a modular structure to separate logic from configuration:

* `main.py`: Primary bot entry point and command handler.
* `sunucuverileri.py`: Server-side configuration management module.
* `veriler.py`: Core logic for XP calculations and leveling metrics.
* `config/`: Configuration directory containing persistent data files.
* `users.json` / `sunucular.json`: Databases for tracking member activity and server settings.






