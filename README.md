# Telegram Scraper Tool 🚀

A fast & automated Telegram tool to:
- ✅ Scrape members from public/private groups
- ✅ Add them to your group
- ✅ Invite them to your channel
- ✅ Use multiple accounts with delay & flood control

---

## 📦 Features
- Scrape users from any public/private group
- Add scraped users to any group (public/private)
- Invite scraped users to any channel (public/private)
- Multi-account support (sessions)
- Random delay to avoid flood limits

---

## 🛠 Installation (Termux / Linux)

```bash
pkg update && pkg upgrade -y
pkg install git python -y
git clone https://github.com/YOUR_USERNAME/telegram-scraper.git
cd telegram-scraper
pip install -r requirements.txt

⚙️ Configuration
Edit config.py and set your credentials:

API_ID = 1234567
API_HASH = 'your_api_hash'
SOURCE = 'https://t.me/sourcegroup'        # Group/channel to scrape from
TARGET_GROUP = 'https://t.me/yourgroup'     # Group to add members
CHANNEL = 'https://t.me/yourchannel'        # Channel to invite members
SESSION_FOLDER = 'sessions'
Save with CTRL + X ➤ Y ➤ ENTER

🚀 Usage:

# 1. Login & scrape members
python scraper.py

# 2. Add users to group
python adder.py

# 3. Invite users to channel
python invite.py
✅ All scraped users are saved in data/members.csv
✅ Successful & failed additions logged in added.txt and failed.txt

⚠️ Disclaimer
This tool is for educational purposes only.
Do not use for spam or violate Telegram's Terms of Service.
