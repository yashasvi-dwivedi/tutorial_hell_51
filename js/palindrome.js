class Solution {
    isPalindrome(s) {
        // Remove non-alphanumeric characters and convert to lowercase
        s = s.replace(/[^a-z0-9]/gi, '').toLowerCase();

        // Check if the string is equal to its reverse
        return s === s.split('').reverse().join('');
    }
}

// Example usage
const solution = new Solution();
console.log(solution.isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(solution.isPalindrome("race a car")); // false
console.log(solution.isPalindrome(" ")); // true
console.log(solution.isPalindrome("bob")); // true
console.log(solution.isPalindrome("Madam")); // true