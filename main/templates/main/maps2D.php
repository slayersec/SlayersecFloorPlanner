<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>

body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}

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
  padding: 14px 80px;
  text-decoration: none;
  font-size: 18px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* CSS for the grid */

.grid-container {
  display: grid;

  grid-template-columns: repeat(15, 0fr);
  grid-template-rows: repeat(15, 1fr);
  
  /* grid-template-columns: 0fr 0fr 0fr 0fr 0fr 0fr;
  grid-template-rows: 1fr 1fr 1fr 1fr 1fr 1fr; */
  padding: 10px;
}

.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;
}

</style>
</head>

<body>

  <div class="container">
    <div class="topnav"> 
     <a href="/homepage">Homepage</a>
      <a href="/profile">Profile</a>
      <a href="/mapsView">Maps</a>
      <a href="/login">Login</a>
      <a href="/register">Register</a>
    </div>
  </div>
  <br><br><br><br><br><br><br>



  <div class="grid-container">
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item"></div>
    <div class="grid-item">9</div>
    <div class="grid-item">10</div>
    <div class="grid-item">11</div>
    <div class="grid-item">12</div>
    <div class="grid-item">13</div>
    <div class="grid-item">14</div>
    <div class="grid-item">15</div>
    <div class="grid-item">16</div>
    <div class="grid-item">17</div>
    <div class="grid-item">18</div>
    <div class="grid-item">19</div>
    <div class="grid-item">20</div>
    <div class="grid-item">21</div>
    <div class="grid-item">22</div>
    <div class="grid-item">23</div>
    <div class="grid-item">24</div>
    <div class="grid-item">25</div>
    <div class="grid-item">26</div>
    <div class="grid-item">27</div>
    <div class="grid-item">28</div>
    <div class="grid-item">29</div>
    <div class="grid-item">30</div>
    <div class="grid-item">31</div>
    <div class="grid-item">32</div>

  </div>

</body>
</html>