{% block content %}
    <form method="POST">
      {% csrf_token %}
      {{form}}
    </form>

<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial}
form {border: 3px solid #f1f1f1;}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

button {
  background-color: #504caf;
  color: black;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

img.avatar {
  width: 40%;
  border-radius: 40%;
}

.container {
  padding: 15px;
}

span.psw {
  float: right;
  padding-top: 15px;
}

  /* I had to change this max-width section */
  p.ex1 {
  max-width: 300px;
  }
  
  span.psw {
     display: block;
     float: none;
  }

</style>
</head>
<body>

<h2> <center> Floor Management Login </center></h2>

<form action="/action_page.php" method="post">
  <div class="imgcontainer">
    <img src="img_avatar2.png" alt="Avatar" class="avatar">
  </div>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Enter Username" name="uname" required>

    <label for="psw"><b>Password</b></label>
    <input type="password" placeholder="Enter Password" name="psw" required>

    <button type="submit">Login</button>
    <label> 
    </label>
  </div>

  <div class="container" style="background-color:#F1F1F1">

 <a href="register.php">Need to register?</a>
  </div>
</form>

</body>
</html>

{% endblock %}