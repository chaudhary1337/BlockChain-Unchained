# Fixing Exploits

## Fixing ReEntrancy

### 1. Logical Fix

Change
```javascript
function withdraw(uint _amount) public {
    require(balances[msg.sender] >= _amount);
    
    (bool sent, ) = msg.sender.call{value: _amount}("");
    require(sent, "Failed to send Ether");
    
    balances[msg.sender] -= _amount;
}
```

to

```javascript
function withdraw(uint _amount) public {
    require(balances[msg.sender] >= _amount);
  
    balances[msg.sender] -= _amount;
    
    (bool sent, ) = msg.sender.call{value: _amount}("");
    require(sent, "Failed to send Ether");  
}
```

### 2.Using Functional Modifier
```javascript
contract SecureVault{
    mapping(address => uint) public balances;
    bool internal locked;

    function deposit() public payable { balances[msg.sender] += msg.value; }

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
        
        balances[msg.sender] -= _amount;
    }
    
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
```
