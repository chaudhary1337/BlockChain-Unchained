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
