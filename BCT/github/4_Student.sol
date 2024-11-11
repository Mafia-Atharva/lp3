// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract StudentRegister {
    address public owner;

    mapping (address => Student) students;

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == owner, "Only owner can register students");
        _;
    }

    struct Student {
        address studentId;
        string name;
        string course;
        uint256 mark1;
        uint256 mark2;
        uint256 mark3;
        uint256 totalMarks;
        uint256 percentage;
        bool isExist;
    }

    function register(
        address studentId,
        string memory name,
        string memory course,
        uint256 mark1,
        uint256 mark2,
        uint256 mark3
    ) public onlyOwner {
        require(!students[studentId].isExist, "Student already registered");

        uint256 totalMarks = mark1 + mark2 + mark3;
        uint256 percentage = totalMarks / 3;

        students[studentId] = Student(studentId, name, course, mark1, mark2, mark3, totalMarks, percentage, true);
    }

    function getStudentDetails(address studentId) 
        public 
        view 
        returns (address, string memory, string memory, uint256, uint256) 
    {
        Student memory stud = students[studentId];
        return (stud.studentId, stud.name, stud.course, stud.totalMarks, stud.percentage);
    }
}
