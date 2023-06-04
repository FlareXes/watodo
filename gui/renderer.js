// renderer.js

const { ipcRenderer } = require('electron')

const todoForm = document.getElementById('todo-from')
const todoInput = document.getElementById('todo-input')
const deleteButton = document.getElementById("todos");


// Display a todo item on the webpage
function displayTodo(todo) {
    const todos_list_element = document.querySelector('#todos');

    const todo_row_element = document.createElement("div");
    todo_row_element.classList.add("todo-row");

    const todo_content_element = document.createElement("div");
    todo_content_element.classList.add("content");

    todo_row_element.appendChild(todo_content_element);

    const todo_input_element = document.createElement("input");
    todo_input_element.classList.add("text");
    todo_input_element.type = "text";
    todo_input_element.value = todo.title;
    todo_input_element.setAttribute("readonly", "readonly");
    todo_content_element.appendChild(todo_input_element);

    const todo_row_actions_element = document.createElement("div");
    todo_row_actions_element.classList.add("actions");

    const todo_delete_element = document.createElement("button");
    todo_delete_element.classList.add("delete");
    todo_delete_element.id = todo.id;
    todo_delete_element.innerHTML = "Delete";

    todo_row_actions_element.appendChild(todo_delete_element);
    todo_row_element.appendChild(todo_row_actions_element)

    todos_list_element.appendChild(todo_row_element);
}

function displayTodos(todos) {
    todos.forEach(todo => displayTodo(todo))
}

window.onload = () => { ipcRenderer.send('get-todos') };

ipcRenderer.on("get-todos-response", (event, data) => {
    if (data.success) {
        displayTodos(data.todos)
    }

    // focus on input form after displaying all todos
    todoInput.focus();
});

ipcRenderer.on("add-todo-response", (event, data) => {
    if (!data.success) {
        console.error(data.error)
    }
    location.reload();
});

ipcRenderer.on("delete-todo-response", (event, data) => {
    if (!data.success) {
        console.error(data.error)
    }
    location.reload();
});


// ----------------------------------------------------------------


function addTodo(todo) {
    ipcRenderer.send('add-todo', todo)
}

function deleteTodo(todoId) {
    ipcRenderer.send('delete-todo', todoId)
}

todoForm.addEventListener('submit', event => {
    event.preventDefault()
    const todo = todoInput.value.trim()
    if (todo !== "")
        addTodo(todo)
    todoInput.value = ''
})

deleteButton.addEventListener('click', (event) => {
    event.preventDefault();
    if (event.target.classList.contains("delete")) {
        const todoId = event.target.id
        deleteTodo(todoId)
    }
});
