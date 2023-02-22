import webbrowser
def first():
    hi = input("Hi! This is our first lesson for python, now u will underastand what <Terminal> and why it is important for us! press Enter for continue")
    hi2 = input("Terminal uses for intreract with computer. When we code saomething and after press Run - button (it looks like a corner), we start our code and in the terminal u'll watch the result. If all are ok - press Enter")
    print_func = input("For output some information to the Terminal, you have to write a command that will display text on the screen, this command - <print> command <print> we use like this: with quotation marks ('and text what u want')")


    print("Well Done! Now we'll open to u special site for practice! Also I'll give u some excercise ")

    webbrowser.open("https://www.programiz.com/python-programming/online-compiler/")

    print("""
    OK!
    Well Done! Now u need go to programiz and PrAcTiCe!
    """)
    hi3 = input("OK! Now u need code a command for output in console <Hello World>")
    while hi3 != 'print ("Hello World")' or hi3!='print("Hello world")' or hi3!='print("hello world")' or hi3!='print("hello World")' or hi3!="print('Hello World')" or hi3!="print('Hello world')"or hi3!="print('hello World')"or hi3!="print('hello World')":
        if hi3[:4]!='print':
            hi3 = input("Bro, u forgot abt command <print>. Try again and input your code again here: ")
        elif hi3[5]!='(':
            hi3 = input("Well Done! But u forgot about brackets after print")
        elif hi3[6]!="'" or '"':
            hi3 = input("The last step - to put quatations marks after <print()>. Try again pls: ")


def lesson2():
    l2a = input("Hi it is <Python Without Knowing Programming> lesson 2 name of this lesson - Input information from the keyboard. If u want contine - Press <Enter>")
    l2b = input("""input (): This function first takes the input from the user and converts it into a string.
  The type of the returned object always will be <type ‘str’>. 
  It does not evaluate the expression it just returns the complete statement as String.
  For example, Python provides a built-in function called input which takes the input from the user.
  When the input function is called it stops the program and waits for the user’s input.
  When the user presses enter, the program resumes and returns what the user typed. If u want to understand how does thin function press <Enter> """)
    l2c = input("""When input() function executes program flow will be stopped until the user has given input.
The text or message displayed on the output screen to ask a user to enter an input value is optional i.e. the prompt, which will be printed on the screen is optional.
Whatever you enter as input, the input function converts it into a string.
if you enter an integer value still input() function converts it into a string.
You need to explicitly convert it into an integer in your code using typecasting. If all is clear and u're ready to do the tasks - press <Enter>""")
    l2qa = input("Using input() function ask for user's name. Use the variabel name it will be easier for u, but python doesn't care abt variables names Input your code here: ")
    while l2qa[0:3] != 'name' and l2qa[4] != '=' and l2qa[5:9]!= 'input' and l2qa[10] != '(' and l2qa[11] != "'" or l2qa[11] != '"':
        if l2qa[0:3] != 'name':
            l2qa = input("Hey! U forgot code in yourvariable Try again! Input your NEW code here: ")
        elif l2qa[4] != '=':
            l2qa = input("Hey! U forgot code in your  <=> after the variable Try again! Input your NEW code here: ")
        elif l2qa[5:9]!= 'input':
            l2qa = input("Hey! U forgot in your code <input> Try again! Input your NEW code here: ")
        elif l2qa[10] != '(':
            l2qa = input("Hey! U forgot in your code <(> after <name = input> Try again and input your code again here: ")
        elif l2qa[11] != '"' or l2qa[11] != "'":
            l2qa = input("Hey U forgot quotation marks after <name = input> Try again and input your code again here: ")

print("Perfect! We're done!!! Now u're ready to go and learn Python normally! I'll open the Youtube chane for continue your education")
webbrowser.open("https://www.youtube.com/watch?v=XKHEtdqhLK8")
