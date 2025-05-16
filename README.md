# Discord Server Backup Bot

[![Stars](https://img.shields.io/github/stars/highmark-31/discord-server-backup-bot?style=social)](https://github.com/highmark-31/discord-server-backup-bot/stargazers)

**Discord Server Backup Bot** is a powerful Discord bot designed for server administrators to easily perform complete backups of their server’s messages, media, emojis, roles, member data, and general server information—all automated and neatly organized.

---

## 📋 Key Features

* Full backup of text messages including attachments (images, videos, files)
* Saves custom server emojis
* Exports a complete member list with roles, IDs, and important dates
* Saves server roles and general server info (name, ID, owner)
* Dynamic progress bar updating every 2 seconds during backup
* Final embed with credits and links to Trustpilot review and GitHub repo
* Well-organized backup folders and files for easy browsing

---

## 🚀 How to Use

1. **Invite the bot** to your Discord server with Administrator permissions and enable necessary intents (especially *Server Members Intent*).
2. Run the bot by replacing `YOUR_TOKEN_HERE` with your bot’s token.
3. Type the command in any text channel to start the backup:

   ```
   !backup
   ```
4. The bot will create a backup folder containing all server data and show progress updates directly in the chat message.
5. Once complete, an embed message will display credits and politely ask for a review on [Trustpilot](https://www.trustpilot.com/review/highmark.it) and a ⭐ on the [GitHub repo](https://github.com/highmark-31/discord-server-backup-bot).

---

## 📂 Backup Folder Structure

```
backup_ServerName_YYYYMMDD_HHMMSS/
├── server_info.txt
├── roles.txt
├── member_list.txt
├── emoji/
│   └── emoji1.png, emoji2.gif ...
├── logs/
│   └── channel_name1.txt ...
├── media/
│   └── channel_name1/
│       └── file1.jpg, file2.mp4 ...
```

---

## ⚙️ Requirements

* Python 3.8+
* `discord.py` library (v2.x recommended)
* Administrator permissions on your Discord server
* Intents enabled in the [Discord Developer Portal](https://discord.com/developers/applications):

  * Server Members Intent
  * Message Content Intent

---

## 🔧 Installation

```bash
pip install -U discord.py
```

---

## 📄 License

This project is distributed under a **custom license** that allows usage and modification **only if original credits to Highmark.it remain intact**. See the `LICENSE` file for details.

---

## 🙏 Credits & Feedback

If you find this bot useful, please consider leaving a review on [Trustpilot](https://www.trustpilot.com/review/highmark.it) and giving a ⭐ to our [GitHub repo](https://github.com/highmark-31/backup-server-discord-bot)!

---

## 📞 Contact

Official Website: [https://highmark.it](https://highmark.it)
GitHub: [https://github.com/highmark-31/backup-server-discord-bot](https://github.com/highmark-31/discord-server-backup-bot)

---

## Command

```bash
!backup
```

