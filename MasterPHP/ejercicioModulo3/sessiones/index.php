<?php

session_start();

$variable_local = "Hola soy una variable local";

$_SESSION['variable_persistente'] = "HOLA SOY UNA SESSION ACTIVA";

echo $variable_local.'<br/>';
echo $_SESSION['variable_persistente'];




