# Telegram Scraper Tool

🚀 A fully automated tool to scrape Telegram members and add/invite them to groups or channels using multiple accounts.

### Features
- ✅ Scrape members from public/private groups
- ✅ Add scraped users to your group
- ✅ Invite scraped users to channels
- ✅ Multi-session support
- ✅ Random delay & flood control

### Usage

```bash
python3 scraper.py
python3 adder.py
python3 invite.py

✅ Termux / Linux-এ তোমার টুল ইনস্টল ও চালানোর পুরো প্রক্রিয়া
🔧 STEP 1: প্রাথমিক Setup (Termux/Linux)
bash
Copy
Edit
pkg update && pkg upgrade -y
pkg install git python -y
❗ Termux এ প্রথমবার Python ইনস্টল না থাকলে এটা করতেই হবে।

🔧 STEP 2: তোমার টুল ক্লোন করো GitHub থেকে
bash
Copy
Edit
git clone https://github.com/XD4RK-W4RR10R/telegram-scraper-tool.git
cd telegram-scraper-tool
🔧 STEP 3: Python dependency ইনস্টল করো
bash
Copy
Edit
pip install --upgrade pip
pip install -r requirements.txt
🧠 যদি কখনো pip error দেয়, এই কমান্ড চালাও:

bash
Copy
Edit
python -m ensurepip --upgrade
🔧 STEP 4: config.py ফাইল এডিট করো
bash
Copy
Edit
nano config.py
এখানে নিচের মতো করে তোমার info বসাও:

python
Copy
Edit
API_ID = 1234567  # তোমার Telegram API ID
API_HASH = 'your_api_hash'  # তোমার API Hash
GROUP = 'https://t.me/targetgroup'  # Target group link (scraping)
CHANNEL = 'https://t.me/yourchannel'  # Channel invite এর জন্য
SESSION_FOLDER = 'sessions'  # session dir
save করতে: CTRL + X ➤ Y ➤ ENTER

🔧 STEP 5: Session ফাইল তৈরি করো (login)
bash
Copy
Edit
python scraper.py
প্রথমবার চালালে Telegram login চাবে (phone number, code etc) – সেগুলো দাও।

🔧 STEP 6: Scrape → Add → Invite Commands
bash
Copy
Edit
# Group থেকে Member Scrape
python scraper.py

# Scraped User দের Group এ Add করা
python adder.py

# Scraped User দের Channel এ Auto Invite করা
python invite.py
✅ Success! এখন তুমি তোমার Tools কে পুরোপুরি চালাতে পারো Termux বা Linux এ 💻
⚠️ যদি No module named telethon বা অন্য error আসে:
bash
Copy
Edit
pip install telethon pandas
🔁 Extra (Multiple Sessions)
একাধিক account ব্যবহার করতে চাইলে sessions/ ফোল্ডারে নতুন সেশন ফাইল বানাও, যেমন:

bash
Copy
Edit
cp sessions/your.session sessions/your2.session
