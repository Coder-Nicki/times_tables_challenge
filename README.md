# timesTable Challenge

[Github Repository](https://github.com/Coder-Nicki/times_tables_challenge)

## Overview
This terminal application allows users to practise their multiplication skills and to race to complete all the levels in time to be crowned the champion. This app is aimed at students of all ages looking to improve their skills in this mathematical ability.

## Code Styling Guide

- [Pep8 styling guide](https://peps.python.org/pep-0008/)

## Features

The first feature of this application is 'Game Mode'. Users start at level one and have to answer multiplication sums correctly in order to move up to the next level. However, if they get too many wrong, or take too long to answer them, then they are out of the game. There are 10 levels that all increase in difficulty. Can you be named the champion and complete all levels successfully?

The second feature is the 'Practice Mode'. Users can choose out of 3 difficulty levels to practise. The levels are easy, medium and hard. During the practise time, the correct and incorrect answers are recorded. The time is also recorded so the user knows how long it took them to answer so many questions. Each practice level has a limit of 100 questions, before they are automatically exited from that mode. The user is also able to exit whenever they like by pressing 'q'.

The third feature is the One Minute Challenge mode. This mode allows the user to see how many questions they can answer correctly in one minute.

Time is a key feature of all modes. The time taken to answer questions is recorded and then printed back to the user. 

The application also utilises a terminal menu so that the user can easily choose where they want to go in the application. 

## Implementation Plan

[Trello board](https://trello.com/b/Q7epZ4TZ/timestables-challenge)

The implementation of this application has gone according to plan. A flowchart was created first. Code was then written for each feature. Unit and manual tests started to be done. The README was updated. Then instructions and a bash script created for others to acces app.

Two things to improve still are: 

- More unit testing
- A better end/exit message that utilises terminal art or animation

## Manual Testing
| Feature | Expected Outcome | Actual Outcome | Any remaining issues|
| --------- | ----- | ----- | ----- |
|User is asked to input name | User's name appears on welcome message | As expected | Nil|
|Main menu is linked to chosen mode| After the user presses on the item, a new screen opens up with chosen mode| As expected| Nil|
| Exit mode exits out of the whole app| When user presses exit mode the app terminates| As expected | Nil|
|In game mode, the user goes onto the next level when previous level is successfully achieved| Level one calls for level two. Level two calls for level 3, et cetera| As expected|Nil|
|User gets 3 questions wrong| If user gets 3 questions wrong then they get a printed message and they are returned to the main menu|As expected|Nil|
|User is too slow| If user's time is over the given time than they are exited from the game to the home menu|As expected|Nil|
|The given times are all correct in each level. Check each level. |Each level has a certain time before they fail the level|As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|
|||As expected|Nil|


## Help Documentation

1. In your terminal type in `git clone https://github.com/Coder-Nicki/times_tables_challenge

2. 


## References
Guido van Rossum, B. W. N. C., 2001. PEP 8 – Style Guide for Python Code. [Online] 
Available at: https://peps.python.org/pep-0008/
[Accessed 23 09 2022].




