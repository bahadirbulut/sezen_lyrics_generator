# Sezen Aksu style song lyrics generator
Simple LSTM model using tensorflow to generate song lyrics in Sezen Aksu style.


## General Information
I have created a simple scraper in python in order to download the lyrics 
from a website. In total there are 354 song lyrics of famous pop singer 
Sezen Aksu. Total amount of rows are 8.797.

I have also uploaded sezen_lyrics.txt file which includes all the lyrics that I
have downloaded. It is already cleaned and ready for modelling.

You can play with it and use any other website to download different lyrics.

## Model configuration and performance

### Model Summary
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
embedding (Embedding)        (None, 110, 100)          874400    
_________________________________________________________________
bidirectional (Bidirectional (None, 110, 300)          301200    
_________________________________________________________________
dropout (Dropout)            (None, 110, 300)          0         
_________________________________________________________________
lstm_1 (LSTM)                (None, 100)               160400    
_________________________________________________________________
dense (Dense)                (None, 4372)              441572    
_________________________________________________________________
dense_1 (Dense)              (None, 8744)              38237512  
=================================================================
Total params: 40,015,084
Trainable params: 40,015,084
Non-trainable params: 0
```

### Model Performance
With hundred epochs i have achieved ~0.8 accuracy. Although looking at the accuracy curve
it looks like it has not reached the plateau yet, thus with more epochs it is likely
to reach higher accuracy. Since this is just for fun. I am not willing to train it
more for now.

As a result sometimes some sentencecs generated are not very meaningful but
there are very interesting sentences as well! Play with it yourself and have fun!


## Usage
You can simply clone this repo and use jupyter notebook to run predictions,
based on your desired starting sentence.<br>

<i> P.S. training the model on GCP took me around 3 hours.
<br>
<br> 
I have used:<br>
- n1-standard-4 (4 vCPUs, 15 GB memory) with 1 x NVIDIA Tesla K80 GPU.</i>
<br><br>
You can try with different configurations for the VM or different configurations
for the model as well. Let me know about your results. 


## Model files
[You can download the model in h5 format here](https://drive.google.com/file/d/1qOGe9EAeoEwB8ivYBkueSLNs8-kpEdce/view?usp=sharing)

[You can download the full model as tensorflow model file here](https://drive.google.com/file/d/1i9T9Y3lzaTxGMd9JDVppWEjP3VWeULCk/view?usp=sharing)

