// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.7.0;
// Write  a  smart  contract  on  a  test  network,  for  Bank  account  of  a  customer  for
  // following operations: Deposit money | Withdraw Money | Show balance
contract Bank{
    mapping(address => uint) public user_account;
    mapping(address => bool) public user_exist;

    function create_account() public payable returns(string memory){
        require(user_exist[msg.sender] == false, "Account Already created!");
        user_account[msg.sender] = msg.value;
        user_exist[msg.sender] = true;
        return "Account created";
    }

    function deposit(uint amount) public payable returns(string memory){
        require(user_exist[msg.sender] == true, "Account not created!");
        require(amount > 0, "Amount should be greater than 0");
        user_account[msg.sender] += amount;
        return "Amount deposisted sucessfully";
    }

    function withdraw(uint amount) public payable returns(string memory){
        require(user_exist[msg.sender] == true, "Account not created!");
        require(amount > 0, "Amount should be greater than 0");
        require(user_account[msg.sender] >= amount, "Amount is greater than money deposisted");
        user_account[msg.sender] -= amount;
        return "Amount withdrawn sucessfully";    
    }

    function account_balance() public view returns(uint){
        return user_account[msg.sender];
    }
    
    function account_exists() public view returns(bool){
        return user_exist[msg.sender];
    }

}





// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.5.0 <0.9.0;

contract EtherWallet {
    address payable public owner;

    constructor() payable{
        owner = payable(msg.sender); // By default msg.sender is not payable, so we cast it
    }

    function withdraw(uint _amount) public {
        require(msg.sender == owner, "Only the owner can invoke this function");
        (bool sent, ) = msg.sender.call{value: _amount}("");
        require(sent, "Failed to send Ether");
    }

    function getBalance() external view returns (uint) {
        return address(this).balance; // Return balance in this contract
    }

    receive() external payable {} // Default function came after Solidity 0.6.0 to allow the contract to receive funds
}



// SPDX-License-Identifier: UNLICENSED
pragma solidity >= 0.7.0;

contract Bank {
    mapping(address => uint) public user_account;
    
    function deposit() public payable returns(string memory) {
        require(msg.value > 0, "Amount should be greater than 0");
        user_account[msg.sender] += msg.value;
        return "Amount deposited successfully";
    }

    function withdraw(uint amount) public returns(string memory) {
        require(amount > 0, "Amount should be greater than 0");
        require(user_account[msg.sender] >= amount, "Insufficient balance");

        user_account[msg.sender] -= amount;
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to send Ether");
        
        return "Amount withdrawn successfully";    
    }

    function account_balance() public view returns(uint) {
        return user_account[msg.sender];
    }
}