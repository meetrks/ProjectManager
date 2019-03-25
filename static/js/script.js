function delete_task(project_id, task_id){

    var data = {
        is_deleted: true
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.href = '/project/' + project_id
        }
    };
    xhttp.open("PUT", "/project/" + project_id + "/task/" + task_id + "/", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}
function delete_project(project_id){
    var data = {
        is_deleted: true
    }
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.href = '/'
        }
    };
    xhttp.open("PUT", "/project/" + project_id + "/", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}
function update_project(project_id){
    var data = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        start_date: document.getElementById('start_date').value,
        end_date: document.getElementById('end_date').value
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.href = '/'
        }
    };
    xhttp.open("PUT", "/project/" + project_id + "/", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}
function update_assignee(project_id, task_id){
    var assignee_opt = document.getElementById("assignee");
    var assignee = assignee_opt.options[assignee_opt.selectedIndex].value;

    var data = {
        assignee: assignee
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {

        }
    };
    xhttp.open("PUT", "/project/" + project_id + "/task/" + task_id + "/", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}
function update_task(project_id, task_id){
    var assignee_opt = document.getElementById("assignee");
    var assignee = assignee_opt.options[assignee_opt.selectedIndex].value;

    var data = {
        name: document.getElementById('name').value,
        description: document.getElementById('description').value,
        assignee: assignee
    }

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            window.location.href = '/project/' + project_id
        }
    };
    xhttp.open("PUT", "/project/" + project_id + "/task/" + task_id + "/", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(JSON.stringify(data));
}

