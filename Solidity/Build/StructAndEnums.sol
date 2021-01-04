// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

contract Order {
    enum Status {Pending, Shipped, Accepted, Rejected, Canceled}

    struct Orders {
        string customerName;
        address customerAddress;
        Status status;
    }

    Orders[] public orders;

    function createOrder(string memory _customerName, address _customerAddress)
        public
    {
        // creating a new order, for a customer;
        // given the name and the address
        // the below is the recommended for larger structs
        orders.push(
            Orders({
                customerName: _customerName,
                customerAddress: _customerAddress,
                status: Status.Pending
            })
        );

        // // for small structs
        // orders.push(Orders(_customerName, _customerAddress));

        // // for lots of defaults, let us use solidity's inits
        // Orders memory orders;
        // orders.customerName = _customerName;
    }

    // note how solidity sees `orders` is public
    // and then automatically creates a `get`-ter function for us
    // function get(uint _index) public view returns (string memory, address, Status){
    //     Orders memory order = orders[_index];
    //     return (order.customerName, order.customerAddress, order.status);
    // }

    function update(
        uint256 _index,
        string memory _customerName,
        address _customerAddress,
        Status _status
    ) public {
        // NOTE: changing `storage` to `memory`
        // causes the changed data to be stored in the temporary memory only
        // that memory is deleted once the execution stops
        // BONUS: this also causes solidity to suggest that
        // we can restrict the function mutability to `view`
        // which is indicative of what happens
        Orders storage order = orders[_index];
        order.customerName = _customerName;
        order.customerAddress = _customerAddress;
        order.status = _status;
    }
}
