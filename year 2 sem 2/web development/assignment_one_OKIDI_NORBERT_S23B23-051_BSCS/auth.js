const fs = require('fs');
const readline = require('readline-sync');
const bcrypt = require('bcrypt');

const usersFile = 'users.json';

// Load users from JSON file
const loadUsers = () => {
    if (!fs.existsSync(usersFile)) return [];
    return JSON.parse(fs.readFileSync(usersFile));
};

// Save users to JSON file
const saveUsers = (users) => {
    fs.writeFileSync(usersFile, JSON.stringify(users, null, 2));
};

// User Registration
const register = () => {
    let users = loadUsers();

    console.log('\n=== User Registration ===');
    const name = readline.question('Enter your name: ');
    const email = readline.questionEMail('Enter your email: ');

    // Check if email already exists
    if (users.some(user => user.email === email)) {
        console.log('Email already registered. Try logging in.');
        return;
    }

    const password = readline.question('Enter your password: ', { hideEchoBack: true });
    const hashedPassword = bcrypt.hashSync(password, 10);

    users.push({ name, email, password: hashedPassword });
    saveUsers(users);

    console.log('Registration successful! You can now log in.');
};

// User Login
const login = () => {
    let users = loadUsers();

    console.log('\n=== User Login ===');
    const email = readline.questionEMail('Enter your email: ');
    const password = readline.question('Enter your password: ', { hideEchoBack: true });

    const user = users.find(u => u.email === email);
    if (!user || !bcrypt.compareSync(password, user.password)) {
        console.log('Invalid email or password!');
        return;
    }

    console.log(`\nWelcome, ${user.name}!`);
    showMenu(user);
};

// User Menu (After Login)
const showMenu = (user) => {
    while (true) {
        console.log('\n=== User Menu ===');
        console.log('1. View Profile\n2. Logout');
        const choice = readline.questionInt('Choose an option: ');

        if (choice === 1) {
            console.log(`\nName: ${user.name}\nEmail: ${user.email}\n`);
        } else if (choice === 2) {
            console.log('Logged out successfully.');
            break;
        } else {
            console.log('Invalid choice. Try again.');
        }
    }
};

// Export functions
module.exports = { register, login };
