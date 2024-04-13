# Python YouTube downloader
A simple terminal downloader that allows you to download a video or just an audio track from YouTube. The audio track is saved in the highest available quality to mp3.

## Libraries used
- moviePy
- pyTube
- colorama

```bash
pip install pytube moviepy colorama
```

## Installation

```bash
git clone https://github.com/Zajic86/YouTube-downloader.git
cd YouTube-downloader
pip install -r requirements.txt
cd yt-down
python yt-down.py
```
or just copy/paste code from yt-down/yt-down.py and install libraries.

If you have a problem with decoding to mp3 (Ubuntu) try install mpg123:
```bash
sudo apt install mpg123
```