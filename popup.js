const inputBox = document.getElementById("inputing");
const listContainer = document.getElementById("list-container");
const notes = document.getElementById("notes-input");
document.getElementById("clickme").addEventListener("click", add);

function saveData(){
    let clone = listContainer.cloneNode(true);
    let checkedItems = clone.querySelectorAll('.checked');
    checkedItems.forEach(item => item.remove());
    localStorage.setItem("data", clone.innerHTML);
    localStorage.setItem("notes", notes.value);
}

function add(){
    if (inputBox.value === '') {
        alert("What do you wanna do today?");
    }
    else{
        let li = document.createElement("li");
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);
        let span = document.createElement("span");
        span.innerHTML = "\u00d7";
        li.appendChild(span);
    }
    inputBox.value = "";
    saveData();
}

listContainer.addEventListener("click", function(e){
    const li = e.target.closest('li');
    if (!li || li.classList.contains('checked')) return;

    li.classList.add('checked');

    setTimeout(() => {
        li.remove();
        saveData();
    }, 600);
}, false);

notes.addEventListener("input", saveData);

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data") || "";
    notes.value = localStorage.getItem("notes") || "";
}

showTask();
