# Lesson 1

In this lesson we have two goals:
1. Learn how to navigate your file structure using the command line (terminal, bash, command prompt, etc)
2. Start taking a look at how a simple REST API works

To do these you will only a computer with access to a web browser.
We will not be doing any complicated programming in this lesson.

## Command Line Interface
You might be wondering why we care about learning to use the command line interface.
The answer is actually very simple: it is a very powerful tool that basically every computer will have.
In fact some computers don't even have a graphical user interface, that is an environment with windows and mouse pointers.
This is especially true for most web servers.
They exists in a _headless_ configuration, that is to say without a monitor attached.
The only way to use these machines is to connect remotely in to a command line interface from your own computer.

Now, we don't have to become experts, but we need to be able to do a set of basic tasks, and become confident about searching online when we don't know how to do something. Let's start by first opening up our command line interface (cli). 
In Windows you'll generally have two options: command prompt or PowerShell.
I recommend using PowerShell; command prompt has its own set of commands, that while not difficult to use, would be harder to teach since PowerShell uses the same commands found in Linux and Mac. 
Having said in Linux and Mac you just need to open a terminal. 
On Mac you can use Spotlight to search for terminal, while on Linux you can do the same but some Linux distros will give you a variety of terminal options. 
If in doubt use bash.

The first thing we need to do is figure out _where_ we are.
That is what folder we're currently working in.
This can be done with the `pwd` command, which stands for Print Working Directory.

![print working directory](pwd.png)

Now that we know where we are, we can worry about _files_ are in this directory.
We can _list_ the files in the directory by using the `ls` command.
You'll obviously see different directories and files listed for your own computer.

![list files and directories](ls.png)
(Aside: One of the big differences if you decide to use command prompt is that `ls` is not a command, instead you use `dir`)

Now that we know where we are and what is around us, we need to figure out how to _go_ there.
For this we'll use the `cd` command to Change Directories.
Unless you've drastically changed your computer you'll have a Desktop folder.
Let's go there by using `cd Desktop`.
It is imporant that you match the case of the directory (lowercase vs uppercase), but for longer names you can use TAB to autocomplete.

![change directory](cd.png)

Notice how the line you normally type in changed when you cd'ed into your Desktop.
You can use this to complement `pwd`.
I did use `pwd` here for completeness though.

If you want to go back _up_ to the previous directory we were in, you would use `cd ..`.
That is two dots.
This will move you one directory up the hierarchy.

We're almost done this section, we just need to learn two more basic things: how to make a directory (also called a folder) and how to find the documentation for commands.

Making a directory is super easy.
First make sure you are in the right place to make your new folder.
Then call `mkdir <name of new directory>`.
This stands for Make Directory with the following name.

![make a new directory](mkdir.png)

If you want to use Spaces in the name of the directory you'll need to escape them with a backslash.
For example `mkdir My\ Brand\ New\ Folder`.
I generally recommend you stick to using underscores and hyphens if you need to space out text as using Spaces tends to get tedious because of all the escape characters.

Now what happens if you see some useful code in StackOverFlow, but you want to know how, or why it works?
This is why we have documentation.
The documentation will explain to you the function of a command and the syntax to use it.
Some documentation will even give you useful examples so that you can see how to use the command in question.
We can bring up the documentation with `man <command>`; ie get the manual for the command.
Let's try with `ls`

![get the manual for ls](man.png)

Once you're in you can scroll down using the arrow keys, and quit using `q`.

Try reading the documentation for the `cat` command.
Can you imagine use cases where it might be useful?
