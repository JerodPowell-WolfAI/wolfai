document.addEventListener('DOMContentLoaded', () => {
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');
    const dateDisplay = document.getElementById('date-display');

    // Set today's date
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    dateDisplay.textContent = new Date().toLocaleDateString('en-US', options);

    // Fetch and render initial todos
    fetchTodos();

    todoForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = todoInput.value.trim();
        if (!text) return;

        try {
            const res = await fetch('/api/todos', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });
            if (res.ok) {
                todoInput.value = '';
                fetchTodos(); // Re-fetch to render properly
            }
        } catch (err) {
            console.error('Error adding todo:', err);
        }
    });

    async function fetchTodos() {
        try {
            const res = await fetch('/api/todos');
            const todos = await res.json();
            renderTodos(todos);
        } catch (err) {
            console.error('Error fetching todos:', err);
        }
    }

    function renderTodos(todos) {
        todoList.innerHTML = '';
        if (todos.length === 0) {
            todoList.innerHTML = '<li class="empty-state">No tasks yet. Add one above!</li>';
            return;
        }

        todos.forEach(todo => {
            const li = document.createElement('li');
            li.className = `task-item ${todo.completed ? 'completed' : ''}`;
            li.dataset.id = todo.id;

            // Checkbox
            const checkbox = document.createElement('div');
            checkbox.className = 'checkbox-container';
            checkbox.innerHTML = '<i class="fas fa-check"></i>';
            checkbox.onclick = () => toggleTodo(todo);

            // Text / Edit input logic
            const textContainer = document.createElement('div');
            textContainer.style.flex = "1";
            textContainer.style.display = "flex";
            textContainer.style.alignItems = "center";

            const span = document.createElement('span');
            span.className = 'task-text';
            span.textContent = todo.text;

            textContainer.appendChild(span);

            // Actions
            const actions = document.createElement('div');
            actions.className = 'actions';

            const editBtn = document.createElement('button');
            editBtn.className = 'action-btn edit-btn';
            editBtn.innerHTML = '<i class="fas fa-pen"></i>';

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'action-btn delete-btn';
            deleteBtn.innerHTML = '<i class="fas fa-trash"></i>';
            deleteBtn.onclick = () => deleteTodo(todo.id);

            // Edit logic
            const handleEdit = () => {
                const input = document.createElement('input');
                input.className = 'edit-input';
                input.value = todo.text;

                textContainer.replaceChild(input, span);
                input.focus();

                const saveEdit = async () => {
                    const newText = input.value.trim();
                    if (newText && newText !== todo.text) {
                        await updateTodoText(todo.id, newText);
                    } else {
                        fetchTodos(); // Re-render to original state
                    }
                };

                input.addEventListener('blur', saveEdit);
                input.addEventListener('keypress', (e) => {
                    if (e.key === 'Enter') {
                        input.blur(); // Trigger saveEdit
                    }
                });
            };

            editBtn.onclick = handleEdit;

            actions.appendChild(editBtn);
            actions.appendChild(deleteBtn);

            li.appendChild(checkbox);
            li.appendChild(textContainer);
            li.appendChild(actions);

            todoList.appendChild(li);
        });
    }

    async function toggleTodo(todo) {
        try {
            await fetch(`/api/todos/${todo.id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ completed: !todo.completed }) // Only toggle completion
            });
            fetchTodos();
        } catch (err) {
            console.error('Error toggling todo:', err);
        }
    }

    async function updateTodoText(id, newText) {
        try {
            await fetch(`/api/todos/${id}`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: newText })
            });
            fetchTodos();
        } catch (err) {
            console.error('Error updating todo text:', err);
        }
    }

    async function deleteTodo(id) {
        try {
            await fetch(`/api/todos/${id}`, {
                method: 'DELETE'
            });
            fetchTodos();
        } catch (err) {
            console.error('Error deleting todo:', err);
        }
    }
});
