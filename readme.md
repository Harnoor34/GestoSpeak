# GestoSpeak

This application leverages the power of machine learning to detect and recognize American Sign Language (ASL) in real-time. It’s capable of converting these signs into alphabets, and subsequently, into sentences. The app provides an intuitive interface for users to communicate effectively using sign language. Not stopping at just visual representation, the app also includes text-to-speech functionality. With a simple click of the ‘Speak’ button, the app vocalizes the created sentences, making communication more accessible and seamless.

## Features

GestoSpeak uses various algorithms to make the project work for e.g.

* **Max Pooling Algorithm** - Max Pooling is a down-sampling operation that helps to extract dominant features from the input while reducing its dimensionality. It works by scanning the input with a window (of a defined size) and selecting the maximum value within that window. This process helps to make the model more robust to variations and reduces computational cost by decreasing the number of parameters to learn, all while maintaining the essential features needed for accurate ASL recognition.

* **Conventional Layers** - This project also leverages the power of Convolutional Neural Networks (CNNs) to bridge the communication gap between sign language and spoken language. CNNs excel at recognizing patterns in visual data, making them ideal for analyzing the hand shapes, orientations, and movements that form the building blocks of sign language. By training a CNN on a vast dataset of sign language videos paired with their corresponding spoken translations, the network learns to extract these visual features and map them to the appropriate spoken words. This allows our system to accurately interpret sign language gestures in real-time, fostering seamless communication for everyone.

## Getting Started 

### Dependencies

Language - **Python 3.11**
IDE Used - **VS Code**

#### Libraries

To install the libraries used just run the Libraries.bat file given as admin

## Running GestoSpeak

Running GestoSpeak is a Very simple task. To run just

1. Run the GestoSpeak.py Application **After Installing The Dependencies**
2. After Running the Application It Starts Detecting the Hand signs automatically
3. Do Some Gestures To Find If It Is Working
4. For Space, Next And Backspace use -
#### Space

![image](https://github.com/Harnoor34/GestoSpeak/assets/65222131/57ad6a39-9e01-4d99-8bb7-133d35177111)

#### Next

![image](https://github.com/Harnoor34/GestoSpeak/assets/65222131/fe786586-2e49-4f29-aef3-1c1f339852d5)

#### Backspace

![image](https://github.com/Harnoor34/GestoSpeak/assets/65222131/126317d4-5426-4867-ad6e-dc46dd3013cd)
   
6. To Make the Application speak the sentence Just Click on speak

### Video Explaination

  https://github.com/Harnoor34/GestoSpeak/assets/65222131/3eba9c0f-bdab-428b-83c1-340b5dcbb3f9
