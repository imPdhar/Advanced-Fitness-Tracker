# Advanced Fitness Tracker

This was the Machine Learning code that was designed for Advanced fitness purposes.

**Hardware-** Raspberry Pi 0w with custom charging circuit, BMP180(Pressure Sensor) and MPU9250(Gyro Sensor)

**Tech stack-** Python 3.x, Sklearn, Scipy, Numpy, and Pandas.

## Features 

- Detects the exercise when the device is in the active-time mode i.e when the code is running. Can currently detect Vertical Raises, Bicep Curls, Push Ups and Sit-Ups. 
- Detects number of steps and displays total calorie burnt in passive mode.
- Detects the number of counts a user workouts. 
- Total Model accuracy of 0.95



## Requirements:

- Pandas- `pip install pandas`

  - csv included  		

- Sklearn- `pip install scikit-learn`

- Numpy- `pip install numpy`

- Matplotlib.pyplot(Optional)- `pip install matplotlib`

- scipy.signal- `pip install scipy`

  

## How to use

-  Install the requirements.
  1. Fill up the body-movement data in ***<u>ExerciseClassifier.csv</u>*** and save it in the directory of the file ***<u>FitnessXpertProgram.py</u>*** (Mind the Path of the csv file).
  2. Run the code to get counts and detect exercises. 

## Errors

1. Expect incomplete data to process error from csv.

   **Solution**: Browse to the csv file and delete the last row since it shouldn't matter after the data is acquired for a long time. 

2. Inaccurate detection if the active-time is lesser than required i.e 30s.             

   **Solution**: Workout/Acquire data for more than 30s. 

**Note:** Evaluation Data for different workouts are saved with their respective names for testing.
