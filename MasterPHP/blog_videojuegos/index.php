<?php include 'includes/header.php'; ?>

<div class="container" id="container">

<!-- Caja Principal -->
<div id="principal" class="principal">
	<h1>Ultimas entradas</h1>

	<?php
		$posts = conseguirEntradas($db);
		if (!empty($posts)):
			while ($post = mysqli_fetch_assoc($posts)):
	?>
	
	<a href="">	
		<article class="entradas">
			<h2> <?=$post['title']?> </h2>
			<p> <?= substr($post['description'],0,200)."..." ?> </p>
		</article>
	</a>

	<?php					
			endwhile;
		endif;
	?>
	
	<div class="todas_entradas">
		<a href="">ver todas las entradas</a>
	</div>

</div>

	<!-- Barra lateral -->
<?php include 'includes/sidebar.php'; ?>

</div>

<!-- Pie de página -->
<?php require_once 'includes/footer.php'; ?>

