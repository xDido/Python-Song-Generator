import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
𝑡=np.linspace(0,3,12*1024) #t provided
N=3*1024 #N provided



arrData1=[440, 440, 440, 493.88 ,440,392] # frequencies of the desired notes left hand
arrData2=[0, 0, 0, 0, 0, 0] # frequencies of the desired notes right hand

arrT=[0.21 ,0.21 ,0.21 ,0.21 ,0.21 , 0.21] # array for the duration press key 
arrt= [0.00, 0.44, 0.87, 1.30, 1.72, 2.15] # array for the shifting to another note

tone =0
for i in range (0,6): # looping on the 4 arrays  to generate a tone by the summation formula 
    u1=np.where(t>=arrt[i], 1 , 0) #creating the first unit step
    u2=np.where( (t>=arrt[i]+ arrT[i]) , 1 , 0) #creating the second unit step
    tone += (np.sin(2 * np.pi * arrData1[i] * t) + np.sin(2 * np.pi * arrData2[i] * t))*(u1 - u2) #doing the summation using the summation formula provided
plt.subplot(6,2,1)
plt.plot(t,tone) #plotting the signal
sd.play(tone,3*1024) #playing the sound generated by the signal


frequency = np.linspace (0, 1024/2, np.int(N/2))
freq_data = fft(tone) #Complex Signal
freq_data = 2/N * np.abs (freq_data [0:np.int(N/2)])
plt.subplot(6,2,2)
plt.plot(frequency, freq_data)


fx= np.random.randint(0,512)
fy = np.random.randint(0,512)
n = np.sin(2*np.pi*fx*t) + np.sin(2*np.pi*fy*t)
noisy = tone + n
plt.subplot(6,2,3)
plt.plot(t, noisy)

freq_data2 = fft(noisy)
freq_data2 = 2/N * np.abs (freq_data2 [0:np.int(N/2)])
plt.subplot(6,2,4)
plt.plot(frequency, freq_data2)

value = [] 
peak_freq =  np.round(np.max(freq_data))

for i in range ( 0 , len(freq_data)):
    if( peak_freq < np.round(freq_data2[i])):
        value.append(freq_data2[i])
       
filtered = noisy - (np.sin((2*np.pi*np.round(frequency[np.where(freq_data2== value[1])]))*t) + np.sin((2*np.pi*np.round(frequency[np.where(freq_data2== value[0])]))*t) )

plt.subplot(6,2,5)
plt.plot(t,filtered)

filtered_f = fft(filtered)
filtered_f = 2/N * np.abs (filtered_f[0:np.int(N/2)])
plt.subplot(6,2,6)
plt.plot(frequency, filtered_f)







        
        
        
        