# MFCKYLD-II <img src='https://www.inderdhillon.com/files/logo-gray.png' width=100 align='right'>
>Inder Dhillon <br>
>inderdhillon.com <br>

### Description:
Python code ‘MFCKYLD-II’ generates M sub shell Fluorescence and Coster-Kronig Yields for elements with Z in the range 57 ≤ Z ≤ 90 for McGuire data and 67 ≤ Z ≤ 90 for Chen et al.’s data.

### Overview:
The program ‘MFCKYLD-II’ predicts M sub-shell Fluorescence and Coster-Kronig Yields for elements by fitting known values with a regression model and using the model to predict values for atomic numbers that don't have known researched values.
In paper ‘MFCKYLD-II’ the program language has been updated from _Fortran_ to _python_ for more accessibility by adding a GUI and the program code has been vectorized using the pandas library for faster execution. It can be run on any architecture with a _python 3.0+ compiler_ and on operating systems: Linux, Windows, Mac OS. It is available in python _.py_ file format. The dependency libraries required for execution for the program are: 
* pandas 
* numpy 
* tkinter

### Sections: 
##### Export to CSV:
Allows exporting values for multiple atomic numbers to a _comma separated values(.csv)_ file.
##### Quick View:
Allows you to obtain the M sub shell Fluorescence and Coster-Kronig Yields right in the program for a single atomic number.

### Command:
``python MFCKYLD.py``

### Acknowledgements:
Done as a part of research with:<br>

Gurjit Singh Dhindsa<br>
_Eastern New Mexico University, Portales, NM, USA_<br>
Gurpreet Kaur<br>
_Physics Department, University of Berkeley, California, USA_<br>
Raj Mittal<br>
_Nuclear Science Laboratories, Physics Department, Punjabi University, Patiala, India_<br>
