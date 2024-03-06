# B. Determining the Insertion Index

|                    |                          |
|--------------------|--------------------------|
|Time limit          |1 second                  |
|Memory limit        |64.0 MB                   |
|Input               |standard input or input.txt|
|Output              |standard output or output.txt|

The Mars rover transmits an array of data about the concentration of marsium in the soil back to Earth. The array is sorted in ascending order.

On Earth, scientists need to determine whether a specific concentration of marsium is present in the array. For this, they require a program that searches the array for a given concentration - the target value.

If the array contains the target value, the program should return the index of the first element that contains this value.

If the target value is not in the array, the program should return the index at which this value could be located in the array.

Thus, the task is to find the index of the target value in the sorted array or determine the index at which this value could be.

Write a program that takes an array and a target value as input and returns the index of the array where the target value is or should be located.

## Input format

The first line is an array of integers separated by spaces.

The second line is the target value.

## Output format

An integer: the index of the target value in the existing array if it is there, or the index at which this value should be if it is not in the array.
