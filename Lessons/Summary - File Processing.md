# Summary: File Processing

In this section you learned that:

- You can  **read**  an existing file with Python:

1. with open(&quot;file.txt&quot;) as file:
2. content = file.read()

- You can  **create**  a new file with Python and  **write**  some text on it:

1. with open(&quot;file.txt&quot;, &quot;w&quot;) as file:
2. content = file.write(&quot;Sample text&quot;)

- You can  **append**  text to an existing file without overwriting it:

1. with open(&quot;file.txt&quot;, &quot;a&quot;) as file:
2. content = file.write(&quot;More sample text&quot;)

- You can both  **append and read**  a file with:

1. with open(&quot;file.txt&quot;, &quot;a+&quot;) as file:
2. content = file.write(&quot;Even more sample text&quot;)
3. file.seek(0)
4. content = file.read()