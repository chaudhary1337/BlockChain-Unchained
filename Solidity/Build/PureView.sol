// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

/*
View: Can read the state, but can not modify them.
Pure: Can not even read the state.

Modifying the state (not allowed in View and not allowed in Pure):
- Writing to state variables.
- Emitting events.
- Creating other contracts.
- Using selfdestruct.
- Sending Ether via calls.
- Calling any function not marked view or pure.
- Using low-level calls.
- Using inline assembly that contains certain opcodes.


Reading the State (allowed in View, not allowed in Pure):
- Reading from state variables.
- Accessing address(this).balance or <address>.balance.
- Accessing any of the members of block, tx, msg (with the exception of msg.sig and msg.data).
- Calling any function not marked pure.
- Using inline assembly that contains certain opcodes.

*/

contract PureView {
    uint256 x = 5;

    function validView(uint256 y) public view returns (uint256) {
        return (x + y);
    }

    // function invalidView(uint y) public view{
    //     x += y;
    // }

    function validPure(uint256 y) public pure returns (uint256) {
        return y * 2;
    }

    // function invalidPure(uint y) public pure returns(uint){
    //     return x+y;
    // }
}
