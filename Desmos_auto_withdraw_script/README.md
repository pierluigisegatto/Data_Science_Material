This folder contains the bash script for the auto management of a cosmos based validator node, such as Desmos. 
In particular, this script, once correctly setup, will periodically withdraw commissions and rewards from the selected validator and will redelegate to the validator itself.

I personally run my Desmos validator using a VPS and I execute this script using *tmux*, which is a terminal multiplexer for Unix-like operating systems. 
In this way I can run the script on another shell without blocking any other functionalities.
To create a new shell: `tmux new -s auto_delegator`
To exit the shell: `CTRL B + D`
To access the shell: `tmux attach -t auto_delegator` 

To setup the script the user is only required to modify the values in the firsts lines of the code.
NET: is the cosmos chain name each command starts with. E.g. in Desmos all the tx, query etc commands are invoked using "desmos" 
VALOPER: Operator address. It starts with desmosvaloper 
