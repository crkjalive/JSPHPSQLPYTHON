<?php

session_start();

// esta variable global fue declarada desde el index, y esta disponible, para cualquier archivo desntro de la sesion activa
echo $_SESSION['variable_persistente'];

// esta variable fue declarada en otro archivo, lo cual no esta disponible desde otros archivos ya que es una variable local

// echo $variable_local.'<br/>';


