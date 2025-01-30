const readline = require('readline-sync');
const { register, login } = require('./auth');

console.log('=== Simple Auth System ===');
console.log('1. Register\n2. Login');

const choice = readline.questionInt('Enter your choice: ');

if (choice === 1) {
    register();
} else if (choice === 2) {
    login();
} else {
    console.log('Invalid option.');
}
