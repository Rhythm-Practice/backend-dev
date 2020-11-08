#Importa librerias y API necesarias
import requests
import matplotlib.pyplot as plot
from scipy.io import wavfile

#Asigna los audios a las variables
samplingFrequency1, signalData1 = wavfile.read('/content/x.wav')
samplingFrequency2, signalData2 = wavfile.read('/content/y.wav')

#Genera las imagenes en formato ".png"
plot.specgram(signalData1, Fs=samplingFrequency1)
plot.savefig('/content/primero.png')//Genera las imagenes ".png"
plot.specgram(signalData2, Fs=samplingFrequency2)
plot.savefig('/content/segundo.png')

#Compara las imagenes con la API "Image-similarity"
r = requests.post(
    "https://api.deepai.org/api/image-similarity",
    files={
        'image1': open('/content/primero.png', 'rb'),
        'image2': open('/content/segundo.png', 'rb'),
    },
    headers={'api-key': '5a3c58cf-d3c0-410b-b778-069bef62f137'}
)
#Imprime un resultado en formato ".json" donde 0 seria una imagen totalmente identica
print(r.json())
