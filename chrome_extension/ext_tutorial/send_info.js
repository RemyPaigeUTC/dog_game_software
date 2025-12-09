const send_info_button = document.createElement('div');
send_info_button.textContent = "Send Info"
send_info_button.id = "send_info"
send_info_button.style["background-color"] = "red"
send_info_button.style["border"] = "1px solid black"
send_info_button.style["text-align"] = "center"
send_info_button.style["padding"] = "5px"
document.getElementsByClassName("dog-profile-card")[0].insertAdjacentElement("afterbegin", send_info_button)
try {
        // view dog - view conformation panel toggle
    const send_info_button = document.getElementById("send_info");
    send_info_button.onclick = function (event) {
        const xhr = new XMLHttpRequest();
        xhr.open("POST", "http://127.0.0.1:5000/receive_data");
        xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")
        const body = JSON.stringify({
          userId: 1,
          title: "Fix my bugs",
          completed: false
        });
        xhr.onload = () => {
          if (xhr.readyState === 4 && xhr.status === 201) {
            console.log(JSON.parse(xhr.responseText));
          } else {
            console.log(`Error: ${xhr.status}`);
          }
        };
        xhr.send(body);

        console.log(document.all[0].outerHTML);
    };
} catch (err) {
    console.log(err);
}

