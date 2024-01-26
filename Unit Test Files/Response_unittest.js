/**
 * This is the file for Unittest to test for Response
 */

var Response = require("./Response");

var testUnit = new Response();
var bs = testUnit.bs;

// To test if the LED lights up after the ledLightUp function is called
function test_ledLightUp(){
    testUnit.ledLightUp();
    return bs.digitalRead(testUnit.led) == 1? 1 : 0;
}

// To test if the LED turns off after the ledNotLightUp function is called
function test_ledNotLightUp(){
    testUnit.ledNotLightUp();
    return bs.digitalRead(testUnit.led) == 0? 1 : 0;
}

// To test whether the ledBlinkFast function works, returns a timer(float) if executes correctly
function test_ledBlinkFast(){
    return testUnit.ledBlinkFast()? 1 : 0;
}

// To test whether the ledBlinkSlow function works, returns 1 if executes correctly
function test_ledBlinkSlow(){
    return testUnit.ledBlinkSlow() == 1? 1 : 0;
}

function run_tests(){
    // Run all four test cases
    var results = [
            ["Function ledLightUp", test_ledLightUp()],
            ["Function ledNotLightUp", test_ledNotLightUp()],
            ["Function ledBlinkFast", test_ledBlinkFast()],
            ["Function ledBlinkSlow", test_ledBlinkSlow()]
        ];
       
    console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
    
    // Display which function passes test case in the console
    for (var i = 0; i < results.length; i++) {
        if (results[i][1] == 1){
            console.log(results[i][0] + " working!");
        }
        else {
            console.log(results[i][0] + " not working!");
        }
    }
}

run_tests();
