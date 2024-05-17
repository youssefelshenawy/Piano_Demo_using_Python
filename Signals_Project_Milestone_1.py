import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd


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






𝑡 = np.linspace(0 , 3 , 12 * 1024)

fi=np.array([C3,C3,G3,G3,A3,A3,G3,F3,F3,E3,E3,D3,D3,C3,G3,G3,F3,F3,E3,E3,D3,G3,G3,F3,F3,E3,E3,D3,C3])
Fi=np.array([C4,C4,G4,G4,A4,A4,G4,F4,F4,E4,E4,D4,D4,C4,G4,G4,F4,F4,E4,E4,D4,G4,G4,F4,F4,E4,E4,D4,C4])


x= generatesong(t,Fi,fi,num_of_notes)

plt.plot(t, x)

sd.play(x, 3 * 1024)
