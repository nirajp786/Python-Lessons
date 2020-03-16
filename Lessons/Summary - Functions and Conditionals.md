# Summary: Functions and Conditionals

In this section you learned to:

- Define a  **function** :

1. def cube\_volume(a):
2.     return a \* a \* a

- Write a  **conditional ** block:

1. message = &quot;hello there&quot;
2.
3. if&quot;hello&quot;in message:
4.     print(&quot;hi&quot;)
5. else:
6.     print(&quot;I don&#39;t understand&quot;)

- Write a conditional block of  **multiple conditions** :

1. message = &quot;hello there&quot;
2.
3. if&quot;hello&quot;in message:
4.     print(&quot;hi&quot;)
5. elif&quot;hi&quot;in message:
6.     print(&quot;hi&quot;)
7. elif&quot;hey&quot;in message:
8.     print(&quot;hi&quot;)
9. else:
10.     print(&quot;I don&#39;t understand&quot;)

- Use the and operator to check if  **both conditions**  are True at the same time:

1. x = 1
2. y = 1
3.
4. if x == 1 and y==1:
5.     print(&quot;Yes&quot;)
6. else:
7.     print(&quot;No&quot;)

Output is Yes since both x and y are 1.

- Use the r operator to check if  **at least one condition**  is True:

1. x = 1
2. y = 2
3.
4. if x == 1 r y==2:
5.     print(&quot;Yes&quot;)
6. else:
7.     print(&quot;No&quot;)

Output is Yes since x is 1.

- Check if a value is of a certain  **type**  with:

1. isinstance(&quot;abc&quot;, str)
2. isinstance([1, 2, 3], list)

or

1. type(&quot;abc&quot;) == str
2. type([1, 2, 3]) == lst
