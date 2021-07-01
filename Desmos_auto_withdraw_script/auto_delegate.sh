#!/bin/bash
#
#----------
#Network:
NET=desmos
#Validador stats:
VALOPER=desmosvaloperxxxxxx
#Wallet key:
WALLET_KEY=validator_key_NAME
#Wallet delegator address:
WALLET=desmos1mxxxxxx
#Chain-id
CHAIN_ID=$(curl -s http://localhost:26657/status | jq -r '.result.node_info.network')
#Comision:
FEE=5000
#Units:
CURR=udaric
###

echo "Wallet password:"
read -s password

#Bucle:
state=true
while ${state};
do
  #withdraw commissions and rewards
  echo "Withdrawing ..."
  echo -e "${password}" | ${NET} tx distribution withdraw-rewards ${VALOPER} --commission --from ${WALLET_KEY} --chain-id ${CHAIN_ID} --fees ${FEE}${CURR} -y
  echo -e "${password}" | ${NET} tx distribution withdraw-all-rewards --from ${WALLET_KEY} --chain-id ${CHAIN_ID} --fees ${FEE}${CURR} -y
  #sleep 120
  sleep 10
  AMOUNT=$(${NET} query bank balances ${WALLET} --chain-id ${CHAIN_ID} --output=json | jq -r '.balances[0].amount')
 echo "Amount being managed:"
 echo $AMOUNT

  #We leave a bit to ensure that we can pay fees in general
  DEL=$(($AMOUNT-1000000))

  #The real deal happening now:
  echo "Delegating ..."
  echo -e "${password}" | ${NET} tx staking delegate ${VALOPER} ${DEL}${CURR} --from ${WALLET_KEY}  --chain-id ${CHAIN_ID} --fees ${FEE}${CURR} -y

  #Wait for an hour:
  echo "Waiting for an hour ..."
  sleep 3600
  #state=false
done
