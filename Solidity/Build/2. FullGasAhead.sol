// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract Gas {
    function getGasPrice() public view returns (uint256) {
        return tx.gasprice;
    }

    function fullGasAhead() public pure {
        uint256 i = 0;
        while (true) {
            i += 100;
        }
    }
}
