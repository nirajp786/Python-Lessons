# Summary: List Comprehensions

In this section you learned that:

- A list comprehension is an expression that creates a list by iterating over another container.
- A  **basic ** list comprehension:
  1. [i\*2for i in[1,5,10]]

Output: [2, 10, 20]

- List comprehension with  **if**  condition:
  1. [i\*2for i in[1,-2,10]if i\&gt;0]

Output: [2, 20]

- List comprehension with an  **if**   **and**   **else**  condition:
  1. [i\*2if i\&gt;0else0for i in[1,-2,10]]

Output: [2, 0, 20]
