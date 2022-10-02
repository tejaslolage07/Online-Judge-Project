// Below code is for proper functioning of the tab key while using the text-area.
// document.getElementById('id_userCode').addEventListener('keydown', function (e) {
//     if (e.key == 'Tab') {
//         e.preventDefault();
//         var start = this.selectionStart;
//         var end = this.selectionEnd;
//         // set textarea value to: text before caret + tab + text after caret
//         this.value = this.value.substring(0, start) +
//             "\t" + this.value.substring(end);
//         // put caret at right position again
//         this.selectionStart =
//             this.selectionEnd = start + 1;
//     }
// });

var editor = ace.edit("editor");
editor.setTheme("ace/theme/monokai");
editor.session.setMode("ace/mode/python");
let compiler_select = document.getElementById("compiler-select");
setInterval(updateCode, 100);

// function submit() {
//     let user_code = editor.getValue();
//     document.getElementById("id_userCode").value = user_code;
// }

function updateCode() {
    document.getElementById("id_userCode").value = editor.getValue();
}

function compiler() {
    let compiler_name = compiler_select.value;
    var language;
    if (compiler_name === "GNU G++ 17") language = "c_cpp";
    if (compiler_name === "Select") language = "c_cpp";
    if (compiler_name === "Python 3") language = "python";
    if (compiler_name === "Java") language = "java";
    editor.session.setMode("ace/mode/" + language);
}

compiler_select.onchange = compiler;
compiler();

function theme(theme) {
    editor.setTheme("ace/theme/" + theme);
}

function size(selected_size) {
    document.getElementById("editor").style.fontSize = selected_size;
    console.log("Size changed.")
}

// document.getElementById("")
// document.getElementById("id_userCode").value = editor.getValue()