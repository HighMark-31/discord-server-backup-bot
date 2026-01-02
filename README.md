<div align="center">

# 🎯 Discord Server Backup Bot
</div>
<div align="center">

[![Stars](https://img.shields.io/github/stars/HighMark-31/discord-server-backup-bot?style=for-the-badge&logo=github&color=FFD700)](https://github.com/HighMark-31/discord-server-backup-bot/stargazers)
[![License](https://img.shields.io/badge/License-Custom-red?style=for-the-badge)](./LICENSE)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=HighMark-31.discord-server-backup-bot&style=for-the-badge)

### 🚀 **VERSION 2.0 - MAJOR UPDATE RELEASED!**

**Complete Server Archival with Interactive Viewer & Multiple Export Formats**

[Features](#-key-features) • [What's New in v2.0](#-whats-new-in-version-20) • [Quick Start](#-quick-start) • [BackupViewer](#-backupviewer) • [Commands](#-commands-reference)

</div>

---

## 📌 About

**Discord Server Backup Bot** is a powerful, fully-featured Discord bot designed for server administrators who need complete, reliable backups of their community data. With v2.0, we've revolutionized how you archive, view, and restore server information.

✨ **Go beyond simple backups** - Save everything: messages, embeds, roles, members, emojis, and media. Then explore it all with our beautiful interactive viewer.

---

## 💎 Key Features

### Original Features
- ✅ **Full message backup** including attachments (images, videos, files)
- ✅ **Custom emoji preservation** - Save all custom server emojis
- ✅ **Complete member export** - Roles, IDs, join dates, and more
- ✅ **Server configuration backup** - Roles, channels, and server info
- ✅ **Real-time progress** - Live progress bar every 2 seconds
- ✅ **Well-organized structure** - Easy-to-browse backup folders

### 🎉 **NEW IN v2.0** - Game-Changing Features

#### 🔄 **Dual Export Formats**
- **JSON Format** - Structured data perfect for embeds, reactions, and rich content
- **Database Format**  - Optimized for massive servers with millions of messages
- **TXT Format**  - Human-readable, universal compatibility

#### **Smart Backup Modes**
- **FULL Mode** - Complete everything: messages, embeds, reactions, attachments, metadata, roles, permissions
- **FAST Mode** - Quick backup of essentials (messages + basic data, no embeds)

#### 👀 **BackupViewer - The Game Changer**
> **Browse your backups exactly like Discord!** Open `BackupViewer.html` in any browser and explore your server backups with a beautiful Discord-like interface. Perfect for previewing and auditing your data.

-  **Discord-like UI** - Familiar interface that feels native
-  **Easy Navigation** - Browse channels and messages intuitively  
-  **Search & Filter** - Find exactly what you're looking for
-  **Rich Preview** - View embeds, media, and metadata

#### 🔐 **Selective Restoration**
- **!restorebackup** - Bring your server back to its former glory
- Restore messages, embeds, roles, permissions, and configuration
- Only works with v2.0+ backups (version guaranteed)

#### 📝 **Embed Support**
- Full Discord embed backup and viewing
- Rich content preservation (colors, fields, thumbnails, images)
- Perfect embed restoration

---

## 🎯 What's New in Version 2.0

| Feature | Before | After |
|---------|--------|-------|
| **Export Formats** | Text Only | JSON, Database, Text |
| **Backup Modes** | All-or-nothing | Full or Fast Smart Modes |
| **Embed Support** | ❌ Not supported | ✅ Complete embed backup |
| **Data Viewer** | ❌ Manual file browsing | ✅ **BackupViewer.html** interactive UI |
| **Restore Option** | ❌ Not available | ✅ **!restorebackup command** |
| **Metadata** | Basic |  Comprehensive backup_metadata.json |
| **Speed** | Single mode |  Fast mode for quick saves |

---

## 🚀 Quick Start

### 1️⃣ **Installation & Setup**

```bash
# Install dependencies
pip install -U discord.py

# Replace TOKEN with your bot token in bot.py and run
python bot.py
```

### 2️⃣ **Invite to Your Server**
- Invite with **Administrator** permissions
- Enable **Server Members Intent** and **Message Content Intent** in [Developer Portal](https://discord.com/developers/applications)

### 3️⃣ **Run Your First Backup**

```
!backup
```

💾 *Boom! Your server is now backed up.*

---

## 📊 Commands Reference

### **Backup Command**

```
!backup [format] [mode]
```

#### **Parameters:**

**Format** (optional - default: `txt`)
```
json          Structured JSON format - best for embeds & metadata
db            Database format - optimized for huge servers  
txt           Human-readable text - universal compatibility
```

**Mode** (optional - default: `full`)
```
full          Complete backup: ALL messages, embeds, attachments, metadata, roles
fast          Quick backup: Messages & essentials only (no embeds, ~60% faster)
```

#### **Examples:**
```bash
!backup                    # Full backup in TXT format (safest default)
!backup json               # Full backup in JSON (best for embeds)
!backup db                 # Database format, full mode (large servers)
!backup json fast          # Quick JSON backup (speed priority)
!backup txt full           # Complete text backup (maximum data)
```

#### **What Gets Backed Up:**
- **Full Mode (`full`)** ✨
  - All messages with complete metadata
  - Discord embeds, reactions, mentions
  - All attachments and media files
  - Member list with roles and join dates
  - Server configuration and permissions
  - Emojis and server settings

- **Fast Mode (`fast`)** ⚡
  - All messages and basic metadata
  - Member information
  - Server structure
  -  *Skips: Embeds, detailed metadata, heavy processing*

---

### **Restore Command** (v2.0+)

```
!restorebackup
```

**Requirements:**
- Backup folder must exist in the bot's directory
- Backup created with **v2.0 or later**
- Bot needs appropriate channel permissions

**What Can Be Restored:**
- 📨 Messages and conversation history
- 🎨 Embeds and rich content
- 📁 Attachments and media files
- 👥 Roles and member permissions
- ⚙️ Server configuration

---

## 👀 BackupViewer - Interactive Backup Explorer

### What is BackupViewer?

**The ultimate tool for exploring your Discord backups.** Open `BackupViewer.html` in any web browser and experience your server data with a Discord-like interface.

### How to Use:

1. **Locate your backup folder**
   - Created by the bot as `backup_ServerName_YYYYMMDD_HHMMSS/`

2. **Open BackupViewer.html**
   - Double-click or open in your browser
   - Select your backup folder from the prompt

3. **Explore Your Data**
   - Browse channels like in Discord
   - View messages with full formatting
   - See embeds, images, and media
   - Search for specific content
   - Review member information

### Features:
- 🎨 **Beautiful UI** - Matches Discord's design language
- 📱 **Responsive** - Works on desktop, tablet, mobile  
- 🔍 **Powerful Search** - Find messages, members, content
- 📊 **Data Preview** - Full embed and attachment rendering
- 💾 **No Upload Required** - Everything stays local
- 🚀 **Fast** - Instant access to your backup data

---

## 📂 Backup Folder Structure

```
backup_ServerName_YYYYMMDD_HHMMSS/
│
├── 📄 server_info.txt              Server name, ID, owner, settings
├── 📄 roles.txt                    All server roles and permissions
├── 📄 member_list.txt              Complete member list with data
├── 📋 backup_metadata.json         [v2.0] Format info, mode, timestamp
│
├── 📁 emoji/
│   ├── custom_emoji1.png
│   └── custom_emoji2.gif
│
├── 📁 logs/                        [v2.0] New structure for messages
│   ├── general.txt
│   ├── announcements.txt
│   └── random.txt
│
├── 📁 media/                       Attachments organized by channel
│   ├── general/
│   │   ├── image1.jpg
│   │   └── video.mp4
│   └── announcements/
│
└── 📁 embeds/                      [v2.0] NEW! Discord embed data
    ├── general_embeds.json         Embed objects with full metadata
    ├── announcements_embeds.json   Colors, fields, thumbnails, etc
    └── random_embeds.json
```

---

## ⚙️ Technical Requirements

- **Python** 3.8 or higher
- **discord.py** v2.x (latest recommended)
- **Administrator permissions** on target Discord server
- **Intents enabled**:
  - ✅ Server Members Intent
  - ✅ Message Content Intent

---

## 🛠️ Installation

```bash
# Clone or download the repository
git clone https://github.com/HighMark-31/discord-server-backup-bot.git
cd discord-server-backup-bot

# Install Python dependencies
pip install -U discord.py

# Configure your bot token in bot.py
# Then run:
python bot.py
```

---

## 📝 Version Comparison

### v1.0
- Basic message backup
- Text output only
- No viewer tool
- No restore function

### ✨ v2.0 (CURRENT)
- 🎯 Multiple export formats (JSON, DB, TXT)
- ⚡ Smart backup modes (Full, Fast)
- 👀 Interactive BackupViewer with Discord-like UI
- 🔄 Restore functionality
- 📝 Full embed support
- 📊 Enhanced metadata
- 🚀 Better performance and organization

---

## 📄 License

This project is distributed under a **custom license** that allows usage and modification **only if original credits to Highmark.it remain intact**. 

See the `LICENSE` file for full details.

---

## 🙌 Support & Feedback

Love the bot? Show your support!

-  **Star this repo** on GitHub
-  **Leave a review** on [Trustpilot](https://www.trustpilot.com/review/highmark.it)
-  **Report bugs** via GitHub Issues
-  **Suggest features** in Discussions

---

## 📞 Contact & Links

| Platform | Link |
|----------|------|
|  **Website** | [https://highmark.it](https://highmark.it) |
|  **GitHub** | [HighMark-31/discord-server-backup-bot](https://github.com/HighMark-31/discord-server-backup-bot/) |
|  **Review** | [Trustpilot](https://www.trustpilot.com/review/highmark.it) |

---

<div align="center">

### Made with ❤️ by HighMark

**v2.0 - The Ultimate Discord Server Archival Solution**

[Back to Top](#-discord-server-backup-bot)

</div>
