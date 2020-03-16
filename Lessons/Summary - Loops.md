# Summary: Loops

In this section you learned that:

- **For loops**  are useful for executing a command over a large number of items.

- You can create a  **for loop**  like so:

1. for letter in&#39;abc&#39;:
2.     print(letter.upper())

Output:

A
B
C

- The name after for (e.g. letter) is just a variable name

- You can loop over  **dictionary keys** :

1. phone\_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
2. for value in phone\_numbers.keys():
3.     print(value)

Output:

John Smith
Marry Simpsons

- You can loop over  **dictionary values** :

1. phone\_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
2. for value in phone\_numbers.values():
3.     print(value)

Output:

+37682929928
+423998200919

- You can loop over  **dictionary items** :
  1. phone\_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
  2. for key, value in phone\_numbeitems():
  3.     print(key, value)

Output:

(&#39;John Smith&#39;, &#39;+37682929928&#39;)

(&#39;Marry Simpons&#39;, &#39;+423998200919&#39;)

- **While loops**  will run as long as a condition is true:
  1. while datetime.datetime.now() \&lt; datetime.datetime(2090, 8, 20, 19, 30, 20):
  2.     print(&quot;It&#39;s not yet 19:30:20 of 2090.8.20&quot;)

The loop above will print out the string inside print() over and over again until the 20th of August, 2090.
