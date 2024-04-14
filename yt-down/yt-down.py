#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pytube import YouTube
from pydub import AudioSegment
import os


def download_audio_highest_quality(in_url, output_path):
    """
    Downloads the highest quality audio from the given YouTube URL and converts it to MP3.
    """
    video_obj = YouTube(in_url)
    audio_streams = video_obj.streams.filter(only_audio=True).order_by('abr').desc()
    highest_quality_audio = audio_streams.first()
    audio_file_path = highest_quality_audio.download(output_path=output_path)
    print("OK - Audio downloaded:", audio_file_path)
    convert_to_mp3(audio_file_path)


def convert_to_mp3(input_path):
    """
    Converts the input audio file to MP3 format by pydub library
    """
    audio = AudioSegment.from_file(input_path)
    output_path = input_path[:-5] + ".mp3"
    audio.export(output_path, format="mp3")
    print("OK - Audio converted & saved to mp3:", output_path)
    os.remove(input_path)  # Delete the original audio file


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.realpath(__file__))
    while True:
        input_url = input("Enter the YouTube video URL: ")
        if "youtube" in input_url:
            choice = input("Complete video (1) or just the audio (2)? Enter 1 or 2: ")
            print("Processing...")
            if choice == "1":
                video = YouTube(input_url)
                stream = video.streams.get_highest_resolution()
                save_path = os.path.join(script_dir, "video")
                stream.download(output_path=save_path)
                print("OK - Video has been downloaded to:", save_path)
            elif choice == "2":
                save_path_audio = os.path.join(script_dir, "audio")
                download_audio_highest_quality(input_url, save_path_audio)
            else:
                print("! Invalid choice. Enter 1 for video or 2 for audio.")
            again = input("? Want more (y/n): ")
            if again.lower() != "y":
                break
        else:
            print("! Wrong link.")
