<!DOCTYPE html>
<html>
<head>
<h2> map overview </h2>

<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box}
body {font-family: Verdana; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}

  min-height: 380px;

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  
  /* Needed to position the navbar */
  position: relative;
}

/* Position the navbar container inside the image */
.container {
  position: absolute;
  margin: 20px;
  width: 95%;
}

/* The navbar */
.topnav {
  overflow: hidden;
  background-color: #333;
}

/* Navbar links */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 49px;
  text-decoration: none;
  font-size: 18px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}
</style>
</head>
<body>


<div class="bg-img">
  <div class="container">
    <div class="topnav"> 
      <a href="#Profile">Profile</a>
      <a href="#Maps">Maps</a>
      <a href="#Login">Login</a>
      <a href="#Register">Register</a>
    </div>
  </div>
 
</div>



</style>
</head>
<body>

<div class="slideshow-container">

<div class="mySlides fade">
 
  <img src="img_nature_wide.jpg" style="width:100%">
  <div class="text">Map models</div>
</div>

<div class="mySlides fade">

  <img src="img_snow_wide.jpg" style="width:100%">
  <div class="text">Map models2</div>
</div>

<div class="mySlides fade">

  <img src="img_mountains_wide.jpg" style="width:100%">
  <div class="text">Map models</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094;</a>
<a class="next" onclick="plusSlides(1)">&#10095;</a>

</div>
<br>


<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}
function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}

</script>

</body>
</html> 