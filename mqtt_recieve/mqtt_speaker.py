import paho.mqtt.client as mqtt
import pafy
import vlc
from playsound import playsound

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("kb_test/1")

def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")
    if msg.payload.decode() == '5':
        play_youtube_video('https://www.youtube.com/watch?v=bP9gMpl1gyQ')

def play_youtube_video(url):
    video = pafy.new(url, ydl_opts={"external_downloader": "pip install yt-dlp"})
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.emqx.io", 1883, 60)  # เปลี่ยน broker และพอร์ตตามที่คุณใช้
client.loop_forever()