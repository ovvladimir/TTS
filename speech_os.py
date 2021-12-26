#! /usr/bin/python3

from tkinter import Tk, scrolledtext, Button, Spinbox, StringVar
from tkinter.constants import CENTER, END, LEFT, RIGHT, X
import subprocess
import os
# from gtts import gTTS


def start():
    sr = st.get(1.0, END).replace('\n', '')
    if os_name == 'nt':
        os.system(f"{command}; $speech.Speak('{sr}')")
    else:
        v = 'echo ' + sr + ' | RHVoice-test --profile ' + var.get() + conf
        # v = 'echo ' + sr + ' | RHVoice-client -s ' + var.get() + conf + \
        #     '| aplay -q'
        subprocess.run(v, shell=True)


def save_wav():
    sv = st.get(1.0, END).replace('\n', '')
    if os_name == 'nt':
        os.system(
            f"{command}; $speech.SetOutputToWaveFile('speech.wav'); "
            f"$speech.Speak('{sv}'); $speech.SetOutputToNull(); "
            "$speech.Dispose()")
    else:
        w = 'echo ' + sv + ' | RHVoice-test --profile ' + var.get() + conf + \
            '--output speech.wav'
        # w = 'echo ' + sv + ' | RHVoice-client -s ' + var.get() + conf + \
        #     '> speech.wav'
        subprocess.run(w, shell=True)
        # tts = gTTS(sv, lang='ru')
        # tts.save('speech.wav')


# ударение в слове с помощью +, например, к+рая
# для RHVoice-client:
# conf = ' -v -1 -r 0.3 -p -0.5 '
# для RHVoice-test:
conf = ' --volume 30 --pitch 75 --rate 100 '

os_name = os.name
if os_name == 'nt':
    # https://docs.microsoft.com/ru-ru/dotnet/api/system.speech.synthesis.speechsynthesizer.volume?view=netframework-4.8
    command = "PowerShell -Command Add-Type -AssemblyName System.Speech; " \
        "$speech = New-Object System.Speech.Synthesis.SpeechSynthesizer; " \
        "$speech.SelectVoice('Microsoft Irina Desktop'); " \
        "$speech.Volume=100; $speech.Rate=0"  # от 0 до 100 и от -10 до 10

root = Tk()
root.title('Text-to-Speech')

var = StringVar()
sb = Spinbox(
    root, textvariable=var,
    value=['Aleksandr-HQ', 'Elena', 'Anna'] if os_name != 'nt' else ['Irina'],
    justify=CENTER, fg='blue', wrap=True, state='readonly'
)
sb.pack(fill=X)
st = scrolledtext.ScrolledText(root)
st.pack(fill=X)
st.focus()
bt1 = Button(root, text='S T A R T', fg='red', command=start, bd=4)
bt1.pack(expand=1, fill=X, side=LEFT)
bt2 = Button(root, text='S A V E', fg='red', command=save_wav, bd=4)
bt2.pack(expand=1, fill=X, side=RIGHT)

root.mainloop()
