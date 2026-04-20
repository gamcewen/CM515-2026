# Week 11 Assignment 

**Due:** Wed April 15, 2026. 10am. Turn in on canvas.

**Instructions:** 
  * Please turn in the answers to this assignment as a .txt document. To create a .txt document in R, go to **New File**, then select **Text file**. You can use any other text editor if you like. Please do not use Mac's Text Edit application, though.
  * DO NOT include the questions in the document you turn in. Answers only!
  * TURN in your assignment on canvas
  * If you are already versed in R, please feel free to substitute out any questions with the [BONUS Content](#bonus-content) at the end of this document. 
  
:white_check_mark: These are the learning objectives associated with each question

-----

## HOMEWORK QUESTION 1 (5 pts) 

:white_check_mark: The purpose is to build curiosity. Students can imagine what R packages will work for their individual goals and projects.

A. Chemistry

B. splots:
https://www.bioconductor.org/packages/release/bioc/html/splots.html
scpdata:
https://www.bioconductor.org/packages/release/data/experiment/html/scpdata.html
motifStack:
https://www.bioconductor.org/packages/release/bioc/html/motifStack.html

C. splots appears easier to learn because it isn't as complex and contains fewer functions. The documentation is much shorter than the other two packages.

## HOMEWORK QUESTION 2 (5 pts)

:white_check_mark: Students will learn how to interface with R and RStudio

*Let's explore R-studio a little bit by learning about shortcut keys. Try the following and report what happens: (answers in words, phrases, or short sentences)**

A. RStudio shows you a "Keyboard Shortcut Quick Reference" guide.

B. It loads your last previously typed command.

C. All of your previous commands disappear from the console.

D. Escape

-----

## HOMEWORK QUESTION 3 (5 pts) 

:white_check_mark: Students will become familiar with a few basic R objects - vectors

:white_check_mark: Students will execute a few basic R functions

*We learned that vectors come in different classes depending on the data type they house. Answer the following in phrases or sentences.*

A.
"users" are characters
"logins" are numeric

B.
They all become characters

C.
```r
super_vector <- as.numeric(users, logins)
```r

num [1:3] NA NA NA

All of the characters become NAs because R can't convert characters to numeric values.

-----

## HOMEWORK QUESTION 4 (5 pts) 

:white_check_mark: Students will become familiar with a few basic R objects - data frames

:white_check_mark: Students will execute a few basic R functions

```
languages <- c("English", "Spanish", "Japanese", "French")
greetings <- c("hello", "hola", "ohio", "bonjour")
partings <- c("bye", "adios", "mata", "salut")
dictionary <- data.frame(languages, greetings, partings)
dim(dictionary)
dictionary

```

-----


## HOMEWORK QUESTION 5 (5 pts)

```
life_expectency_data <- read.csv('/Users/gavinmcewen/Documents/GitHub/CM515-2026/modules/wk_11_rstudio/life-expectancy_1900-2023_CountriesOnly - life-expectancy_1900-2023_CountriesOnly.csv')
```

```
dim(life_expectency_data)
```
[1] 18798     4

```
str(life_expectency_data)
```
'data.frame':	18798 obs. of  4 variables:
 $ Entity                : chr  "Venezuela" "Uruguay" "Ukraine" "Sweden" ...
 $ Code                  : chr  "VEN" "URY" "UKR" "SWE" ...
 $ Year                  : int  1900 1900 1900 1900 1900 1900 1900 1900 1900 1900 ...
 $ Period_Life_Expectancy: num  28 49 36.6 52.2 30.5 ...
 
```
class(life_expectency_data)
```
[1] "data.frame"

```
summary(life_expectency_data)
```
Entity              Code                Year      Period_Life_Expectancy
 Length:18798       Length:18798       Min.   :1900   Min.   :10.99         
 Class :character   Class :character   1st Qu.:1964   1st Qu.:54.88         
 Mode  :character   Mode  :character   Median :1984   Median :65.58         
                                       Mean   :1983   Mean   :63.00         
                                       3rd Qu.:2004   3rd Qu.:72.45         
                                       Max.   :2023   Max.   :86.37      

Country code should be changed character -> factor
```
life_expectency_data$Code <- as.factor(life_expectency_data$Code)
```
-----

# Bonus content

:white_check_mark: Students are encouraged to cultivate their own personal curiosity in R, data science, and programming. Feel free to turn in any of these answers in lieu of Question 1 - 5 if you are experienced user.

  1. Explore the [Base R Cheatsheet](https://iqss.github.io/dss-workshops/R/Rintro/base-r-cheat-sheet.pdf)
  
   What is a function or object you haven't used before? Explore it. Write down what you tried and how it works. Submit code showing what you have done.
    
  2. Explore the [R Graph Gallery](https://www.r-graph-gallery.com/index.html).
  
   Choose a category of R plots that you would like to learn more about. Using the R Graph Gallery pages, wikipedia, and other internet resources, learn how these plots generate their data. Think about which plots you might use in your own research. 

   Next, read through some of the R code in the Gallery associated with each plot. Even if you don't understand the R code, just give it a try. Notice the difference between reading the comments versus the code.

   Write down the type of plot you explored and describe how you would like to use it in your work.

  3. Explore [Our World In Data](https://ourworldindata.org/).

   Click on **Articles By Topic** to activate a pull down menu to explore. You can download any dataset you want. 

   For example, if you go to [Internet access per country over time](https://ourworldindata.org/internet#internet-access), you can see different plots like so...

<img src="webContent/Screen Shot 2023-01-23 at 6.00.02 AM.png" width="600">

   You can select the **Download** menu tab at the bottom, and download the full dataset as a .csv file. Try it! Explore the data you've obtained!

<img src="webContent/Screen Shot 2023-01-23 at 6.00.16 AM.png" width="600">


    Try downloading and importing some of this data. Make a plot. Explain and turn in what you did. 
