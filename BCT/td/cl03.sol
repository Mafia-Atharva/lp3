// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    // State variables
    mapping(address => uint256) private balances;
    address public owner;
    bool private locked; // For re-entrancy protection

    // Events
    event Deposit(address indexed account, uint256 amount);
    event Withdrawal(address indexed account, uint256 amount);

    // Custom errors
    error InsufficientBalance(uint256 requested, uint256 available);
    error TransactionFailed();
    error InvalidAmount();

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    // Modifiers
    modifier noReentrant() {
        require(!locked, "No re-entrancy");
        locked = true;
        _;
        locked = false;
    }

    modifier validAmount(uint256 _amount) {
        if(_amount <= 0) revert InvalidAmount();
        _;
    }

    // Deposit function
    function deposit() public payable validAmount(msg.value) {
        balances[msg.sender] += msg.value;
        emit Deposit(msg.sender, msg.value);
    }

    // Withdraw function
    function withdraw(uint256 _amount) public noReentrant validAmount(_amount) {
        if(balances[msg.sender] < _amount) {
            revert InsufficientBalance({
                requested: _amount,
                available: balances[msg.sender]
            });
        }

        balances[msg.sender] -= _amount;
        
        (bool success, ) = payable(msg.sender).call{value: _amount}("");
        if(!success) revert TransactionFailed();

        emit Withdrawal(msg.sender, _amount);
    }

    // Check balance function
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }

    // Get contract balance
    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function
    receive() external payable {
        deposit();
    }
}