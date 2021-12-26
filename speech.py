#! /usr/bin/python3

from tkinter import Tk, scrolledtext, Button, Spinbox, StringVar
from tkinter.constants import CENTER, END, LEFT, RIGHT, X
import subprocess
# from gtts import gTTS


def start():
    sr = st.get(1.0, END).replace('\n', '')
    v = 'echo ' + sr + ' | RHVoice-test --profile ' + var.get() + conf
    # v = 'echo ' + sr + ' | RHVoice-client -s ' + var.get() + conf + \
    #     '| aplay -q'
    subprocess.run(v, shell=True)


def save_wav():
    sv = st.get(1.0, END).replace('\n', '')
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


root = Tk()
root.title('Text-to-Speech')
var = StringVar()
sb = Spinbox(
    root, textvariable=var, value=['Aleksandr-HQ', 'Elena', 'Anna'],
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
