<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: Arial;
  background-color: white;
}

* {
  box-sizing: border-box;
}

p.ex1 {
  margin-bottom: 25px;
}

</style>
</head>

<body>

<form action="/action_page.php">
  <div class="container">
    <h1><center> Profile </center> </h1>
    <?php include "imageUpload.php";?>
    
    <center>
    <p> 
    <label for="name"><b>Name</b></label> 
        <input type="text" placeholder="Name" name="name" id="name" required>
    </p>
    
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
    <label for="role"><b>Role</b></label>
        <input type="text" placeholder="Role" name="role" id="role" required>
        <br>
    </p>

    <p>
    <label for="employeeID"><b>EmployeeID</b></label>
        <input type="text" placeholder="EmployeeID" name="employeeID" id="employeeID" required>
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

    <p>
    <label for="notes"><b>Notes</b></label> <br>
        <textarea id="notes" name="notes" rows="10" cols="50"></textarea>
        <br>
    </p>
    
  
    <button type="submit" class="registerbtn">Save</button> <br>
    <a href="/homepage.php">Back To Hompage?</a>

    </center>


</body>
</html> 



