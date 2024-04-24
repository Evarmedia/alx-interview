
<div class="panel panel-default" id="project-description">
  <div class="panel-body">
    <h2>Resources</h2>

<ul>
<li><a href="/rltoken/F458nFkW9StJum2zPI4khg" title="What is Pascal&#39;s triangle" target="_blank">What is Pascal&rsquo;s triangle</a></li>
<li><a href="/rltoken/XXMN2RVCCGcF5l5ZnUIv8Q" title="Pascal&#39;s Triangle - Numberphile" target="_blank">Pascal&rsquo;s Triangle - Numberphile</a></li>
<li><a href="/rltoken/q5v0xbgrVxG4Nf-fV-BW2w" title="What are Python Algorithms" target="_blank">What are Python Algorithms</a></li>
</ul>

<h2>Additional Resources</h2>

<ul>
<li><a href="/rltoken/vKf7Spm4xxFMom3x4Jx52g" title="Mock Technical Interview" target="_blank">Mock Technical Interview</a></li>
</ul>

<h2>Must Know</h2>

<p>To successfully complete this project, you should revise the following Python concepts:</p>

<ol>
<li><p><strong>Lists and List Comprehensions</strong>:</p>

<ul>
<li>Understand how to create, access, modify, and iterate over lists.</li>
<li>Utilize list comprehensions for more concise and readable code, especially for generating rows of Pascal&rsquo;s Triangle.</li>
</ul></li>
<li><p><strong>Functions</strong>:</p>

<ul>
<li>Know how to define and call functions.</li>
<li>Pass parameters and return values, particularly how to return a list of lists representing Pascal&rsquo;s Triangle.</li>
</ul></li>
<li><p><strong>Loops</strong>:</p>

<ul>
<li>Use <code>for</code> and <code>while</code> loops to iterate through sequences.</li>
<li>Nested loops may be necessary for generating each row and calculating the values of Pascal&rsquo;s Triangle.</li>
</ul></li>
<li><p><strong>Conditional Statements</strong>:</p>

<ul>
<li>Apply <code>if</code>, <code>elif</code>, and <code>else</code> conditions to implement logic based on the position within Pascal&rsquo;s Triangle (e.g., the edges of the triangle always being 1).</li>
</ul></li>
<li><p><strong>Recursion (Optional)</strong>:</p>

<ul>
<li>While not strictly necessary, understanding recursion can provide an alternative approach to generating Pascal&rsquo;s Triangle.</li>
<li>Recognize base cases and recursive cases for a function that generates the triangle&rsquo;s rows.</li>
</ul></li>
<li><p><strong>Arithmetic Operations</strong>:</p>

<ul>
<li>Perform addition, a fundamental operation for calculating each element of Pascal&rsquo;s Triangle as the sum of the two elements directly above it.</li>
</ul></li>
<li><p><strong>Indexing and Slicing</strong>:</p>

<ul>
<li>Access elements and slices of lists, crucial for identifying and summing the correct elements when constructing each row of the triangle.</li>
</ul></li>
<li><p><strong>Memory Management</strong>:</p>

<ul>
<li>Be mindful of how lists are stored and copied, especially when creating new rows based on the values of the previous row.</li>
</ul></li>
<li><p><strong>Error and Exception Handling (Optional)</strong>:</p>

<ul>
<li>Use try-except blocks as needed to handle potential errors, such as invalid input types or values.</li>
</ul></li>
<li><p><strong>Efficiency and Optimization</strong>:</p>

<ul>
<li>Consider the time and space complexity of different approaches to generating Pascal&rsquo;s Triangle.</li>
<li>Evaluate and apply optimizations to improve the performance of the solution.</li>
</ul></li>
</ol>

<p>By revisiting these concepts, you will be well-prepared to tackle the challenges of implementing Pascal&rsquo;s Triangle in Python, applying both your mathematical understanding and programming skills to develop an efficient and effective solution.</p>

  </div>
</div>


      

      

        
<h2 class="gap">Tasks</h2>

  <div data-role="task11539" data-position="15" id="task-num-0">
      <div class="panel panel-default task-card " id="task-11539">
  <span id="user_id" data-id="150802"></span>

  <div class="panel-heading panel-heading-actions">
    <h3 class="panel-title">
      0. Pascal&#39;s Triangle
    </h3>

  <div>
        <span class="label label-info">
          mandatory
        </span>
    </div>
  </div>

  <div class="panel-body">
    <span id="user_id" data-id="150802"></span>

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Create a function <code>def pascal_triangle(n):</code> that returns a list of lists of integers representing the Pascal&rsquo;s triangle of <code>n</code>:</p>

<ul>
<li>Returns an empty list if <code>n &lt;= 0</code></li>
<li>You can assume <code>n</code> will be always an integer</li>
</ul>

<pre><code>guillaume@ubuntu:~/0x00$ cat 0-main.py
#!/usr/bin/python3
&quot;&quot;&quot;
0-main
&quot;&quot;&quot;
pascal_triangle = __import__(&#39;0-pascal_triangle&#39;).pascal_triangle

def print_triangle(triangle):
    &quot;&quot;&quot;
    Print the triangle
    &quot;&quot;&quot;
    for row in triangle:
        print(&quot;[{}]&quot;.format(&quot;,&quot;.join([str(x) for x in row])))


if __name__ == &quot;__main__&quot;:
    print_triangle(pascal_triangle(5))

guillaume@ubuntu:~/0x00$ 
guillaume@ubuntu:~/0x00$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
guillaume@ubuntu:~/0x00$ 
</code></pre>

  </div>
