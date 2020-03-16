# Summary: Positive/Negative Indexes, Slicing

In this section you learned that:

- Lists, strings, and tuples have a  **positive index**  system:

1. [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2.    0      1      2      3      4      5      6

- And a  **negative index**  system:

1. [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2.   -7     -6     -5     -4     -3     -2     -1

- In a list, the  **2nd** ,  **3rd** , and  **4th**  items can be accessed with:

1. days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2. days[1:4]
3. Output: [&#39;Tue&#39;, &#39;Wed&#39;, &#39;Thu&#39;]

- **First three items of a list** :

1. days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2. days[:3]
3. Output:[&#39;Mon&#39;, &#39;Tue&#39;, &#39;Wed&#39;]

- **Last three items of a list** :

1. days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2. days[-3:]
3. Output: [&#39;Fri&#39;, &#39;Sat&#39;, &#39;Sun&#39;]

- **Everything but the last** :

1. days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2. days[:-1]
3. Output: [&#39;Mon&#39;, &#39;Tue&#39;, &#39;Wed&#39;, &#39;Thu&#39;, &#39;Fri&#39;, &#39;Sat&#39;]

- **Everything but the last two** :

1. days = [&quot;Mon&quot;, &quot;Tue&quot;, &quot;Wed&quot;, &quot;Thu&quot;, &quot;Fri&quot;, &quot;Sat&quot;, &quot;Sun&quot;]
2. days[:-2]
3. Output: [&#39;Mon&#39;, &#39;Tue&#39;, &#39;Wed&#39;, &#39;Thu&#39;, &#39;Fri&#39;]

- A single in a  **dictionary**  can be accessed using its key:

1. phone\_numbers = {&quot;John Smith&quot;:&quot;+37682929928&quot;,&quot;Marry Simpons&quot;:&quot;+423998200919&quot;}
2. phone\_numbers[&quot;Marry Simpsons&quot;]
3. Output: &#39;+423998200919&#39;
