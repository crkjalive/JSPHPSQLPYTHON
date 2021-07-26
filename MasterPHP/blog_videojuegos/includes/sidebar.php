<aside id="sidebar" class="sidebar">
	
	<?php if (isset($_SESSION['usuario'])): ?>
	<div id="usuario_logueado" class="bloque usuario_logueado">
		<h3 class="usuario">Bienvenido: <?=$_SESSION['usuario']['name'].' '.$_SESSION['usuario']['lastName'] ?> </h3>
		<!-- botones -->
		<div class="botones" ><a href="entrada.php">Crear Entrada</a></div>
		<div class="botones" ><a href="categoria.php">Crear Categoria</a></div>
		<div class="botones" ><a href="misDatos.php">Mis Datos</a></div>
		<div class="botones" ><a href="cerrar.php">Salir</a></div>
	</div>
	<?php endif; ?>

	<div class="login bloque" id="login">
		<h3>Identificate</h3>
		<?php if (isset($_SESSION['error_login'])): ?>
		<div class="alerta">
			<?=$_SESSION['error_login']; ?>
		</div>
		<?php endif; ?>

		<form action="login.php" method="POST">
			<label for="email">Email</label>
			<input type="text" name="email" />

			<label for="password">Contraseña</label>
			<input type="password" name="password" />

			<input type="submit" value="Entrar" />
		</form>
	</div>

	<div class="registro bloque" id="registro">

		<h3>Registrate</h3>
		
		<?php if(isset($_SESSION['completado'])): ?>
			<div class="alerta-exito">
				<?=$_SESSION['completado']; ?>
			</div>
		<?php elseif(isset($_SESSION['errores']['general'])): ?>
			<div class="alerta">
				<?=$_SESSION['errores']['general'] ?>
			</div>
		<?php endif; ?>
		
		<?php echo isset($_SESSION['errores']) ? mostrarError($_SESSION['errores'], 'name') : ''; ?>
		<?php echo isset($_SESSION['errores']) ? mostrarError($_SESSION['errores'], 'lastName') : ''; ?>
		<?php echo isset($_SESSION['errores']) ? mostrarError($_SESSION['errores'], 'email') : ''; ?>
		<?php echo isset($_SESSION['errores']) ? mostrarError($_SESSION['errores'], 'password') : ''; ?>
	
		<form action="registro.php" method="POST">

			<label for="name">Nombre</label>
			<input type="text" name="name" />

			<label for="lastName">Apellido</label>
			<input type="text" name="lastName" />

			<label for="email">Email</label>
			<input type="text" name="email" />
			
			<label for="password">Contraseña</label>
			<input type="password" name="password" />
			
			<input type="submit" value="Registrar" name="submit" />
		</form>
		<?php borrarErrores() ?>
	</div>
</aside>