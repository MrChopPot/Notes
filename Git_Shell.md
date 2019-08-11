## Shell

#### 1. Manipulating files and directories

~~~shell
# Where am I?
pwd

# How can I identify files and directories?
ls # ls /home/repl/seasonal

# How else can I identify files and directories?
# ...if it begins with /, it is absolute; and vice versa.
ls /home/repl/course.txt # absolute
ls course.txt # relative
ls seasonal/summer.csv # relative
ls people # relative

# How can I move to another directory?
cd /home/repl/seasonal # absolute
cd seasonal # relative

# If you are in /home/repl/seasonal, where does cd ~/../. take you?
Answer: /home

# How can I copy files?
cp seasonal/summer.csv backup/summer.bck
cp seasonal/spring.csv seasonal/summer.csv backup

# How can I move a file?
mv seasonal/spring.csv seasonal/summer.csv backup

# How can I rename files?
mv course.txt old-course.txt

# How can I delete files?
rm thesis.txt backup/thesis-2017-08.txt

# How can I create and delete directories?
rmdir people
mkdir yearly
mkdir yearly/2017
~~~



#### 2. Manipulating data

~~~shell
# How can I view a file's contents?
cat course.txt

# How can I view a file's contents piece by piece?
less seasonal/spring.csv seasonal/summer.cs # Press spacebar to page down, :n to go to the second file, and :q to quit.

# How can I look at the start of a file?
head seasonal/autumn.csv

# How can I control what commands do?
head -n 5 seasonal/winter.csv

# How can I list everything below a directory?
ls -R -F # -R shows every file & directory in the current level, then everything in each sub-directory; -F prints a / after the name of directories and a * after the name of runnable programs.

# How can I get help for a command?
man tail | cat
tail -n +7 seasonal/spring.csv

# How can I select columns from a file?
cut -f 2-5,8 -d , values.csv # select columns 2 through 5 and columns 8, using comma as the separator, in file "value.csv"

# What can't cut do?
Answer: In particular, it does not understand quoted strings. 

# How can I repeat commands?
Just type !55 to re-run the 55th command in your history. You can also re-run a command by typing an exclamation mark followed by the command\'s name, such as !head or !cut, which will re-run the most recent use of that command.

# How can I select lines containing specific values?
grep can search for patterns as well; we will explore those in the next course. What's more important right now is some of grep's more common flags:

-c: print a count of matching lines rather than the lines themselves
-h: do not print the names of files when searching multiple files
-i: ignore case (e.g., treat "Regression" and "regression" as matches)
-l: print the names of files that contain matches, not the matches
-n: print line numbers for matching lines
-v: invert the match, i.e., only show lines that don't match

# Why isn't it always safe to treat data as text?
paste seasonal/autumn.csv seasonal/winter.csv
~~~

