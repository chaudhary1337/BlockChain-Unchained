// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract SmartStorage{
    string public text;
    
    function set(string memory _text) public {
        text = _text;
    }
    
    function get() public view returns (string memory){
        return text;
    } 
}
