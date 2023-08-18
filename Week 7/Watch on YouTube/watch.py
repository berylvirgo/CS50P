import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe[^>]*\bsrc="(https?://(?:www\.)?youtube\.com/embed/[^"]+)"[^>]*>', s)
    
    if match:
        youtube_url = match.group(1)
        short_url = convert_to_youtube_short_url(youtube_url)
        return short_url
    else:
        return None


def convert_to_youtube_short_url(long_url):
    # Replace the 'https://www.youtube.com/embed/' part with 'https://youtu.be/' to get the short URL
    if long_url.startswith("https://www.youtube.com/embed/"):
        return long_url.replace("https://www.youtube.com/embed/", "https://youtu.be/")
    elif long_url.startswith("https://youtube.com/embed/"):
        return long_url.replace("https://youtube.com/embed/", "https://youtu.be/")
    elif long_url.startswith("http://www.youtube.com/embed/"):
        return long_url.replace("http://www.youtube.com/embed/", "https://youtu.be/")
    else:
        return long_url.replace("http://youtube.com/embed/", "https://youtu.be/")


if __name__ == "__main__":
    main()