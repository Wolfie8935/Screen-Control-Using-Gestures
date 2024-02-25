# Screen-Control-Using-Gestures

## Overview
This project aims to revolutionize how we interact with our computers by allowing users to control their screens through hand gestures. Utilizing the power of computer vision and machine learning, this application detects specific hand gestures to perform actions like moving the mouse, clicking, scrolling, and even minimizing windows. The next phase of the project will incorporate the Sign Language MNIST database to detect alphabets, enabling gesture-based text input to act as a keyboard, making it more inclusive and user-friendly.

## Creators
- Aman Goel [https://github.com/Wolfie8935]
- Ayushi Mishra [https://github.com/humblefoo02]

## Features
- **Gesture-Based Mouse Control**: Move the mouse cursor on the screen using hand movements.
- **Clicks and Scrolling**: Perform left and right clicks, and scroll up or down using specific gestures.
- **Minimize Windows**: Ability to minimize active windows with a unique gesture.
- **User-Friendly Interface**: Designed with the user in mind, ensuring ease of use.
- **Sign Language Recognition**: *(Upcoming)* Integration with the Sign Language MNIST database for detecting alphabets through gestures.

## Installation
To run this project, you'll need Python 3.10 and the following libraries:
- OpenCV (`cv2`) for image processing and gesture detection.
- NumPy for numerical calculations.
- PyAutoGUI for controlling the mouse and keyboard.
- Matplotlib for visualizing command execution statistics.

Use the following commands to install the required packages:
```bash
pip install opencv-python numpy pyautogui matplotlib
```

## Usage
Before running the application, make sure your webcam is connected and properly configured. Also change the output of the cap file accordingly.

## Contributing
We welcome contributions to improve this project further. Whether you have suggestions, bug reports, or want to add new features, please feel free to make a pull request or open an issue.


## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Database Link: [https://www.kaggle.com/datasets/datamunge/sign-language-mnist/data]

## Future Work
- Sign Language Alphabet Detection: The integration of the Sign Language MNIST database is underway. This will allow for the detection of alphabetic gestures, enabling users to input text through sign language.
- Improved Gesture Recognition Accuracy: Ongoing work to refine the machine learning model for more accurate and responsive gesture detection.
- Expanded Gesture Commands: Plans to include more complex gestures for a wider range of controls, such as volume adjustment, tab switching, and more.
- Custom Gesture Training: Implementing a feature for users to train the application to recognize custom gestures, tailoring the experience to individual needs.
