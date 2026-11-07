import pywhatkit as kt

txt = """Python is a popular and powerful programming language that is widely used for software development, 
web applications, data science, artificial intelligence, automation, and many other fields. 
It was created by Guido van Rossum and is known for its simple and easy-to-read syntax, 
making it an excellent choice for beginners as well as experienced programmers. 
Python allows developers to write programs with fewer lines of code compared to many other programming languages, 
which increases productivity and reduces complexity."""

kt.text_to_handwriting(txt, "handwriting.png", [0, 0, 138])
print("Handwriting image generated successfully!")