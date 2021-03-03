<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
  background-color: white;
  border: 10px solid black;
}

* {
  box-sizing: border-box;
}

p.ex1 {
  margin-bottom: 25px;
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
  padding: 14px 80px;
  text-decoration: none;
  font-size: 18px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Profile Page CSS */

.containerProfile {
    padding: 80px;
}

/* width of input fields set to max and def input fields */
input[type=text], input[type=number] {
  width: 20%;
  padding: 10px;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

</style>
</head>

<body>

  <div class="container">
    <div class="topnav"> 
		<a href="/homepage">Homepage</a>
		<a href="/profile">Profile</a>
		<a href="/maps2D">Maps</a>
		<a href="/login">Login</a>
		<a href="/register">Register</a>
    </div>
  </div>

    <form action="/action_page.php">
    <div class="containerProfile">
        <h1><center> Profile </center> </h1>
    
        <div align = "left">
            <?php include "imageUpload.php";?>
        </div>
    
        <!-- This is the placement of name, empID, and role under the emp pic -->

        <div style="position:relative; text-align:left;">

            <p> 
            <label for="name"><b>Name</b></label> 
                <input type="text" placeholder="Name" name="name" id="name" required>
            </p>
    
            <p>
            <label for="employeeID"><b>EmployeeID</b></label>
                <input type="text" placeholder="EmployeeID" name="employeeID" id="employeeID" required>
                <br>
            </p>

            <p>
            <label for="role"><b>Role</b></label>
                <input type="text" placeholder="Role" name="role" id="role" required>
                <br>
            </p>

        </div>
        

        <!-- This is the placement of the rest of the fields towards the top -->

        <div class="extraInformation">
            <center>

            <div style="position:relative; left:80px; bottom:450px; line-height:61px;">

                <p> 
                <label for="email"><b>Email</b></label>
                    <input type="text" placeholder="Enter Email" name="email" id="email" required>
                    <br>
                </p>

                <p> 
                <label for="Phone#"><b>Phone#</b></label>
                    <input type="text" placeholder="Enter Phone#" name="Phone#" id="Phone#" required>
                    <br>
                </p>
            
                <p>
                <label for="age"><b>Age</b></label>
                    <input type="number" placeholder="Age" name="age" id="age" required>
                    <br>
                </p>

                <p>
                <label for="position"><b>Position</b></label>
                    <input type="text" placeholder="Position" name="position" id="position" required>
                    <br>
                </p>

                <p>
                <label for="records"><b>Records</b></label>
                    <input type="text" placeholder="Records" name="records" id="records" required>
                    <br>
                </p>

                <p>
                <label for="warning"><b>Warning</b></label>
                    <input type="text" placeholder="Warning" name="warning" id="warning" required>
                    <br>
                </p>
                </center>
        </div>
    </div>
    
    <div align = "center">

        <!-- Placement for Notes -->

        <div style="position:relative; bottom:450px;">

            <p>
            <label for="notes"><b>Notes</b></label> <br>
                <textarea id="notes" name="notes" rows="20" cols="100"></textarea>
                <br>
            </p>

            <button type="submit" class="savebtn">Save</button> <br>

        </div>
    </div>

    
</body>
</html> 



