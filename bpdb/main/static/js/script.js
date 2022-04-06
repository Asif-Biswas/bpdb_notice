var acc = document.getElementsByClassName("my-accordion");
var i;

for (i = 0; i < acc.length; i++) {
  acc[i].addEventListener("click", function() {
    this.classList.toggle("my-active");
    this.style.borderRadius = "5px";
    var panel = this.nextElementSibling;

    // cloase all panels
    for (var j = 0; j < acc.length; j++) {
        if (acc[j] != this) {
            acc[j].nextElementSibling.style.maxHeight = null;
            acc[j].style.borderRadius = "5px";
        }
    }

    // open only clicked panel
    if (panel.style.maxHeight) {
        panel.style.maxHeight = null;

    } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        this.style.borderRadius = "5px 5px 0 0";
    }

  });
}

// make first panel open by default
var panel = document.getElementsByClassName("my-panel")[0];
panel.style.maxHeight = panel.scrollHeight + "px";
acc[0].style.borderRadius = "5px 5px 0 0";


function myMenuFunction(x) {
    x.classList.toggle("menu-change");
    document.getElementById("show-after-menu-clicked").classList.toggle("d-none");
  }