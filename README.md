# Python Intersecting Rectangles

A Python system to compare the oposite coordinates in 2 rectangles and determine if they intersect.

## Features
- Input top left and bottom right coordinates of 2 rectagles
- Calculate all corner coodinates of the 2 rectangles
- Algorithimcly determine if the 2 rectangles intercent
- Buult in Unit Testing


## Examples 

<details>
<summary>Click to view overlapping example</summary>
  
```
Info for rectangle 1
Enter X coordinate 1 (top left)0
Enter Y coordinate 1 (top left)10
Enter X coordinate 2 (bottom right)10
Enter Y coordinate 2 (bottom right)0
Info for rectangle 2
Enter X coordinate 1 (top left)1
Enter Y coordinate 1 (top left)11
Enter X coordinate 2 (bottom right)9
Enter Y coordinate 2 (bottom right)-1
True
```
</details>

<details>
<summary>Click to view non overlapping example</summary>
  
```
Info for rectangle 1
Enter X coordinate 1 (top left)0
Enter Y coordinate 1 (top left)10
Enter X coordinate 2 (bottom right)10
Enter Y coordinate 2 (bottom right)0
Info for rectangle 2
Enter X coordinate 1 (top left)-5
Enter Y coordinate 1 (top left)10
Enter X coordinate 2 (bottom right)-1
Enter Y coordinate 2 (bottom right)0
False
```
</details>

<details>
<summary>Click to view testing results</summary>
  
```
  .................
  ----------------------------------------------------------------------
  Ran 17 tests in 0.000s

  OK
```
</details>

## Requirements
- Python (tested) 3.13.7+
- [Unittest (tested) 3.14+](https://docs.python.org/3/library/unittest.html)

