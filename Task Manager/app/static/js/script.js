document.addEventListener("DOMContentLoaded", () => {
    const toggleDarkMode = document.getElementById("dark-mode-toggle");
  
    if (toggleDarkMode) {
      toggleDarkMode.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");
      });
    }
  
    // Показать fade-in элементы
    document.querySelectorAll(".fade-in").forEach((element) => {
      element.classList.add("show");
    });
  
    // Добавление новой задачи
    const addTaskForm = document.getElementById("add-task-form");
    if (addTaskForm) {
      addTaskForm.addEventListener("submit", (e) => {
        e.preventDefault();
  
        const taskInput = document.getElementById("task-input");
        const taskList = document.getElementById("task-list");
  
        if (taskInput && taskList && taskInput.value.trim() !== "") {
          const newTask = document.createElement("li");
          newTask.className = "fade-in";
          newTask.textContent = taskInput.value.trim();
  
          taskList.appendChild(newTask);
          taskInput.value = "";
        }
      });
    }
  });
  