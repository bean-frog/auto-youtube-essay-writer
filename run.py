import yt_dlp
import webvtt
import requests
import sys
import ollama

# get URL
if len(sys.argv) <= 1:
    print("[error] Usage: 'python3 auto_astro_ls.py [youtube URL]")
    exit()

ydl_opts = {'extract_flat': 'discard_in_playlist',
 'fragment_retries': 10,
 'ignoreerrors': 'only_download',
 'postprocessors': [{'key': 'FFmpegConcat',
                     'only_multi_video': True,
                     'when': 'playlist'}],
 'retries': 10,
 'skip_download': True,
 'subtitleslangs': ['en-orig'],
 'writeautomaticsub': True,
 'outtmpl': 'subs.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([str(sys.argv[1])])

vtt = webvtt.read('subs.en-orig.vtt')
transcript = ""
lines = []

for line in vtt:
    lines.extend(line.text.strip().splitlines())

previous = None
for line in lines:
    if line == previous:
       continue
    transcript += " " + line
    previous = line

print("[subtitles] '"+str(transcript[:50])+"..."+str(transcript[len(transcript)-50:])+"'")

file = open('txt.txt', 'r')
text = file.read()
file.close()


print("[ollama] loading Ollama")
try:
    ollama.list()
except:
    print("[ollama] Ollama not detected running, exiting")
    exit()

print("[ollama] prompting Ollama...")


def prompt_ollama(prompt):
    response = ollama.chat(model='llama3.2:3b', messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])
    return str(response['message']['content'])

#prompt_ollama(str(str("The following transcript is an text transcription of an important spoken lecture. From the lecture, draft an essay that explains the concepts described. The essay shoould explain the concepts just learn from the transcription, and be entirely in the third-person perspective. Use a conversational tone, and simple but clear writing. Transcript: '"+str(transcript)+"'")))
prompt = "Write a long summary of the following transcription: "
response = prompt_ollama(str(prompt + transcript))
print("[ollama] prompting Ollama again...")
prompt2 = "The following transcript is an text summarization of an important lecture. From the lecture, draft an ESSAY that explains the concepts described. The essay shoould explain the concepts just learn from the transcription, and be entirely in the third-person perspective. Use a conversational tone, and simple but clear writing. Transcript: "
response2 = prompt_ollama(str(prompt2 + response))

print("[ollama] Done!")


print("[essay] \n"+str(response2)+"\n")
print('[done] DONE!')
#print(text)
