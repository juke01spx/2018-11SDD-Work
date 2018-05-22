<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>RAF Quiz Results</title>
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
        <h1>RESULTS</h1>
        <p>Your results on the slightly interesting quiz about jets</p></div>
</content>
    <animation>
    
    </animation>
    
<br>
	<div class="contentbox">

	<?php
	
	$totalscore = 0;
	$answer1 = $_POST["question1"];
	$answer2 = $_POST["question2"];
	$answer3 = $_POST["question3"];
	$answer4 = $_POST["question4"];
	$answer5 = $_POST["question5"];
	$answer6 = $_POST["question6"];
	$answer7 = $_POST["question7"];
	$answer8 = $_POST["question8"];
	$answer9 = $_POST["question9"];
	$answer10 = $_POST["question10"];
	
	
	if ($answer1=="T") {
		$totalscore = $totalscore + 1;
		echo "<strong><p>Question 1</strong> is correct. The F-22 is very expensive.</p>";
	} else {
		echo "<strong><p>Question 1</strong> was answered incorrectly.</p>";
	}
	
	if ($answer2=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 2</strong> is correct. The Me-163 proved to be quite ineffective in actual combat scenarios.</p>";
	} else {
		echo "<p><strong>Question 2</strong> was answered incorrectly</p>";
	}
	
	if ($answer3=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 3</strong> is correct. The Me-163 is rocket powered which makes it extremely fast.</p>";
	} else {
		echo "<p><strong>Question 3</strong> was answered incorrectly</p>";
	}
	
	if ($answer4=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 4</strong> is correct. The F-17 was a prototype for the F-18 and was never actually deployed into combat.</p>";
	} else {
		echo "<p><strong>Question 4</strong> was answered incorrectly</p>";
	}
	
	if ($answer5=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 5</strong> is correct. The Boeing B-52 Stratofortress is an American strategic bomber.</p>";
	} else {
		echo "<p><strong>Question 5</strong> was answered incorrectly</p>";
	}
	
	if ($answer6=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 6</strong> is correct. Chuck Yeager was the first human to officialy break the sound barrier.</p>";
	} else {
		echo "<p><strong>Question 6</strong> was answered incorrectly</p>";
	}
	
	if ($answer7=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 7</strong> is correct. The Bell X-1 was the first aircraft to go supersonic.</p>";
	} else {
		echo "<p><strong>Question 7</strong> was answered incorrectly</p>";
	}
	
	if ($answer8=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 8</strong> is correct. While Von Ohain is considered to be the designer of the turbojet, and also flew the first turbojet powered aircraft, the modern turbojet is based on the prototype that Whittle invented, not Ohain's version.</p>";
	} else {
		echo "<p><strong>Question 8</strong> was answered incorrectly</p>";
	}
	
	if ($answer9=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 9</strong> is correct. The F-16 has just a single engine.</p>";
	} else {
		echo "<p><strong>Question 9</strong> was answered incorrectly</p>";
	}
	
	if ($answer10=="T") {
		$totalscore = $totalscore + 1;
		echo "<p><strong>Question 10</strong> is correct. Two B-29 Superfortress' named 'Enola Gay' (1st Bomb - Little Boy) and 'Bockscar' (2nd Bomb - Fat Man) dropped the bombs.</p>";
	} else {
		echo "<p><strong>Question 10</strong> was answered incorrectly</p>";
	}
	
	
	if ($totalscore==0) {
		echo "<h1>What happened?</h1><h2>You got no answers correct!</h2>";
	}
	
	if ($totalscore==1) {
		echo "<h1>Terrible</h1>";
		echo "<h2>You got ".$totalscore." question correct</h2>";
	}
	
	if ($totalscore==2) {
		echo "<h1>Mediocre</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==3) {
		echo "<h1>Mediocre</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==4) {
		echo "<h1>Good Job</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==5) {
		echo "<h1>Good Job</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==6) {
		echo "<h1>Great Work</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==7) {
		echo "<h1>Great Work</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==8) {
		echo "<h1>Awesome</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==9) {
		echo "<h1>So Close!</h1>";
		echo "<h2>You got ".$totalscore." questions correct</h2>";
	}
	
	if ($totalscore==10) {
		echo "<h1>Congratulations</h1>";
		echo "<h2>You got everything correct!</h2>";
		echo "<a href=what.html>┗▛▄▖</a>";
	}
		
	?>
</div>


</body>
</html>