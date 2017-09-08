/*jshint esversion: 6 */
function funcHelper(arr, indexPos) {
    "use strict";
    return removeDupes(arr, indexPos);
}

function removeDupes(arr, indexPos) {
    "use strict";
    // Check if indexPos is at the end of array
    if (indexPos === arr.length - 1) {
        // If true, return the array
        return arr;
    }
    // Check if array value is the same as next in the array
    else if (arr[indexPos] === arr[indexPos + 1]) {
        // If true, use a loop to shift the array to the left
        for (let i = indexPos; i < arr.length - 1; i++) {
            arr[i] = arr[i + 1];
        }
        // Then remove last value from the array to shorten it
        arr.length = arr.length - 1;
        // Check if another duplicate of the same value exists
        if (arr[indexPos] === arr[indexPos + 1]) {
            // If true, recall function with current arr & indexPos
            removeDupes(arr, indexPos);
        }
    }
    // Values not the same, move indexPos and call function again
    //indexPos += 1;
    return removeDupes(arr, indexPos + 1);
    //return arr;
}


// var arr = [1, 1, 1, 3, 5, 6]
// var arr = [1, 1, 1, 2, 2, 4, 5, 6, 7, 7, 9];
var arr = [-1, -1, 2, 3, 3, 3, 7, 10, 20, 20, 21];
console.log(removeDupes(arr, 0));