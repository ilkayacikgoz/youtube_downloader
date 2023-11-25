import pytube
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

url = input("Video urlsini giriniz: ")

path = ""

pytube.YouTube(url).streams.get_highest_resolution().download(path)