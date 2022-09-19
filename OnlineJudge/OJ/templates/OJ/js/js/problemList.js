// ### CONSOLE LOG debugging ###

// let problem_name_list = document.getElementsByClassName("PL-problem-name");
// for (let i = 0; i < problem_name_list.length; i++) {
//     problem_name_list[i].addEventListener("click", () => {
//         console.log("Clicked.")
//     })
// }

let problem_difficulty_list = document.getElementsByClassName("PL-problem-difficulty");
let add_HTML1 = "<div class='PL-problem-difficulty-easy'>Easy</div>"
let add_HTML2 = "<div class='PL-problem-difficulty-medium'>Medium</div>"
let add_HTML3 = "<div class='PL-problem-difficulty-hard'>Hard</div>"
for (let i = 0; i < problem_difficulty_list.length; i++) {
    if (problem_difficulty_list[i].getAttribute("difficulty-value") <= 2) {
        problem_difficulty_list[i].innerHTML = add_HTML1;
    }
    else if (problem_difficulty_list[i].getAttribute("difficulty-value") <= 4) {
        problem_difficulty_list[i].innerHTML = add_HTML2;
    }
    else if (problem_difficulty_list[i].getAttribute("difficulty-value") <= 5) {
        problem_difficulty_list[i].innerHTML = add_HTML3;
    }
}

let problem_number_list = document.getElementsByClassName("PL-problem-id");
let problem_list_item = document.getElementsByClassName("PL-list-item");
for (let i = 0; i < problem_number_list.length; i++) {
    problem_number_list[i].innerHTML = i + 1;
    if ((i + 1) % 2 == 0)
        problem_list_item[i].classList.add("PL-list-item-even")
    else
        problem_list_item[i].classList.add("PL-list-item-odd")
}