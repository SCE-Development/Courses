# Linux 

The purpose of this document is to give a brief introduction to popular Linux commands. It's recommended that you try to replicate the procedure in a GUI environment (with a mouse). You'll find that once you get the hang of using a terminal, it's much faster than relying on a mouse.

FIRST STEP: Open up Windows Explorer or Finder on your windows PC/Mac. Navigate to the desktop, create a new folder, open it, then create a text document. 

If you understand what you just did, then you already have a good grip on naviagating directories. We'll be replicating the above steps using a terminal. 

# `pwd` (Print Working Directory)
***Note directory is synonmous with folder***

Use this command to find out where you're located. If you're on your desktop, you'll see something like this: `/root/Desktop`

# `cd` (Current Directory)
Use the cd command to navigate to a certain directory. 

Example: 

Let's say you have a folder on your desktop called "dir". To go from your current directory (Desktop) to the folder (dir), just type the word `cd dir`. 

***NOTE:*** this won't work if you're in another directory (say your Documents folder) because the path isn't clear. 

Here's a visual: 

Desktop --> dir

Documents

Notice that dir and Documents are not related in any way. You can't start in the Documents directory and then try to gain access to dir. If you want to get to dir from Documents, you'll have to naviagte out of the directory, into Desktop, and then into dir. Here are the commands: 

`pwd ` #/root/Documents

`cd .. `#The `..` takes you up one directory (in other words, it takes you out of the current directory, and back to the previous one - in this case, root).

`cd Desktop/dir` #Now that you're out of the Documents folder, you can `cd` into the dir folder, which is located on the Desktop. 

It is ***highly*** recommended you follow these steps in a GUI before replicating them in your terminal. You'll visually see what's happening and understand the process. 

# `mkdir` (Make directory/folder)
This command creates a new folder in your current directory. 
Ex:
If you're on your desktop, and you want to create a folder called my_folder, all you have to do is type: `mkdir my_folder`. A new folder will be created on your desktop. 

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

To delete a whole line of text in a basic editor you'd have to start from the end and hold delete/backspace. In vi, you can just type `esc`, `dd`. Now the entire line is gone. You can type `u` to undo the command. This is one of MANY vi features, and is simply supposed to introduce you to what can be done with a powerful text editor.

# Important Concepts

We've just gone over a few basic terminal commands. There are MANY more, but these should give you a good grip on the basics. Next we'll going over some basic concepts (piping and redirecting). This is a little more advanced, but not especially difficult. It is recommended that you have a solid foundation on the above examples before moving forward. 

# Piping

# Redirecting

***Author: Rocky Kandah***

