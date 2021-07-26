
<!-- Menu --> 
<nav id="nav" class="nav">
	<ul>
		<a href="index.php"><li>Inicio</li></a>

		<?php 
			$categorias = conseguirCategorias($db);
			if (!empty($categorias)):
				while($categoria = mysqli_fetch_assoc($categorias)): 
		?>
		
				<a href="categoria.php?id=<?=$categoria['id']?>">
					<li><?=$categoria['categoria'];?></li>
				</a>

		<?php 
				endwhile; 
			endif;		
		?>	
	</ul>
</nav>
