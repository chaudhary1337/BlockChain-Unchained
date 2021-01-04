// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.7.0;

/*
LOGICAL DETAILS
Imagine you are a car manufacturer. 
You have a lot of cars that you produce. How can you keep track?

One idea is to have a primary contract, which only you can access.
Now, only you have the permissions to 'create' `new cars`
You can assign the owner to be the person who sent you enough ether,
or in our case, just sent a request.

Note this is not exactly instantiation of cars from the manufacturer itself.
The manufacturer is instead a 'generator' contract, 
generating other contracts. The contracts *then* are instantiated 
from the contract `Car`.

IMPLEMENTATION DETAILS
1. deploy the CarFactory contract
2. create as many cars as you want, for as many different owners
3. remember to send at least 10 ether with it
4. getting the car using `getCar` shows the actual buyer; 
the one who sent the money (10 ether)
5. however, getting the car using `cars` variable, 
from the auto-generated functionality shows a different address.
6. that address is the address of the instance!
7. which can now be checked by deploying the `Car` contract

POSSIBLE ATTACK: PHISHING
since you can ask the `CarFactory` owner of the contract
to instantiate for you, you can also force them to send 10 ether!
*/

contract Car {
    // stores the buyer's address 
    // and the model name of the car bought 
    address public owner;
    string public model;
    
    // instantiation
    constructor(address _owner, string memory _model) payable {
        require(msg.value >= 10 ether, "atleast 10 ether required!");
        owner = _owner;
        model = _model;
    }
}

contract CarFactory {
    // as a manufacturer, you need a list of the cars you sold
    Car[] public cars;
    
    uint public bankBalance;
    
    // takes in buyer's address and name of model bought
    function create(address _owner, string memory _model) public payable {
        // `car` named variable of the contract `Car`, 
        // we also send in `msg.value` amount of ether
        // being instantiated with required values
        Car car = (new Car){value: msg.value}(_owner, _model);
        
        // stonks for the manufacturer!
        bankBalance += msg.value;
        
        // storing the instance
        cars.push(car);
    }

    // returns the car at that index
    function getCar(uint _index) public view returns (address, string memory, uint) {
        Car car = cars[_index];
        return (car.owner(), car.model(), address(car).balance);
    }
}
