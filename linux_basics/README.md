# Linux 
You've heard about it, and you've probably used it without knowing, but what is it?


Well first and foremost, it's an operating system, much like Windows and Mac OS. The only difference is it's open source, which means other people can contribute to it. This is the reason there's so many "flavors" of Linux (***Ubuntu, CentOS, the list goes on...***)

The purpose of this document is to give a brief introduction to popular Linux commands. It's recommended that you try to replicate the procedure in a GUI environment (with a mouse). You'll find that once you get the hang of using a terminal, it's much faster than clicking around with a mouse. 

FIRST STEP: Open up Windows Explorer or Finder on your windows PC/Mac. Navigate to the desktop, create a new folder, open it, then create a text document. 

If you understand what you just did, then you already have a good grip on naviagating directories. We'll be replicating the above steps using a terminal. 

# `pwd` (Print Working Directory)
***Note directory is synonmous with folder***

Use this command to find out where you're located. If you're on your desktop, you'll see something like this: `/root/Desktop`

# `cd` (Current Directory)
Use the cd command to navigate to a certain directory. 

Example: 

Let's say you have a folder on your desktop called "dir". To go from your current directory (Desktop) to the folder (dir), just type the word `cd dir`. 

***NOTE:*** this won't work if you're in another directory (say your home folder) because the path isn't clear. 

Here's a visual: 

Desktop --> dir

Documents

Notice that dir and Documents are not related in any way. You can't start in the Documents directory and then try to gain access to dir. If you want to get to dir from Documents, you'll have to naviagte out of the directory, into Desktop, and then into dir. Here are the commands: 

`pwd ` #/root/Desktop

`cd .. `#The `..` takes you up one directory (in other words, it takes you out of the current directory, and back to the previous one).

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

To save your text document follow the key combos at the bottom of the screen (ctrl x, y, enter).

CONCEPT: piping
CONCEPT: redirecting
And probably more commands, stay tuned!
Rocky Kandah

