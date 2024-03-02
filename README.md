# EFFICIENCY PROFICIENCY

ALEXANDER RODRIGUEZ

JANUARY 4, 2024

## Abstract

To solve the problem of identifying the most time-efficient sorting algorithm of the insertion, bubble, gnome, merge, and selection algorithms, each one was programmed into a python file. This file sorted the same list of two hundred fifty-six characters one hundred times using each algorithm and recorded the time of each trial. When the program was completed, the average time elapsed for each was as follows: insertion sort, 0.65ms; bubble sort, 7.41ms; merge sort, 0.43ms; gnome sort, 4.36ms; and selection sort, 1.35ms. Merge sort averaged sorting in the least amount of time, indicating that it is the most time-efficient algorithm, as was the hypothesis.

## Background

Whether it’s sorting books on a bookshelf, shirts in a closet, or files in a folder, people have used many different techniques, or algorithms, for sorting. Some of these algorithms are significant time-savers, while others are notoriously time-inefficient.

One such algorithm is called “insertion sort”. In a list of items, insertion sort first removes all the items, then takes each item one at a time and inserts it where it should go relative to the items already inserted. Most people use this algorithm to put books on a bookshelf without even knowing it. On average, this algorithm works in quadratic time (Programiz), which is relatively slow.

Another such algorithm is bubble sort. When sorting a list of items, it continually goes through the whole list two items at a time and swaps each consecutive two that aren’t in the correct order, until the whole list is eventually sorted. (ProductPlan) This algorithm is commonly used to sort shirts in partially-sorted closets. Bubble sort also works in quadratic time, on average (Christian and Griffiths, 65–66).

Merge sort starts by dividing all the items into sorted piles of two items each. It then takes two piles and “merges” them into one by continually comparing the first items of both piles and inserting the one that should come first into the new pile, until both piles have been fully merged. This process is repeated until there is only one pile left: the sorted list. This algorithm can be used to quickly sort a deck of cards. Mergesort works in linearithmic time, which is faster than quadratic (Christian and Griffiths, 64–65, 68).

Gnome sort, an algorithm similar to bubble sort, goes through each item in a list, comparing two at a time. If two consecutive items are in order, the latter item and the next item are then compared. If not, they are swapped, and the previous two items are compared again. If there are no previous items, it then compares the latter and next again. Like the first two algorithms, on average, gnome sort works in quadratic time (NLST).

Lastly is selection sort, which sorts a list one item at a time from beginning to end. It repeatedly goes through the unsorted portion of the list, finds the item that would come first, and swaps its position with the foremost unsorted item. The list is fully sorted when the second-to-last item has been swapped. Selection sort always works in quadratic time.

The problem in this project is to answer this: “Of the insertion, bubble, merge, gnome, and selection sorting algorithms, which one is the most time-efficient?” This is important to know because of how much sorting is done both by people and computers. The hypothesis is that merge sort will sort a list in the smallest amount of time. This is the most likely because sources indicate that mergesort works in linearithmic time, whereas the other four work in quadratic.

## Materials

- Windows computer
- DIGITAL
  - Windows command prompt
  - Python interpreter
  - Visual Studio Code
  - Unsorted list of two hundred fifty-six items

## Experimental Procedure

1. Download any required software:
    1. Windows command prompt is installed on a Windows computer by default.
    2. Python interpreter: <https://www.python.org/downloads/>
    3. Visual Studio Code: <https://code.visualstudio.com/download>
2. Create an empty python file
3. Define variables:
    1. “trials”: the number of trials to run using each algorithm (100).
    2. “roundTo”: the number of digits to round the average execution times to (2).
    3. “array”: an unordered list of two hundred fifty-six items, each item being two capital letters: \['KO', 'JG', 'OA', …\].
4. Create five functions, one for each algorithm; each of these functions creates a copy of the unordered list then sorts the copy alphabetically using its corresponding algorithm.
5. Create a function to time each of the functions after executing them the number of times specified by the “trials” variable, which in this case is one hundred. This function will calculate the average execution time of all the trials in milliseconds. Python’s “timeit” module will be used to get the time in seconds, which can then easily be converted.
6. Print (meaning display) some basic information along with each of the algorithm names followed by their respective average execution speeds rounded to the number of places specified by the “roundTo” variable, which in this case is two.
7. Record the results.

## Data

Table one shows the expected time complexity of the algorithms in Big-O notation. In Big-O notation, _n_ represents the number of items in the list to be sorted. Though this notation can’t be directly converted into units such as seconds, it shows how fast sorting time grows proportionally to the size of the list.

| **Algorithm:** | **Insertion Sort** | **Bubble Sort** | **Merge Sort** | **Gnome Sort** | **Selection Sort** |
| --- | --- | --- | --- | --- | --- |
| Average Time Complexity: | Quadratic | Quadratic | Linearithmic | Quadratic | Quadratic |
| --- | --- | --- | --- | --- | --- |
| Average: | O(n<sup>2</sup>) | O(n<sup>2</sup>) | O(n log n) | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| --- | --- | --- | --- | --- | --- |
| Worst: | O(n<sup>2</sup>) | O(n<sup>2</sup>) | O(n log n) | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| --- | --- | --- | --- | --- | --- |
| Best: | O(n) | O(n) | O(n log n) | O(n) | O(n<sup>2</sup>) |
| --- | --- | --- | --- | --- | --- |

Figure one shows the average time elapsed of each algorithm for each trial in milliseconds.

![Figure One](https://raw.githubusercontent.com/the-web-crawler/efficiency-proficiency-stem-project/main/res/bar_graph.png)

Figure two shows the average time elapsed of each algorithm for each trial in percentages.![Average Time Elapsed in Percentages](https://raw.githubusercontent.com/the-web-crawler/efficiency-proficiency-stem-project/main/res/pie_chart.png)

## Discussion

Since one hundred consistent trials were conducted, the results are highly accurate. Merge sort takes the smallest amount of time to sort a list, so the hypothesis that it is the most time-efficient has been proven correct. Despite the fact that the time elapsed for merge sort and insertion sort is relatively close, the trials consistently showed that merge sort is faster.

The hypothesis was based on research that showed that merge sort sorts a list in linearithmic time, whereas the other four algorithms all take quadratic time to sort. In other words, the other four take _n<sup>2</sup>_ time, where _n_ represents the number of items in the list. Merge sort, however, only takes _n log n_ time.

There are multiple limitations to the study, however. One such limitation is the fact that two of the algorithms, bubble sort and gnome sort, actually sort faster the more organized the unordered list already is. In fact, if the list were already sorted, it would “sort” the list in linear time, which is simply _n_.

Another limitation is that merge sort is the most unintuitive of the five algorithms. It may be difficult for humans to do in real-world scenarios, unlike insertion sort and bubble sort, which are both inefficient yet intuitive.

One final limitation is that merge sort, along with insertion sort, requires a place to temporarily store items, which may not always be viable in real-world scenarios. However, the experiment itself, having been done by computer, was not restrained by these limitations.

## Bibliography

“Big-O Notation: A simple explanation with examples.” LinkedIn. <https://www.linkedin.com/pulse/big-o-notation-simple-explanation-examples-pamela-lovett/> (accessed January 8, 2024).

“Bubble Sort.” ProductPlan. <https://www.productplan.com/glossary/bubble-sort/> (accessed October 2, 2023).

“Bubble Sort.” Programiz. <https://www.programiz.com/dsa/bubble-sort> (accessed January 6, 2024).

Christian, Brian, and Griffiths, Tom. _Algorithms to Live by: The Computer Science of Human Decisions_. Henry Holt and Company, 2021.

“gnome sort.” NLST. <https://xlinux.nist.gov/dads/HTML/gnomeSort.html> (accessed October 2, 2023).

“Insertion Sort Algorithm.” Programiz. <https://www.programiz.com/dsa/insertion-sort> (accessed October 2, 2023).

“Selection Sort – Data Structure and Algorithm Tutorials.” GeeksforGeeks. <https://www.geeksforgeeks.org/selection-sort/> (accessed October 2, 2023).
