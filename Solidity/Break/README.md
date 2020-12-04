# Fixing Exploits

## Fixing Underflow/Overflow
[SafeMath](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/math/SafeMath.sol)

## ReEntrancy

### The Exploit
Short Answer: Recursion 

Long Answer:
We deploy the contract ```Attack``` with the address of the ```SecureVault```. We now call the ```attack``` function, and send it ```1 wei```. This is deposited to the vault.

Now, we ask for the wei back. This we do by calling the ```withdraw``` function. The function now wants to send us the money back, but instead of letting it complete, in the ```fallback``` (the function which is called by ```withdraw```) function, we call the ```withdraw``` function again. This sends the function in a recursive loop, only stopping when there are ```1 wei``` left. We take the last wei as well :).

Its only after all of the calls are returned that one realises the damage done. 

#### 1. Logical Fix

Change
```javascript
function withdraw(uint _amount) public {
    require(balances[msg.sender] >= _amount);
    
    (bool sent, ) = msg.sender.call{value: _amount}("");
    require(sent, "Failed to send Ether");
    
    // changing the balance only after the call is made; only when the transaction is successful
    balances[msg.sender] -= _amount;
}
```

to

```javascript
function withdraw(uint _amount) public {
    require(balances[msg.sender] >= _amount);
  
    // recalculating the balance regardless of the transaction's failure or success. It is not helpful for every case. Look for mutex locks, with the help of functional modifier.
    balances[msg.sender] -= _amount;
    
    (bool sent, ) = msg.sender.call{value: _amount}("");
    require(sent, "Failed to send Ether");  
}
```

#### 2.Using Functional Modifier
```javascript
contract SecureVault{
    mapping(address => uint) public balances;
    bool internal locked;

    function deposit() public payable { balances[msg.sender] += msg.value; }

    // adding this modifer, which does not allow recursion
    modifier noReEntrancy(){
        require(!locked, "No Re-entrancy!")
        locked = true;
        _;
        locked = false;
    }

    function withdraw(uint _amount) public noReEntrancy {
        require(balances[msg.sender] >= _amount);
        
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");
        
        // we now deduct the amount from the hacker, of course, only after the transaction's success.
        balances[msg.sender] -= _amount;
    }
    
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
```

## Self Destruction

### The Attack
Short Answer: We take down everyone with us

Long Answer:

Quick Info: Self-destruct destroys the contract. It also has to remove any ether stored at the location, so it ends up transferring *all* the ether to the addess supplied, as, ```selfdestruct(transfer_address)```.

We can use this to force send ether to a contract, overriding all the conditions; doesn't matter if the function is non-payable, or there are input restrictions.

We now use this idea to send >=7 ethers, to a game of ```Gamble7```. This overrides the condition of 1 ether/deposition. However, this comes at the cost of the attacker not getting anything in return; there is no contract which the winning funds can be supplied to!

### Fix
We relied on the internal ```address(this).balance```. The simple fix is to create our own ```uint public balance``` variable, storing the balance details here.

## Denial of Service

### The Attack
Short Answer: We refuse to accept the refund

Long Answer: The contract ```KinfOfEther``` allows only one king, who has maximum amount of ether in storage currently. The "kings" are usualy accounts of people, residing in the ```EVM```, along with contracts themselves. Infact what we exploit is partly the fact that user account and contract account addresses are indistinguishable; we can have a contract pretend to be a user. This is not an issue, and is perfectly valid. [Source](https://stackoverflow.com/questions/42081194/where-do-smart-contracts-reside-in-blockchain-ethereum-or-hyperledger)

Now, note how the contract ```Attack``` does not have any fallback function to accept the ether back. This simply means that the transactions will fail; this contract can *not* receive any ether. Thus, we stay the king, by not accepting the refund XD

### Fix
Do not auto-refund. Add a new function to withdraw the funds. This was execution will be un-haltered.
