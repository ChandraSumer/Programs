<!DOCTYPE html>
<html>
<head>
<style>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: rgb(0,55,255);
}
li a.active {
  background-color: darkblue;
  color: white;
}
li {
  float: left;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 19px;
  text-decoration: none;
}

li a:hover {
  background-color: rgb(0,50,200);
      color: white;
}
</style>
</head>
<body style="background-color:rgb(232, 239, 255)">

<ul style="font-size:20px;"><b>
  <li><a  href="about.html">About Me</a></li>
  <li><a href="learn.html">Learn</a></li>
  <li><a href="quiz.html">Quiz</a></li>
</ul>
<?php
$s=0;
if(isset($_POST['q1']) && $_POST['q1']=="d"){
$s++;
}
if(isset($_POST['q2']) && $_POST['q2']=="1"){
$s++;
}
if(isset($_POST['q3']) && $_POST['q3']=="2"){
$s++;
}
if(isset($_POST['q4']) && $_POST['q4']=="2"){
$s++;
}
if(isset($_POST['q5']) && $_POST['q5']=="4"){
$s++;
}
if(isset($_POST['q6']) && $_POST['q6']=="3"){
$s++;
}
if(isset($_POST['q7']) && $_POST['q7']=="4"){
$s++;
}
if(isset($_POST['q8']) && $_POST['q8']=="3"){
$s++;
}
if(isset($_POST['q9']) && $_POST['q9']=="1"){
$s++;
}
if(isset($_POST['q10']) && $_POST['q10']=="3"){
$s++;
}
echo '<p>Your score is: '.$s.'<p>';
?>
</body>
</html>
</body>
</html>
