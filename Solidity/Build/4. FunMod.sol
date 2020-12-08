// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract FunMod{
    address public owner;

    constructor () { owner = msg.sender; }

    modifier validateAddress(address _address) {
        require(_address != address(0), "Address is Invalid!");
        _;
    }

    modifier onlyOwner(){
        require(msg.sender == owner, "Only the owner is allowed access!");
        _;
    }

    function changeOwner(address _newOwner) public onlyOwner validateAddress(_newOwner){
        owner = _newOwner;
    } 
}
