// ================= PAGE LOAD EFFECT =================

document.addEventListener("DOMContentLoaded", function () {
  console.log("Women Safety System Loaded");
});

// ================= BUTTON CLICK ANIMATION =================

document.querySelectorAll(".btn").forEach((btn) => {
  btn.addEventListener("click", function () {
    btn.style.transform = "scale(0.95)";
    setTimeout(() => {
      btn.style.transform = "scale(1)";
    }, 150);
  });
});

// ================= SOS BUTTON EFFECT =================

const sosBtn = document.querySelector(".sos-btn");

if (sosBtn) {
  sosBtn.addEventListener("click", function () {
    alert("🚨 SOS Alert Triggered!");

    sosBtn.innerHTML = "Sending Alert...";
    sosBtn.disabled = true;
  });
}

// ================= SIMPLE FORM VALIDATION =================

const forms = document.querySelectorAll("form");

forms.forEach((form) => {
  form.addEventListener("submit", function (e) {
    const inputs = form.querySelectorAll("input[required]");

    let valid = true;

    inputs.forEach((input) => {
      if (input.value.trim() === "") {
        valid = false;
        input.style.border = "2px solid red";
      } else {
        input.style.border = "1px solid #ccc";
      }
    });

    if (!valid) {
      e.preventDefault();
      alert("Please fill all required fields!");
    }
  });
});

// ================= PHONE NUMBER VALIDATION =================

const phoneInput = document.querySelector("input[name='phone']");

if (phoneInput) {
  phoneInput.addEventListener("input", function () {
    phoneInput.value = phoneInput.value.replace(/[^0-9]/g, "");

    if (phoneInput.value.length > 10) {
      phoneInput.value = phoneInput.value.slice(0, 10);
    }
  });
}

// ================= SMOOTH CARD HOVER =================

document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("mouseenter", () => {
    card.style.transform = "translateY(-5px)";
  });

  card.addEventListener("mouseleave", () => {
    card.style.transform = "translateY(0)";
  });
});

// ================= NAVBAR SCROLL SHADOW =================

window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");

  if (navbar) {
    if (window.scrollY > 20) {
      navbar.style.boxShadow = "0px 5px 15px rgba(0,0,0,0.3)";
    } else {
      navbar.style.boxShadow = "none";
    }
  }
});
function sendLiveLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      fetch("/live_location", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          lat: position.coords.latitude,
          long: position.coords.longitude,
        }),
      });
    });
  }
}

setInterval(sendLiveLocation, 5000);

