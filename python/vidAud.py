import moviepy.editor as mp

# converting the video to audio
clip = mp.VideoFileClip(r"Video File")
clip.audio.write_audiofile(r"Audio File")