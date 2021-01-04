// SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

/*
Require should be used to validate conditions such as:
- inputs
- conditions before execution
- return values from calls to other functions

Revert is useful when the condition to check is complex.
For example, (i>10) is ezpz but what if (x>y), 
where y is some combination of z, which is some combination of ...

you get the idea.

Assert should only be used to test for internal errors,
and to check invariants.
*/

contract Account {
    uint256 public balance;
    uint256 public constant MAX_UINT = 2**256 - 1;

    function deposit(uint256 _amount) public {
        uint256 oldBalance = balance;
        uint256 newBalance = balance + _amount;

        // balance + _amount does not overflow if balance + _amount >= balance
        require(newBalance >= oldBalance, "Overflow");

        balance = newBalance;

        assert(balance >= oldBalance);
    }

    function withdraw(uint256 _amount) public {
        uint256 oldBalance = balance;

        // balance - _amount does not underflow if balance >= _amount
        require(balance >= _amount, "Underflow");

        if (balance < _amount) {
            revert("Underflow");
        }

        balance -= _amount;

        assert(balance <= oldBalance);
    }
}
