# Summary: Processing User Input

In this section you learned that:

- A Python program can get  **user input**  via the input function:

- The  **input**   **function**  halts the execution of the program and gets text input from the user **:**

1. name = input(&quot;Enter your name: &quot;)

- The input function converts any  **input to a string** , but you can convert it back to int or float:

1. experience\_months = input(&quot;Enter your experience in months: &quot;)
2. experience\_years = int(experience\_months) / 12

- You can  **format strings**  with (works both on Python 2 and 3):

1. name = &quot;Sim&quot;
2. experience\_years = 1.5
3. print(&quot;Hi %s, you have %s years of experience.&quot; % (name, experience\_years))

Output: Hi Sim, you have 1.5 years of experience.

- You can also  **format strings**  with (Python 3 only):

1. name = &quot;Sim&quot;
2. experience\_years = 1.5
3. print(&quot;Hi {}, you have {} years of experience&quot;.format(name, experience\_years))

Output: Hi Sim, you have 1.5 years of experience.
