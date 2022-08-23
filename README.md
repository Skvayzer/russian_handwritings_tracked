# Russian Tracked Handwritings

# NOT FINISHED

Data Set Information:

We created a character database by collecting samples from 8 writers. Each writer contributed with letters (lower and uppercase), digits, and words from pangram that we have not employed in our experiments, but they are included in "extra" folder for each writer in this database. Up to 4 samples have been collected for each pair writer/character, so the total number of samples in this database version is 2128:

8 writers x 2 repetitions x (2x26 letters + 10 digits)

The proposed task is a writer-independent one consisting of 11 leaving-one-writer-out tests, so the effective training set size (for each one of the 1364 test samples) is 1240:

10 writers x 2 repetitions x (2x26 letters + 10 digits)

Moreover, this classification task is a 43-class one because we have not considered a different class for each different character: each one of the 26 letters is considered as a case-independent class, there are 9 additional clases for non-zero digits, and the zero is included in the same class as o's.

This database is available in a UNIPEN-like format, trying to mimic the original Pendigits database. Two versions of that database are available; see folder: [Web Link]

The distribution of our database consists of 12 files:

uji.names
One file "UJIpenchars-wNN" per writer, where NN = "01", "02"... "11"

The handwriting samples were collected on a Toshiba Portégé M400 Tablet PC using its cordless stylus. Each one of the 11 writers completed 2 non-consecutive sessions. In each session, the corresponding writer was asked to write one exemplar for each character in a fixed set including lowercase letters, uppercase ones, and digits, along with other characters omitted from this database version. The acquisition program shows a set of boxes on the screen, a different one for each required character, and writers are told to write only inside those boxes. If they make a mistake or are unhappy with a character writing, they are instructed to clear the content of the corresponding box by using an on-screen button and try again. Subjects are monitored only when writing their first exemplars and every sample considered OK by its writer was accepted as such.

Only X and Y coordinate information was recorded along the strokes by the acquisition program, without, for instance, pressure level values or timing information. Thus, in multi-stroke samples, no information at all was recorded between strokes; however, in this database version we have included a ".DT 100" line in sample files after each stroke, following the Pendigits database criterion.

We have observed that runs of consecutive points with identical coordinates were frequently acquired inside strokes; such runs were preserved in this database version, so each database user must decide whether to avoid them by an appropriate preprocessing step or not.

Attribute Information:

For each sample, you can find:

a. The character it represents.
b. The class it belongs to.
c. The sequence of strokes it consists of.

When testing, you are only allowed to read the sequence of strokes of a sample in order to predict its class.

For Each Attribute:

As said before, this database is available in a UNIPEN-like format, trying to mimic the original Pendigits database. A definition of UNIPEN format can be found in [Web Link]

Regarding the attributes of a sample, you can find them in the file format as follows:

a. Character name: Each sample begins with a ".SEGMENT" line. The last component of that line shows the character name, one out of 62 possibilities. The complete set of possibilities is shown in the first line of each file, a ".LEXICON" line. Those possibilities are repeated here:

"a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m"
"n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"
"A" "B" "C" "D" "E" "F" "G" "H" "I" "J" "K" "L" "M"
"N" "O" "P" "Q" "R" "S" "T" "U" "V" "W" "X" "Y" "Z"
"0" "1" "2" "3" "4" "5" "6" "7" "8" "9"

b. Class name: The class name of a sample appears in the ".COMMENT" line that follows its ".SEGMENT" line. This name is one out of 35 possibilities. In each file, the complete set of possibilities is shown in ".COMMENT" lines between the ".LEXICON" line and a ".HIERARCHY" one. Those class definitions are repeated here:

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

c. Sequence of strokes: After the ".SEGMENT" and ".COMMENT" lines of a sample, a sequence of one or more strokes follows until the beginning of a new sample or the end of the file. Each stroke begins with a ".PEN_DOWN" line and ends with a sequence ".PEN_UP", ".DT 100"; in between, a sequence of lines, each one representing X and Y coordinates of a point, where X grows left-to-right and Y grows downwards. Coordinates are integer numbers.
