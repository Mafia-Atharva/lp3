// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentManagement {
    // Structure definition for Student
    struct Student {
        uint256 id;
        string name;
        uint256 age;
        string course;
        bool isActive;
    }

    // State variables
    address public owner;
    uint256 private studentCount;
    
    // Arrays to store student data
    Student[] public students;
    
    // Mapping for efficient lookups
    mapping(uint256 => uint256) private studentIndexById;
    
    // Events
    event StudentAdded(uint256 indexed id, string name, uint256 age, string course);
    event StudentUpdated(uint256 indexed id, string name, uint256 age, string course);
    event ReceivedEther(address indexed sender, uint256 value);
    
    // Custom errors for gas efficiency
    error StudentNotFound(uint256 id);
    error InvalidStudent();
    error Unauthorized();

    // Constructor
    constructor() {
        owner = msg.sender;
        studentCount = 0;
    }

    // Modifiers
    modifier onlyOwner() {
        if(msg.sender != owner) revert Unauthorized();
        _;
    }

    // Main functions
    function addStudent(
        string memory _name,
        uint256 _age,
        string memory _course
    ) public onlyOwner returns (uint256) {
        // Input validation
        if(bytes(_name).length == 0 || _age == 0 || bytes(_course).length == 0) {
            revert InvalidStudent();
        }

        // Increment student count
        studentCount++;

        // Create new student
        Student memory newStudent = Student({
            id: studentCount,
            name: _name,
            age: _age,
            course: _course,
            isActive: true
        });

        // Add to array and mapping
        students.push(newStudent);
        studentIndexById[studentCount] = students.length - 1;

        // Emit event
        emit StudentAdded(studentCount, _name, _age, _course);

        return studentCount;
    }

    function getStudent(uint256 _id) public view returns (
        uint256 id,
        string memory name,
        uint256 age,
        string memory course,
        bool isActive
    ) {
        uint256 index = studentIndexById[_id];
        if(index >= students.length || students[index].id != _id) {
            revert StudentNotFound(_id);
        }

        Student memory student = students[index];
        return (
            student.id,
            student.name,
            student.age,
            student.course,
            student.isActive
        );
    }

    function updateStudent(
        uint256 _id,
        string memory _name,
        uint256 _age,
        string memory _course
    ) public onlyOwner {
        uint256 index = studentIndexById[_id];
        if(index >= students.length || students[index].id != _id) {
            revert StudentNotFound(_id);
        }

        // Update student data
        students[index].name = _name;
        students[index].age = _age;
        students[index].course = _course;

        emit StudentUpdated(_id, _name, _age, _course);
    }

    function getAllStudents() public view returns (Student[] memory) {
        return students;
    }

    function getStudentCount() public view returns (uint256) {
        return studentCount;
    }

    // Fallback and receive functions
    receive() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    fallback() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }
}