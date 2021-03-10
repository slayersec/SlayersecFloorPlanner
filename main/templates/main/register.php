<?php
session_start();
?>
<form method="POST">
</form>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
  background-color: black;
}

* {
  box-sizing: border-box;
}

/* This is the padding for the boxes */
.container {
  padding: 15px;
  background-color: white;
}

/* width of input fields set to max and def input fields */
input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #504caf;
  color: black;
  padding: 12px 18px;
  margin: 5px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}
button {
  background-color: #504caf;
  color: black;
  padding: 12px 18px;
  margin: 5px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

.registerbtn:hover {
  opacity: 1;

}

/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
</style>
</head>
<body>

<form action="registerLogic" method="post">
  <div class="container">
    <h1><center> Register Page </center> </h1>
    <hr>
    {% csrf_token %} 
  <label for="Username"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" id="uname" required>

  <label for="Phone#"><b>Phone#</b></label>
    <input type="text" placeholder="Enter Phone#" name="phone" id="phone" required>
    
  
  <label for="email"><b>Email</b></label>
    <input type="text" placeholder="Enter Email" name="email" id="email" required>

  <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" id="psw" required>

    <hr>
	
    <?php
    
    ?>
	
	
    <button type="submit" class="registerbtn">Register</button>
    
    <a href="/login">Already have an account?</a>
	
  </div>
  
  </div>
</form>

</body>
</html>

