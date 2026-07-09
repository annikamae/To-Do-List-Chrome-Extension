import json
from pyscript import document
from js import localStorage

STORAGE_KEY = "python_chrome_todo_tasks"
PRIORITIES = ["🍁 Low", "🥕 High", "🔥 Highest"]

def load_tasks():
    saved_data = localStorage.getItem(STORAGE_KEY)
    return json.loads(saved_data) if saved_data else []

def save_tasks(tasks):
    localStorage.setItem(STORAGE_KEY, json.dumps(tasks))

def render_tasks():
    task_list_element = document.getElementById("task-list")
    task_list_element.innerHTML = ""
    
    tasks = load_tasks()
    for index, task_dict in enumerate(tasks):
        if isinstance(task_dict, str):
            task_dict = {"text": task_dict, "done": False, "priority": 0}

        li = document.createElement("li")
        if task_dict.get("done", False):
            li.classList.add("completed")
            
        chk = document.createElement("input")
        chk.type = "checkbox"
        chk.className = "todo-checkbox"
        chk.checked = task_dict.get("done", False)
        chk.onclick = lambda e, idx=index: toggle_task(idx)
        li.appendChild(chk)
        
        text_span = document.createElement("span")
        text_span.innerText = task_dict.get("text", "")
        text_span.className = "task-text"
        li.appendChild(text_span)
        
        actions = document.createElement("div")
        actions.className = "actions"
        
        p_idx = task_dict.get("priority", 0)
        p_btn = document.createElement("button")
        p_btn.innerText = PRIORITIES[p_idx]
        p_btn.className = f"priority-btn p-{p_idx}"
        p_btn.onclick = lambda e, idx=index: cycle_priority(idx)
        actions.appendChild(p_btn)
        
        del_btn = document.createElement("button")
        del_btn.innerText = "✕"
        del_btn.className = "delete-btn"
        del_btn.onclick = lambda e, idx=index: delete_task(idx)
        actions.appendChild(del_btn)
        
        li.appendChild(actions)
        task_list_element.appendChild(li)

def add_task(event):
    input_element = document.getElementById("task-input")
    task_text = input_element.value.strip()
    
    if task_text:
        tasks = load_tasks()
        tasks.append({"text": task_text, "done": False, "priority": 0})
        save_tasks(tasks)
        input_element.value = ""
        render_tasks()

def toggle_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks(tasks)
        render_tasks()

def cycle_priority(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        current_p = tasks[index].get("priority", 0)
        tasks[index]["priority"] = (current_p + 1) % 3
        save_tasks(tasks)
        render_tasks()

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        render_tasks()

render_tasks()
