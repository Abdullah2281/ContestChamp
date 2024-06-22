// static/your_app/js/timer.js
document.addEventListener("DOMContentLoaded", function () {
    // Get the end time from the data attribute
    const timerElement = document.getElementById("timer");
    const endTime = new Date(timerElement.getAttribute("data-end-time"));

    // Update the countdown every second
    const timerInterval = setInterval(function () {
        const now = new Date().getTime();
        const distance = endTime - now;
        if (distance < 0) {
            clearInterval(countdown);
            timerElement.innerHTML = "Contest has been started";
            window.location.href = '/contest/' + contestId;
            return;
        }
        // Time calculations for hours, minutes, and seconds
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="timer"
        timerElement.innerHTML = ('0' + hours).slice(-2) + ":"
            + ('0' + minutes).slice(-2) + ":"
            + ('0' + seconds).slice(-2);

        // If the countdown is over, write some text

    }, 1000);
});