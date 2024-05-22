let index = 0;
const speed = 70; // Tốc độ hiển thị (ms)
const resultElement = document.querySelector(".result");

const typeWriter = ({ text }) => {
    if (index < text.length) {
        resultElement.innerHTML += text.charAt(index);
        index++;
        resultElement.scrollTop = resultElement.scrollHeight;
        setTimeout(() => {
            typeWriter({ text });
        }, speed);
    }
};

document
    .getElementById("drop_zone")
    .addEventListener("dragleave", function (e) {
        e.preventDefault();
        this.style.backgroundColor = "#ffffff";
    });

document
    .getElementById("drop_zone")
    .addEventListener("drop", function (e) {
        e.preventDefault();
        this.style.backgroundColor = "#ffffff";
        var file = e.dataTransfer.files[0];
        console.log("Dropped file:", file.name);
    });

document
    .getElementById("drop_zone")
    .addEventListener("click", function (e) {
        document.querySelector("#drop_zone input").click();
    });

document.querySelector("#fileInput").addEventListener("change", function (e) {
    const file = e.target.files[0];
    const reader = new FileReader();
    reader.onload = function (event) {
        document.getElementById("drop_zone").style.backgroundImage = `url('${event.target.result}')`;
        document.getElementById("drop_zone").style.backgroundSize = 'cover';
    };
    reader.readAsDataURL(file);
});

document.getElementById("startButton").addEventListener("click", async () => {
    const input = document.querySelector("#fileInput");
    if (input.files.length > 0) {
        const file = input.files[0];
        console.log(file);
        const reader = new FileReader();
        const formData = new FormData();
        formData.append('file', file);

        console.log(formData);
        const response = await fetch('http://127.0.0.1:8000/upload', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();
        reader.onload = function (e) {
            document.querySelector(".result").innerText = "";
            document.getElementById("drop_zone").classList.add('load');
            setTimeout(() => {
                document.getElementById("drop_zone").classList.remove('load');
                index = 0
                typeWriter({text: result.content});
            }, 2000);
        };
        reader.readAsDataURL(file);
    } else {
        input.click();
    }
});
