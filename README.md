# Russian Tracked Handwritings

Data Set Information:

We created a character dataset by collecting samples from 12 writers. Each writer contributed with letters (lower and uppercase), digits, and words from a pangram that we have not employed in our experiments, but they are included in "extra" folder for each writer in this database. Up to 4 samples have been collected for each pair writer/character, and the total number of samples in this database version is 2812:


Moreover, this classification task is a 42-class one because we have not considered a different class for each different character: each one of the 33 letters is considered as a case-independent class, there are 9 additional clases for non-zero digits, and the zero is included in the same class as "о" 's.

Database structure:

**scanner.py** - character scanning program, dataset collection.  
**convert2mnist.py** - a program for converting a dataset into a mnist-like form. It is intended for an example with the test.  
**example_using.py** - example of a primitive grid for character recognition. It is intended only to demonstrate the consistency of the dataset. When using the dataset, of course, the user can and will use their own, more advanced approaches.  
data - folder with dataset.  
**w_n_m** - folder with writer's attempt (in total 37 folders)  
&emsp;       \<char\> - the main file of the symbol track, a text file with a list of coordinates of the form - "x1","y1","x2","y2",...,"xN","yN".  
&emsp;       \<char\>_times - a file with additional information on the track with a list of time in ms between receiving coordinates of points.  
&emsp;       \<char\>.png is an auxiliary file - a picture of the symbol as it was visible to the writer. The file is for understanding only.  
 


The handwriting samples were collected on a **xp pen deco03** using its stylus. Each one of the 8 writers completed 1-4 consecutive sessions. In each session, the corresponding writer was asked to write one example for each character in a fixed set including lowercase and uppercase letters, digits, along with pangram words omitted. The acquisition program shows a set of boxes on the screen, a different one for each required character, and writers are told to write only inside those boxes. Subjects are monitored only when writing their first sample and every further sample is considered to be OK due to its writer accepted them as such.

Only X and Y coordinate information and timing information were recorded along the strokes by the acquisition program, without, for instance, pressure level values.

Class distribution in **example_using.py**:
              
[A] = { "а" , "А" }  
[Б] = { "б" , "Б" }         
[В] = { "в" , "В" }  
[Г] = { "г" , "Г" }  
[Д] = { "д" , "Д" }  
[Е] = { "е" , "Е" }        
[Ё] = { "ё" , "Ё" }            
[Ж] = { "ж" , "Ж" }            
[З] = { "з" , "З" }             
[И] = { "и" , "И" }                
[Й] = { "й" , "Й" }               
[К] = { "к" , "К" }                
[Л] = { "л" , "Л" }                
[М] = { "м" , "М" }                
[Н] = { "н" , "Н" }               
[О] = { "о" , "О", "0" }              
[П] = { "п" , "П" }               
[Р] = { "р" , "Р" }                
[С] = { "с" , "С" }                
[Т] = { "т" , "Т" }                
[У] = { "у" , "У" }                
[Ф] = { "ф" , "Ф" }               
[Х] = { "х" , "Х" }               
[Ц] = { "ц" , "Ц" }               
[Ч] = { "ч" , "Ч" }                
[Ш] = { "ш" , "Ш" }                
[Щ] = { "щ" , "Щ" }                
[Ъ] = { "ъ" , "Ъ" }               
[Ы] = { "ы" , "Ы" }                
[Ь] = { "ь" , "Ь" }               
[Э] = { "э" , "Э" }               
[Ю] = { "ю" , "Ю" }                
[Я] = { "я" , "Я" }                
[1] = { "1" }                
[2] = { "2" }               
[3] = { "3" }               
[4] = { "4" }                
[5] = { "5" }                
[6] = { "6" }                
[7] = { "7" }               
[8] = { "8" }                
[9] = { "9" }  
