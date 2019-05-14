<? php

$x = 5;

$y = 10;

function fun()

  {

    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];

 }

fun();

 echo $y;

?>