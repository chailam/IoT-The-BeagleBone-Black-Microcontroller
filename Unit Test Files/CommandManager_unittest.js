/**
 * This is the file for Unittest to test for CommandManager
 */


var CommandManager = require("./CommandManager");
var assert = require('assert');

// Function to test whether addCommand functions correctly.
function test_addCommand(){
    var testUnit = new CommandManager();
    // Add 4 commands into the testUnit
    testUnit.addCommand("A1", "Combo1");  
    testUnit.addCommand("B2", "Combo2");
    testUnit.addCommand("C3", "Combo3");
    testUnit.addCommand("D4", "Combo4");
    // Check to see if the results match
    assert(testUnit.commandArray[0].combo == "A1" && testUnit.commandArray[0].commandName == "Combo1");
    assert(testUnit.commandArray[1].combo == "B2" && testUnit.commandArray[1].commandName == "Combo2");
    assert(testUnit.commandArray[2].combo == "C3" && testUnit.commandArray[2].commandName == "Combo3");
    assert(testUnit.commandArray[3].combo == "D4" && testUnit.commandArray[3].commandName == "Combo4");
    
    var testUnit2 = new CommandManager();
    // Add 10 commands into the second testUnit using this loop
    for (var i=0; i<10; i++){
        testUnit2.addCommand(i, i * i);
    }
    // Test if they match
    for (var i=0; i<10; i++){
        assert(testUnit2.commandArray[i].combo == i && testUnit2.commandArray[i].commandName == i * i);
    }
}

// Function to test whether identifyCommand functions correctly.
function test_identifyCommand(){
    var testUnit = new CommandManager();
    // Add 4 commands into the testUnit
    testUnit.addCommand("AA", "Command1");
    testUnit.addCommand("BB", "Command2");
    testUnit.addCommand("CC", "Command3");
    testUnit.addCommand("DD", "Command4");
    // Check to see if the identifyCommand correctly identifies the commands
    assert(testUnit.identifyCommand("AA") == "Command1");
    assert(testUnit.identifyCommand("BB") == "Command2");
    assert(testUnit.identifyCommand("CC") == "Command3");
    assert(testUnit.identifyCommand("DD") == "Command4");
    
    // Add 10 commands into the second testUnit using this loop
    var testUnit2 = new CommandManager();
    for (var i=0; i<10; i++){
        testUnit2.addCommand(i, i * i);
    }
    // Test to see if identifyCommand correctly returns correct output
    for (var i=0; i<10; i++){
        assert(testUnit2.identifyCommand(i) == i * i);
    }
}

function run_tests(){
    test_addCommand();
    test_identifyCommand();
    console.log("All test cases pass")
}

run_tests();
