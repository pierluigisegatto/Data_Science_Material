This folder contains the bash script for the auto management of a cosmos based validator node, such as Desmos. 
In particular, this script, once correctly setup, will periodically withdraw commissions and rewards from the selected validator and will redelegate to the validator itself.

I personally run my Desmos validator using a VPS and I execute this script using *tmux*, which is a terminal multiplexer for Unix-like operating systems. 
In this way I can run the script on another shell without blocking any other functionalities.

To create a new shell: `tmux new -s auto_delegator`

To exit the shell: `CTRL B + D`

To access the shell: `tmux attach -t auto_delegator` 


To setup the script the user is only required to modify the values in the firsts lines of the code.
- NET: is the cosmos chain name each command starts with. E.g. in Desmos all the tx, query etc commands are invoked using **desmos** 
- VALOPER: Operator address. It starts with **desmosvaloper** 
- WALLET_KEY: key name of your wallet
- WALLET: your delegator address. Its starts with **desmos1**.
- CHAIN_ID: is the name of the chain you currently use for your validator. This field is automatically curled for you.
- FEE: is the amount of gas you are going to provide for each of your transactions.
- CURR: is the currency used by the cosmos chain. For desmos is **udaric**


To run the script, from the folder where the script is located: `./auto_delegator.sh`
At startup it will prompt you to insert the keyring password of your wallet. Once provided it will run indefinetly and every hour it will withdraw and redelegate your commissions and rewards.

For Desmos in particular this script will perform these transactions:

`desmos tx distribution withdraw-all-rewards --from WALLET_KEY --chain-id morpheus-apollo-1 -fees FEE usaric -y`

`desmos tx distribution withdraw-rewards VALOPER --commission --chain-id morpheus-apollo-1 --from WALLET_KEY --fees FEE usaric -y`

`desmos tx staking delegate VALOPER AMOUNT_TO_DELEGATEudaric --chain-id morpheus-apollo-1 --from WALLET_KEY --fees FEE udaric -y`




