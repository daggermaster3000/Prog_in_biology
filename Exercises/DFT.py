# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:28:32 2022

@author: quill
"""
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import sys
from random import uniform
import os 
def DFT(t,signal,t2,s_signal,fs,f,freqs=np.arange(0, 40,0.1)):
    """
    Perform a DFT on signal (an array of values)
    Return an array of complex numbers
    """
  
    N = len(s_signal)
    zeta = np.e**(complex(-2*np.pi/N*1j))
    res = []
    for freq in freqs:
        shat = 0
        for n in range(0, len(s_signal)-1):
            shat += s_signal[n] * zeta**(freq*n)

        res.append(shat)
     
    mag = np.absolute(res)    
    dom = max(mag)
    fmax =(mag.tolist().index(dom)-1)*0.1
    
    fig, axs = plt.subplots(3)
    fig.suptitle('Discrete Fourier transform')
    axs[0].plot(t, signal , label = f"f:{f} Hz")   
    axs[0].legend()
    axs[0].set_title("original signal")
    axs[1].plot(t2, s_signal, label=f"fs:{1/fs} Hz")   
    axs[1].legend()
    axs[1].set_title("sampled signal")
    axs[2].plot(np.absolute(np.fft.fft(s_signal)[:40]), label = "numpy  FFT")
    axs[2].plot(freqs,mag,label = "DFT")
    axs[2].legend()
    plt.savefig('DFT.png')


def sine(f=2,fs=0.001,sample=False):
    t = np.arange(0, 1, 0.001)
    ts = np.arange(0,1,fs)
    A = 2
    phase = 0
    
    signal = A*np.cos(t*2*np.pi*f+phase)
    s_sig = A*np.cos(ts*2*np.pi*f+phase)
    if sample:
        return t,signal,ts,s_sig
    else:
        return t,signal
    
def type(line_1,wait=0.1):
    for x in line_1:
        print(x, end='')
        sys.stdout.flush()
        sleep(uniform(0, wait))
        
def interact(activate):
    if activate:
        type("\nHello lad!\nI will DFT a frequency and its fifth for you! \nI am still a little insecure so keep the input under 40Hz plz :)\nAnd just to see whether or not you can trust me I will show you numpy's fft")
        sleep(1)
        f = float(input('\nType the Input frequency plz:'))
        fi = input('\nDo you want the fifth?(y/n)')
        if fi == 'y':
            type('\ncomputing fifth...')
            fifth = 3*f/2
            type(f'{fifth} Hz')
            t, signal = sine(f=f)
            t2, signal2 = sine(f=fifth)
            signal = signal+signal2
        else:
            t, signal = sine(f=f)
        DFT(t,signal)
        type('\ncomputing DFT...\n')
      
        os.startfile('DFT.png')
        type('\nDFT complete! Now I can go sleep')
        sleep(1)
        type('''\n
            ┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
            ┌▀█╔══╗╔══╗╔══╗╔══╗▀█
            ┌▀█║╔═╣║╔╗║║╔╗║╚╗╗║▀█
            ┌▀█║╚╗║║╚╝║║╚╝║╔╩╝║▀█
            ┌▀█╚══╝╚══╝╚══╝╚══╝▀█
            ┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█
            ┌▀█░░░░░░░░░░░░░░░░▀█
            ┌▀█░░█▌▌█▐▀▐░▌▀█▀░░▀█
            ┌▀█░░█▐▌█▐▐▐▀▌░█░░░▀█
            ┌▀█░░█░▌█▐█▐░▌░█░░░▀█
            ┌▀█░░░░░░░░░░░░░░░░▀█
            ┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█┌▀█ ''',wait = 0.01)
        type('\nzzz')
    else:
        f = 10
        fs = 0.2
        t, signal, ts, s_sig = sine(f=f,fs = fs,sample=True)
        DFT(t,signal,ts,s_sig,fs=fs,f=f)
        
if __name__ == "__main__":

    interact(False)
    
    
