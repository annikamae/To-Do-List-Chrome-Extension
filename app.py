import json
from pyscript import document
from js import localStorage

STORAGE_KEY = "python_chrome_todo_tasks"

def load_tasks():
    """Retrieves tasks saved in the local storage cache."""
    saved_data = localStorage.getItem(STORAGE_KEY)
    return json.loads(saved_data) if saved_data else []

def save_tasks(tasks):
    """Commits tasks into the local storage cache."""
    localStorage.setItem(STORAGE_KEY, json.dumps(tasks))

def render_tasks():
    """Clears and rebuilds the visual list using current state."""
    task_list_element = document.getElementById("task-list")
    task_list_element.innerHTML = ""
    
    tasks = load_tasks()
    for index, task in enumerate(tasks):
        li = document.createElement("li")
        text_span = document.createElement("span")
        text_span.innerText = task
        li.appendChild(text_span)
        
        # Delete action button
        del_btn = document.createElement("button")
        del_btn.innerText = "✕"
        del_btn.className = "delete-btn"
        del_btn.onclick = lambda e, idx=index: delete_task(idx)
        
        li.appendChild(del_btn)
        task_list_element.appendChild(li)

def add_task(event):
    """Appends a new entry from the input box to the list."""
    input_element = document.getElementById("task-input")
    task_text = input_element.value.strip()
    
    if task_text:
        tasks = load_tasks()
        tasks.append(task_text)
        save_tasks(tasks)
        input_element.value = ""  # Clean input bar
        render_tasks()

def delete_task(index):
    """Removes a task by its relative positioning index."""
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        render_tasks()

render_tasks()