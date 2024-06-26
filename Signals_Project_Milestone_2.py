import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
import math

def generatesong (t,Fi,fi,num_of_notes):
    
    yfinal=np.zeros(len(t))
    
    T=len(t)//num_of_notes
 
    for i in range(num_of_notes):
        
        x=np.zeros(len(t))
        x[i*T:(i+1)*T-np.random.randint(T//4,T//2)] =1
        
        x1=np.sin(2*np.pi*Fi[i]*t)
        x2=np.sin(2*np.pi*fi[i]*t)
        x3=x1+x2


        y= x3* x
       
        yfinal=yfinal+y

    return  yfinal




num_of_notes=29


C3=130.81
D3= 146.83
E3=164.81
F3=174.61
G3=196
A3=220
B3=246.93



C4=261.63
D4= 293.66
E4=329.63
F4=349.23
G4=392
A4=440
B4=493.88






𝑡 = np. linspace(0 , 15 , 12 * 4024)

fi=np.array([C3,C3,G3,G3,A3,A3,G3,F3,F3,E3,E3,D3,D3,C3,G3,G3,F3,F3,E3,E3,D3,G3,G3,F3,F3,E3,E3,D3,C3])
Fi=np.array([C4,C4,G4,G4,A4,A4,G4,F4,F4,E4,E4,D4,D4,C4,G4,G4,F4,F4,E4,E4,D4,G4,G4,F4,F4,E4,E4,D4,C4])


x= generatesong(t,Fi,fi,num_of_notes)











N = 15*1024
f = np.linspace(0 , 512 , N//2)

x_f = fft(x)
x_f = 2/N * np.abs(x_f [0:np.int(N/2)])


fn1,fn2= np.random.randint(0,512,2) #it can get the two values equal and it can get 0



n= np.sin(2*fn1*np.pi*t) + np.sin(2*fn2*np.pi*t) 
xwithnoise= x + n 

xwithnoise_f = fft(xwithnoise)
xwithnoise_f = 2/N * np.abs(xwithnoise_f [0:np.int(N/2)])





high=math.ceil(np.max(x_f))

FN1, FN2 = np.where(xwithnoise_f>high)[0]/15 #returns tupil (array if indecies, data type)





xfiltered= xwithnoise - (np.sin(2*int(FN1)*np.pi*t) + np.sin(2*int(FN2)*np.pi*t) )

xfiltered_f= fft(xfiltered)
xfiltered_f = 2/N * np.abs(xfiltered_f [0:np.int(N/2)])


plt.plot(t, x)
plt.title("x only")
plt.figure()
plt.plot(f, x_f)
plt.title("x f domain")
plt.figure()
plt.plot(t, xwithnoise)
plt.title("x with noise")
plt.figure()
plt.plot(f, xwithnoise_f)
plt.title("x with noise in f domain")
plt.figure()
plt.plot(t, xfiltered)
plt.title("x filtered")
plt.figure()
plt.plot(f, xfiltered_f)
plt.title("x filtered in f domain")

sd.play(x, 3 * 1024)

