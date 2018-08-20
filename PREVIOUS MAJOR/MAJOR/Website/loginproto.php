<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>RAF Welcome</title>
<link rel="shortcut icon" href="Img/favicon.ico">
<link href="CSS/prototype.css" rel="stylesheet" type="text/css">
</head>

<body>
<header>
        <img src="Img/base_images/raptorprototype.jpg">	
    </header>
        <nav>
    <ul>
        <li><a href="prototype.html">Home</a></li>
        <li><a href="aboutproto.html">About</a></li>
        <li>
          <a>Jets</a>
          <ul>
            <li><a href="f15proto.html">F-15</a></li>
            <li><a href="f22proto.html">F-22</a></li>
            <li><a href="f35proto.html">F-35</a></li>
            <li><a href="b52proto.html">B-52 Stratofortress</a></li>
            <li><a href="su35proto.html">SU-35</a></li>
            <li><a href="me163proto.html">Me-163 Komet</a></li>
          </ul>
        </li>
        <li><a href="galleryproto.html">Gallery</a></li>
        <li><a href="quizproto.html">Quiz</a></li> 
        <li><a href="loginproto.html">Login</a></li> 
        <li><a href="index.html">Return To Site</a></li>     
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