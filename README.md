# Python YouTube downloader
A simple terminal **downloader** that allows you to download a **video** or just an **audio track** from **YouTube**. The audio track is saved in the **highest** available **quality to mp3**.

## Libraries imported
- pydub
- pytube

```bash
pip install pytube pydub
```
or clone repo and install **requirements.txt**

## Installation

```bash
git clone https://github.com/Zajic86/YouTube-downloader.git
cd YouTube-downloader
pip install -r requirements.txt
cd yt-down
python yt-down.py
```
or just copy/paste code from yt-down/yt-down.py and install libraries.

If you have a problem with decoding to mp3 (Ubuntu) try install or update **mpg123**:
```bash
sudo apt install mpg123
```

## Using a script
- Paste the **copied URL** of the video from YouTube
- Select an option: download the entire **video (1)** or only the **audio track (2)**
- Processing video: The video will be downloaded in the highest possible quality to the **/video** folder
- Processing audio: The audio is downloaded in the highest possible quality in .webm format to the **/audio** folder, then it is converted to mp3 format and the original format is deleted
- Output message
- Query for next download (y/n)

**Note:** keep in mind that the videos may be licensed and it may be illegal to download them. Download only your videos or freely licensed ones. I take no responsibility for using this script for illegal purposes