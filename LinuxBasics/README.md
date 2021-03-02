# Linux 

The purpose of this document is to give a brief introduction to popular Linux commands. It's recommended that you try to replicate the procedure in a GUI environment (with a mouse). You'll find that once you get the hang of using a terminal, it's much faster than clicking.

FIRST STEP: Open up Windows Explorer or Finder on your windows PC/Mac. Navigate to the desktop, create a new folder, open it, then create a text document. 

If you understand what you just did, then you already have a good grip on navigating directories. We'll be replicating the above steps using a terminal. 

If you have linux already, just open up terminal. If you're running Windows or Mac OS, you can download virtual box and run Ubuntu.

If that's too much work, you can just use this link to follow along (Note, it doesn't come with a Desktop directory, so it's recommended you type `mkdir Desktop` then `cd Desktop` ***(case sensitive)*** once the site loads. The command may not make sense right now, but it will make it easier to follow along. 

# `pwd` (Print Working Directory)
***Note directory is synonmous with folder***

Use this command to find out where you're located. If you're on your desktop, you'll see something like this: `/root/Desktop`

# `cd` (Current Directory)
Use the cd command to navigate to a certain directory. 

Example: 

Let's say you have a folder on your desktop called "dir". To go from your current directory (Desktop) to the folder (dir), just type the command `cd dir`. 

***NOTE:*** this won't work if you're in another directory (say your Documents folder) because the path isn't clear. 

`Desktop --> dir` #Desktop and dir are related

`Documents` #Documents is isolated

Notice that dir and Documents are not related in any way. You can't start in the Documents directory and then try to gain access to dir. If you want to get to dir from Documents, you'll have to naviagte out of the directory, into Desktop, and then into dir. Here are the commands: 

`pwd ` #/root/Documents

`cd .. `#The `..` takes you up one directory (in other words, it takes you out of the current directory, and back to the previous one - in this case, root).

`cd Desktop/dir` #Now that you're out of the Documents folder, you can `cd` into the dir folder, which is located on the Desktop. 

It is ***highly*** recommended you follow these steps in a GUI before replicating them in your terminal. You'll visually see what's happening and understand the process. 

# `mkdir` (Make directory/folder)
This command creates a new folder in your current directory. 
Ex:
If you're on your desktop, and you want to create a folder called my_folder, all you have to do is type: `mkdir my_folder`. A new folder will be created on your desktop. 

To remove a directory, type: `rmdir <name>`. Note, if the directory is not empty, you'll be prompted with an error. 

To delete a non-empty directory, type `rm -rf`. ***NOTE: THIS COMMAND IS DANGEROUS IF NOT USED PROPERLY.*** 

Always be certain of what you are deleting before typing this command. If you're not, type `rm -r` instead (this will prompt you before deleting every file). 

# `ls` (List)

This command shows a list of all documents/ directories in the current directory.
Ex: 
If you're on the desktop and want to know what other directories/ documents are present, type `ls`. You'll see a list of everything on the desktop.

`cd Desktop` #Navigate to the desktop (if you're not already there)

`ls` #(List all other folders/documents on the desktop). 


# `nano` (Basic Text Editor)

The `nano` command does two things at once; it creates a new text document, and then opens a window where you can begin typing into your text document. If you don't follow the nano command with a name, the file will be unnamed until you save and exit. Otherwise, you can just type `nano <name>` and you'll create a text document (in your current directory) with whatever name you supplied. 

The nano editor is a simple text editor (note you will not be able to click, you'll have to use arrow keys to move around). Nano is good for beginners but `vi` is a much more powerful text editor. It's recommended you first get used to using nano before moving onto `vi`. 

To save your text document follow the key combos at the bottom of the screen (ctrl x, y, enter)

To display the contents of a text file, type `cat <name>`. The output will print to the terminal window (if you wish to print the output to another document, refer the redirecting section at the bottom of the page).  

To delete a file, type `rm <name>`

# `vi` (Powerful Text Editor)

As mentioned above,  vi is for "power users." It is capable of far more than a basic text editor (nano). 

Note, vi is not complicated; it's just different than what you're probably used to. There are plenty of tutorials online that will explain how to use vi properly. Here, we'll just go over how to insert text, save, and exit. 

`vi text_file` #create a new file called text_file and open in vi

type `i` this puts you in insert mode (so you can start typing).

Type what ever you'd like, then hit `esc`, `:wq`. You'll save and exit your text document.

***Quick Example of VI Capabilities***

`vi file`

`i` #insert mode

`Hello world`

`I'm writing on a new line.`

To delete a whole line of text in a basic editor, you'd have to start from the end and hold delete/backspace. In vi, you can just type `esc`, `dd`. Now the entire line is gone. You can type `u` to undo the command. This is one of MANY vi features, and is simply supposed to introduce you to what can be done with a powerful text editor.

# Important Concepts

We've just gone over a few basic terminal commands. There are MANY more, but these should give you a good grip on the basics. Next we'll going over some basic concepts (piping and redirecting). This is a little more advanced, but not especially difficult. It is recommended that you have a solid foundation on the above examples before moving forward. 

# Piping

Piping is a form of redirection. It can be used to route output in any direction/location you want.

Here's an example:

Let's say your on the Desktop and you have three directories (a, b,c, apple, carrot, christopherColumbus). 

To see a list of those directories, you'd just type `ls`. 

***Output:***

a

b

c

apple

carrot

christopherColumbus


Now, if you wanted to search for directories that had the letter 'a' in them, you'd use the grep command (grep = search). 

To list out all the directories with ONLY a, type: `ls | grep a`

The ls stands for list, and the | acts as a pipe. We're directing the output to only feed through directories/documents that contain the letter 'a'. 

OUTPUT: 

a

apple

carrot

Note, `ls grep a` does not work. Ask yourself this if you don't understand why: what are you trying to execute? ls, grep, or a? How is the computer supposed to know what  you're talking about? The `|` allows you to "funnel" the output and get only what you want. 

Another note, you can have multiple `|` in an expression. 

Ex: 

`ls | grep a | grep c`

Start with `grep c`. This will list only the documents/directories that contain the letter c.

The `grep a` then funnels the output further; only output that contains the letter a will be listed. 

***OUTPUT:***

carrot

***Note, christopherColumbus and 'c' will not be listed because they do not contain the letter a - thus the term, piping/funneling***


# Redirecting

Redirecting relies on the following two symbols: `<` & `>`. They are fairly simple to use if you think about the acute angled side as the funnel. 

Example: 

INPUT > FUNNELED OUTPUT

Practical Example:

Let's say you want to print the contents of one file to another. This can be accomplished with redirecting. 

  `touch file file2` #touch creates a file without opening a text editor. In this case, we've created two files, file & file2.
  
  `nano file` #open the text editor for file, write anything you want. In this case, we'll just write `Hello World`. 
  
  Now to transfer the contents of file to file2, we'll "redirect" the output of the `cat` command.
  
  `cat file > file2` Now the contents of file2 have been replaced with the contents of file. If you wish to append rather than replace, use >> instead.
  
  `cat file >> file2` 
  
  To check that the transfer was successful, type `cat file2`. The output should now match file.
  
  You've made it to the end of this brief introduction of Linux. If you understand the above steps, you have an excellent foundation. With practice, you'll be able to get around a terminal with no issue at all. 
  
  Recommended next steps: 
    
    1). PRACTICE PRACTICE PRACTICE!

    2). STUDY THE ps command and understand how to kill/restart processess.

    3). KEEP PRACTICING!

***Author: Rakan Kandah***

