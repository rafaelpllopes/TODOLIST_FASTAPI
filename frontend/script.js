const apiUrl = 'http://localhost:8000/tasks';

async function fetchTasks() {
    const res = await fetch(apiUrl);
    const tasks = await res.json();
    const list = document.getElementById('task-list');
    list.innerHTML = '';

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = task.completed ? 'completed' : '';

        const title = document.createElement('span');
        title.textContent = task.title;

        const toggleButton = document.createElement('button');
        toggleButton.textContent = task.completed ? '🔄' : '✅';
        toggleButton.title = task.completed ? 'Reabrir tarefa' : 'Concluir tarefa';
        toggleButton.onclick = () => toggleComplete(task);

        const delBtn = document.createElement('button');
        delBtn.textContent = '🗑';
        delBtn.title = 'Excluir tarefa';
        delBtn.onclick = () => deleteTask(task.id);

        const actions = document.createElement('div');
        actions.className = 'actions';
        actions.appendChild(toggleButton);
        actions.appendChild(delBtn);

        li.appendChild(title);
        li.appendChild(actions);
        list.appendChild(li);
    });
}

async function addTask(title) {
    await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });
    fetchTasks();
}

async function toggleComplete(task) {
    await fetch(`${apiUrl}/${task.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ completed: !task.completed })
    });
    fetchTasks();
}

async function deleteTask(id) {
    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    fetchTasks();
}

document.getElementById('task-form').addEventListener('submit', e => {
    e.preventDefault();
    const input = document.getElementById('incluir-tarefa');
    const title = input.value.trim();
    if (title) {
        addTask(title);
        input.value = '';
    }
});

fetchTasks();
