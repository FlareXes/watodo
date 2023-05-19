// main.js
const { app, BrowserWindow } = require('electron');
const { ipcMain } = require('electron');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const fs = require('fs');

const dbPath = path.join(app.getPath('userData'), 'gui', 'todos.db');

// Ensure that the nested directories exist
const nestedDir = path.dirname(dbPath);
if (!fs.existsSync(nestedDir)) {
    fs.mkdirSync(nestedDir, { recursive: true });
}

// create a new database connection
const db = new sqlite3.Database(dbPath);

// create the todos table
db.run(`CREATE TABLE IF NOT EXISTS todos (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  title TEXT)`
);


// create a new browser window
let mainWindow;
function createWindow() {
    mainWindow = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true,
            devTools: false
        },
        autoHideMenuBar: true,
    });

    mainWindow.loadFile('index.html');

    mainWindow.on('closed', () => {
        mainWindow = null;
    });
}

// when the app is ready, create the window
app.whenReady().then(createWindow);

// Handle window activation
app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
});

// Handle quitting of app
app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});


// Listen for get-todos event from renderer process
ipcMain.on('get-todos', (event) => {
    let query = "SELECT * FROM todos"

    db.all(query, [], (err, todos) => {
        if (err) {
            console.log(err);
            event.reply('get-todos-response', { success: false, error: err });
        } else {
            event.reply('get-todos-response', { success: true, todos: todos });
        }
    });
});


// Insert the todo to the database
ipcMain.on('add-todo', (event, todo) => {
    let query = "INSERT INTO todos (title) VALUES (?)"

    db.run(query, todo, (err, newTodo) => {
        if (err) {
            console.log(err);
            event.reply('add-todo-response', { success: false, error: err });
        } else {
            event.reply('add-todo-response', { success: true, todo: newTodo });
        }
    });
});


// Listen for delete-todos event from renderer process
ipcMain.on('delete-todo', (event, todoId) => {
    let query = "DELETE FROM todos WHERE id = ?"

    db.run(query, todoId, (err, newTodo) => {
        if (err) {
            console.log(err);
            event.reply('delete-todo-response', { success: false, error: err });
        } else {
            event.reply('delete-todo-response', { success: true, todo: newTodo });
        }
    });
});
