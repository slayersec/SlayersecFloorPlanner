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
		$phone = $_POST['phone'];
		$email = $_POST['email'];
		$psw = $_POST['psw'];
		
		

		//INSERTING INTO DATABASE OVERRIDE
        $sql = "insert into login_table  (username, password, employeeID) 
		                           values('$uname',  '$psw', 111)";
	    $conn->query($sql);
		
		//Link to Employee Profiles
		//$sql = "insert into login_table  (username, password) 
		//                           values('$uname',  '$psw')";
	    //$conn->query($sql);


		
		$conn->close();
		header("location:login");
		
		
   }	
	//outer if 		
		  //Global Variable Passing using Session[]
		 // $_SESSION["uname"]= $uname;
		 //$uname= $_SESSION["uname"] ;
    //header("location: /view/login.php");
    //header("location: /view/login.php");
   
    
    
?>





