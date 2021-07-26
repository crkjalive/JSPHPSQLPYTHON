<?php require_once 'cabecera.php'; ?>
<div class='contenido_contacto'>
  <h1> formulario de contacto </h1>
  <?php 
if (isset($_POST['name'])) 
{
  echo 'Hola '.$_POST['name'];
}
else
{
  echo "envianos tu nombre para saber quien eres";
};
?>
  <form method="POST" for='contacto.php'>
  <label>Name:</label>
  <br/>
  <input type='text' name="name" placeholder='Nombre:'>
  <br/>
  <input type='submit' value='enviar'>
</form>
</div>
<?php require_once 'footer.php'; ?>
