import asyncio
import pandas as pd
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from session_manager import create_client
from config import TARGET_GROUP
from utils.delay import random_sleep
from utils.logger import log_info, log_error

async def scrape_members():
    client = create_client('scraper_session')
    await client.start()

    offset = 0
    limit = 100
    all_participants = []

    while True:
        try:
            participants = await client(GetParticipantsRequest(
                channel=TARGET_GROUP,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))

            if not participants.users:
                break

            all_participants.extend(participants.users)
            offset += len(participants.users)

            log_info(f"Scraped {len(all_participants)} members so far.")
            random_sleep(2, 5)

        except FloodWaitError as e:
            log_error(f"Flood wait error: sleeping for {e.seconds} seconds")
            await asyncio.sleep(e.seconds)

        except Exception as e:
            log_error(f"Error during scraping: {str(e)}")
            break

    users_data = []
    for user in all_participants:
        users_data.append({
            'id': user.id,
            'username': user.username or '',
            'access_hash': user.access_hash,
            'name': (user.first_name or '') + ' ' + (user.last_name or '')
        })

    df = pd.DataFrame(users_data)
    df.to_csv('data/members.csv', index=False)
    log_info(f"Total {len(users_data)} members scraped.")
    print(f"[+] Scraped {len(users_data)} members.")

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(scrape_members())
