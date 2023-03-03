function findHouse() {
  index = document.getElementById("index").value;
  h_no = index % 6;

  if (h_no == 0 && h_no === 0) {
    h = "Wishwa";
    color = /*"rgb(155, 11, 11)"; */ "red";
  } else if (h_no == 1) {
    h = "Gagana";
    color = "yellow";
  } else if (h_no == 2) {
    h = "Sayura";
    color = "blue";
  } else if (h_no == 3) {
    h = "Derana";
    color = "green"; /*"rgb(81, 255, 0)"; /* green */
  } else if (h_no == 4) {
    h = "Soorya";
    color = "rgb(241, 137, 1)"; /* orange */
  } else if (h_no == 5) {
    h = "Pawana";
    color = "purple";
  } else {
    h = "Error";
    color = "red";
  }
  if (index != "") {
    document.getElementById("house").innerHTML = "Your House is&nbsp" + h;
    document.getElementById("house").style.color = color;
  }
}
