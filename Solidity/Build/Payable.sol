// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract Wallet {
    // defining events
    event Log(address addr, uint256 amount, uint256 balance);

    // onwer is visible publically
    // onwer must also be payable to receive and send ethers
    address payable public owner;

    // setting up the owner
    constructor() {
        owner = msg.sender;
    }

    // checks whether the message sender is owner or not.
    // allows execution if sender is onwer.
    modifier onlyOwner() {
        require(msg.sender == owner, "You are not the owner. Go away.");
        _;
    }

    function getBalance() public view returns (uint256) {
        return address(this).balance;
    }

    function deposit() public payable {
        emit Log(msg.sender, msg.value, address(this).balance);
    }

    // note how withdraw can be generalised to get transfer
    // function withdraw(uint _amount) public onlyOwner {
    //     owner.transfer(_amount);
    // }

    function transfer(address payable _to, uint256 _amount) public onlyOwner {
        _to.transfer(_amount);
        emit Log(_to, _amount, address(this).balance);
    }
}
