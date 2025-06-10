import asyncio
import pandas as pd
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
from session_manager import create_client
from config import TARGET_GROUP
from utils.delay import random_sleep
from utils.logger import log_info, log_error

async def add_members():
    client = create_client('adder_session')
    await client.start()

    df = pd.read_csv('data/members.csv')
    added = []
    failed = []

    for index, row in df.iterrows():
        try:
            user = await client.get_entity(row['id'])
            await client(InviteToChannelRequest(
                channel=TARGET_GROUP,
                users=[user]
            ))
            print(f"[+] Added {row['name']} ({row['username']})")
            log_info(f"Added {row['name']} ({row['username']})")
            added.append(row['username'])
            random_sleep(30, 60)

        except PeerFloodError:
            print("[!] Flood error! Stop adding members now.")
            log_error("PeerFloodError: Stopped adding.")
            break

        except UserPrivacyRestrictedError:
            print(f"[!] Privacy settings blocked adding {row['username']}")
            log_error(f"Privacy restricted: {row['username']}")
            failed.append(row['username'])

        except Exception as e:
            print(f"[!] Failed to add {row['username']}: {str(e)}")
            log_error(f"Failed to add {row['username']}: {str(e)}")
            failed.append(row['username'])

    with open('data/added.txt', 'a') as f:
        for user in added:
            f.write(user + '\n')

    with open('data/failed.txt', 'a') as f:
        for user in failed:
            f.write(user + '\n')

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(add_members())
