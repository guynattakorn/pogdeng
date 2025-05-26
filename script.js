let click = 0;

function updateClick() {
    click += 1;
    const span = document.getElementById("click");
    span.textContent = click;

    // เล่นเสียง pop
    const popSound = document.getElementById("pop-sound");
    popSound.currentTime = 0;
    popSound.play();

    // สุ่ม animation ซ้ายหรือขวา
    const isLeft = Math.random() < 0.5;
    const animationClass = isLeft ? "swing-left" : "swing-right";

    span.classList.remove("swing-left", "swing-right");
    void span.offsetWidth;
    span.classList.add(animationClass);
}

function setImage(source) {
    const img = document.getElementById('moo');
    img.src = source;
}

window.addEventListener("DOMContentLoaded", () => {
    const body = document.body;

    body.addEventListener("mousedown", () => setImage('Moo-Deng-Hippo-Thailand-Pattaya-2-1.png'));
    body.addEventListener("touchstart", () => setImage('Moo-Deng-Hippo-Thailand-Pattaya-2-1.png'));

    body.addEventListener("mouseup", () => setImage('thailand_pygmy_hippo_67377.png'));
    body.addEventListener("touchend", () => setImage('thailand_pygmy_hippo_67377.png'));

    body.addEventListener("click", updateClick);
    body.addEventListener("touchstart", updateClick);
});
