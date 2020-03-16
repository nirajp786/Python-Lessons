# Summary: More on Functions

In this section you learned that:

- Functions can have more than one  **parameter** :

1. def volume(a, b, c):
2.     return a \* b \* c

- Functions can have  **default**  parameters (e.g. coefficient):

1. def converter(feet, coefficient =2808):
2.     meters = feet / coefficient
3.     return meters
4.
5. print(converter(10))

Output: 3.0480370641306997

Arguments can be passed as  **non-keyword**  (positional) arguments (e.g. a) or  **keyword**  arguments (e.g. b=2 and c=10):

1. def volume(a, b, c):
2.     return a \* b \* c
3.
4. print(volume(1, b=2, c=10))

- An  **\*args ** parameter allows the  function to be called with an arbitrary number of non-keyword arguments:

1. def find\_max(\*args):
2.     return max(args)
3. print(find\_max(3,99,1001,2,8))

Output: 1001

- An  **\*\*kwargs**  parameter allows the function to be called with an arbitrary number of keyword arguments:

1. def find\_winner(\*\*kwargs):
2.     return max(kwargs, key = kwargs.get)
3.
4. print(find\_winner(Andy=17,Marry=19,Sim=45,Kae=34))

Output: Sim

- Here&#39;s a summary of function elements:
<img src="https://i.udemycdn.com/redactor/raw/2019-07-24_19-07-36-0d306e1785ef65d50aeb204567dfb62f.png"
     alt="Functions"
     style="float: left; margin-right: 10px;" />
