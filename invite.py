import asyncio
import pandas as pd
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from session_manager import create_client
from config import TARGET_CHANNEL
from utils.delay import random_sleep
from utils.logger import log_info, log_error

async def invite_members():
    client = create_client('invite_session')
    await client.start()

    try:
        df = pd.read_csv('data/members.csv')
    except FileNotFoundError:
        print("[!] members.csv ফাইল খুঁজে পাওয়া যায়নি!")
        return

    added = []
    failed = []

    for index, row in df.iterrows():
        try:
            user = await client.get_entity(row['id'])
            await client(InviteToChannelRequest(
                channel=TARGET_CHANNEL,
                users=[user]
            ))
            print(f"[+] Invited {row['username']} to channel.")
            log_info(f"Invited {row['username']} to channel.")
            added.append(row['username'])
            random_sleep(20, 40)  # delay to avoid flood

        except PeerFloodError:
            print("[!] Flood error. Script থামানো হচ্ছে...")
            log_error("PeerFloodError: Stopped invitation.")
            break

        except UserPrivacyRestrictedError:
            print(f"[!] Privacy setting block করেছে: {row['username']}")
            log_error(f"Privacy error: {row['username']}")
            failed.append(row['username'])

        except Exception as e:
            print(f"[!] Failed to invite {row['username']}: {e}")
            log_error(f"Error inviting {row['username']}: {e}")
            failed.append(row['username'])

    # সেভ করা হচ্ছে
    with open('data/added.txt', 'a') as f:
        for user in added:
            f.write(user + '\n')

    with open('data/failed.txt', 'a') as f:
        for user in failed:
            f.write(user + '\n')

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(invite_members())
