<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>RAF Welcome</title>
<link rel="shortcut icon" href="Img/favicon.ico">
<link href="CSS/main.css" rel="stylesheet" type="text/css">
</head>

<body>
<header>
        	
    </header>
    <nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li>
          <a>Jets</a>
          <ul>
            <li><a href="f15.html">F-15</a></li>
            <li><a href="f22.html">F-22</a></li>
            <li><a href="f35.html">F-35</a></li>
            <li><a href="b52.html">B-52 Stratofortress</a></li>
            <li><a href="su35.html">SU-35</a></li>
            <li><a href="me163.html">Me-163 Komet</a></li>
          </ul>
        </li>
        <li><a href="gallery.html">Gallery</a></li>
        <li><a href="quiz.html">Quiz</a></li> 
        <li><a href="login.html">Login</a></li>   
        <li><a href="prototype.html">Prototype</a></li>   
      </ul>
</nav>
 <content>
		<div class="bodybox">
        <h1>WELCOME</h1>
        <p>LOGIN SUCCESSFUL</p></div>
</content>
    <animation>
    
    </animation>
<br>
<div class="contentbox">
	<?php
	$userid = $_POST["userid"];
	$password = $_POST["password"];
	
	IF ($userid == "admin" AND $password == "admin") {
		echo ("<h2>Welcome Back, Administrator</h2>");
	} ELSE {
		echo ("<h2>Welcome, ".$userid."</h2>");	
	}
	?>
    </div>
    
</body>
</html>