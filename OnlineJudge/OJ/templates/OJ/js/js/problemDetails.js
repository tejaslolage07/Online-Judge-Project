let btn = document.getElementById("btn");
let problem_name = document.getElementById("problem-name");
let problem_statement = document.getElementById("problem-statement");
function setGreen() {
    problem_name.className = "PD-problem-name-heading-green font-style-dancing-script";
    btn.className = "btn btn-outline-success";
}

function setYellow() {
    problem_name.className = "PD-problem-name-heading-yellow font-style-dancing-script";
    btn.className = "btn btn-outline-warning";
}

function setRed() {
    problem_name.className = "PD-problem-name-heading-red font-style-dancing-script";
    btn.className = "btn btn-outline-danger";
}


let difficulty = parseInt(problem_name.getAttribute("target"));
if (difficulty === 5) setRed();
else if (3 <= difficulty < 5) setYellow();
else setGreen();

