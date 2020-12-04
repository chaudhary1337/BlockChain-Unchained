// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

/*
Create a contract which looks the same, in this case is Mal.
Should have the same function signatures and same variable sizes
for the function that is being called 
from Foo, to Bar (but actually to Mal).
*/

contract Bar {
    event Log(string message);

    function log() public { emit Log("Bar was called"); }
}

contract Foo {
    Bar bar;

    constructor(address _bar) public { bar = Bar(_bar); }
    function callBar() public { bar.log(); }
}

// This code is to be hidden in a separate file
contract Mal {
    event Log(string message);

    function log() public { emit Log("Mal was called"); }
}