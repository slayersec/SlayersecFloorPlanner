<?php



/*
// Initialize the session
session_start();
 
// Check if the user is already logged in, if yes then redirect him to welcome page
if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: homepage.php");
    exit;
}
*/
 
// Include config file
require_once "config";
 

// Processing form data when form is submitted

    
    // Validate credentials
    if(isset($_POST['uname']) && isset($_POST['psw']) ){
		
		$uname = $_POST['uname'];
		$psw = $_POST['psw'];


        //$sql = "insert into login_table  (username, password) 
		//                           values('$uname',  '$psw')";
	   // $conn->query($sql);


		$sql = "SELECT * FROM login_table WHERE username = '$uname'  and password= '$psw'";
		
		//echo $sql;exit;
		
		$result = $conn->query($sql);

		if ($result->num_rows > 0) {
		  // output data of each row
		  while($row = $result->fetch_assoc()) {
			  header("/homepage");
			 
			 /*echo $row["username"];
					  echo $row["password"];
					  echo $row["employeeID"];
					  */
		  }
		} else {
		  //echo "0 results";
		    header("location:login");
        }
		$conn->close();

		
		
		
	}//outer if 		
		  //Global Variable Passing using Session[]
		 // $_SESSION["uname"]= $uname;
		 //$uname= $_SESSION["uname"] ;
        
   
    
    
?>





