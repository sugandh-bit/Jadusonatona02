<p align="center">
<img src="[https://files.catbox.moe/fobxgt.jpg](https://files.catbox.moe/fobxgt.jpg)" alt="RockyMusicBot Logo" width="500px">
</p>

<h1 align="center">🎵 Rocky Music Bot 🎵</h1>

<p align="center">
  <b>A Powerful Telegram Music Bot to Play Songs in Voice Chats</b>
</p>

<p align="center">
  <a href="https://t.me/ROCKY_UPDATE"><img src="https://img.shields.io/badge/Support%20Channel-blue?style=for-the-badge&logo=telegram&logoColor=white&link=https://t.me/ROCKY_UPDATE" alt="Support Channel"></a>
  <a href="https://t.me/ROCKY_SUPPORTB"><img src="https://img.shields.io/badge/Support%20Group-blue?style=for-the-badge&logo=telegram&logoColor=white" alt="Support Group"></a>
  <a href="https://t.me/MR_ROCKY_TZ"><img src="https://img.shields.io/badge/Owner-purple?style=for-the-badge&logo=telegram&logoColor=white" alt="Owner"></a>
</p>

<p align="center">
  <a href="https://github.com/abh628/MrRocky/fork"><img src="https://img.shields.io/github/forks/abh628/MrRocky?style=social" alt="GitHub Forks"></a>
  <a href="https://github.com/abh628/MrRocky/stargazers"><img src="https://img.shields.io/github/stars/abh628/MrRocky?style=social" alt="GitHub Stars"></a>
  <a href="https://github.com/abh628/MrRocky/graphs/contributors"><img src="https://img.shields.io/github/contributors/abh628/MrRocky?style=social" alt="GitHub Contributors"></a>
</p>

<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/abh628/MrRocky"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku&logoColor=white" width="250px" alt="Deploy to Heroku"></a>
</p>

<h2 align="center">🚀 Deploy to Render (Free)</h2>

<p align="center">
  <a href="https://render.com/deploy?repo=https://github.com/abh628/MrRocky">
    <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render">
  </a>
</p>

## ✨ Features

- **Play Music**: Stream high-quality music in Telegram voice chats
- **Multiple Sources**: YouTube, Spotify, SoundCloud, and local files
- **Playlists**: Create and manage playlists for your group
- **Multi-Language**: Available in multiple languages
- **Elegant UI**: Clean and modern user interface
- **Group Management**: Powerful admin commands
- **High Quality**: Crystal clear audio streaming

## 📊 Repository Stats

<p align="center">
  <a href="https://github.com/abh628/RockyMusic"><img src="https://img.shields.io/github/repo-size/abh628/RockyMusic?style=flat-square" alt="Repo Size"></a>
  <a href="https://github.com/abh628/RockyMusic/issues"><img src="https://img.shields.io/github/issues/abh628/RockyMusic?style=flat-square" alt="Issues"></a>
  <a href="https://github.com/abh628/RockyMusic/network/members"><img src="https://img.shields.io/github/forks/abh628/RockyMusic?style=flat-square" alt="Forks"></a>
  <a href="https://github.com/abh628/RockyMusic/stargazers"><img src="https://img.shields.io/github/stars/abh628/RockyMusic?style=flat-square" alt="Stars"></a>
  <a href="https://github.com/abh628/RockyMusic/blob/main/LICENSE"><img src="https://img.shields.io/github/license/abh628/RockyMusic?style=flat-square" alt="LICENSE"></a>
  <a href="https://github.com/abh628/RockyMusic/commits/main"><img src="https://img.shields.io/github/last-commit/abh628/RockyMusic?style=flat-square" alt="Last Commit"></a>
</p>

## 🔥 Essential Commands

| Command | Description |
| --- | --- |
| `/play` | Play song from YouTube |
| `/pause` | Pause the current stream |
| `/resume` | Resume the paused stream |
| `/skip` | Skip to the next song |
| `/stop` | Stop the streaming |
| `/playlist` | Show the playlist |
| `/song` | Download a song as audio |
| `/settings` | Open bot settings |

## 🚀 Deployment Guide

### 🔧 VPS Deployment (Step by Step)

#### Prerequisites

First, update your system and install required packages:

```bash
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install python3-pip ffmpeg git -y
```

#### Clone the Repository

```bash
git clone https://github.com/abh628/MrRocky
cd MrRocky
```

#### Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Install Dependencies

```bash
pip3 install -U pip
pip3 install -U -r requirements.txt
```

#### Configuration

Copy example config file and edit it with your values:

```bash
cp sample.env .env
nano .env
```

Fill in your:
- `API_ID` & `API_HASH` from my.telegram.org
- `BOT_TOKEN` from @BotFather
- `SESSION_STRING` (Generate using session generator bot)
- `MUSIC_BOT_NAME` (your bot name)
- `SUDO_USERS` (your user ID)

#### Starting the Bot

There are two ways to start the bot:

1. Using Python directly:
```bash
python3 -m RockyMusic
```

2. Using Bash script:
```bash
bash start
```

#### Running in Background with Screen

To keep the bot running in background:

```bash
screen -S MrRocky
bash start
```

To detach the screen, press `Ctrl+A` then `D`

To reattach the screen later:
```bash
screen -r MrRocky
```

### ☁️ Heroku Deployment

<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/abh628/RockyMusic"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-purple?style=for-the-badge&logo=heroku&logoColor=white" width="250px" alt="Deploy to Heroku"></a>
</p>

1. Click the button above
2. Fill in the required details:
   - App name
   - API_ID & API_HASH
   - BOT_TOKEN
   - MUSIC_BOT_NAME
   - SESSION_STRING
   - SUDO_USERS (your User ID)
3. Click "Deploy App"
4. Once deployed, go to Resources tab and turn on the worker
