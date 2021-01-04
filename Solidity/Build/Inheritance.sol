// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract X{
    string public name;
    constructor(string memory _name){ name = _name; }
}

contract Y{
    string public text;
    constructor(string memory _text){ text = _text; }
}

// one way to hardcode instantiation
contract B is X("My name is bruh"), Y("why are we here") {
}

// another way to hardcode instantiation
contract C is X, Y{
    constructor() X("meow") Y("just to suffer?"){}
}

// no hardcoding
contract D is X, Y{
    constructor(string memory _name, string memory _text) X(_name) Y(_text){}
}   
