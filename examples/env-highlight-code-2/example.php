<html>
<head>
<?php 
include '../../include/head-sub-sub.php';
include '../latex-highlight.php';
?>
</head>
<body>

<?php
ini_set('default_charset','UTF8');
include '../../include/header-sub-sub.php';
?>

<h1>src/example.tex</h1>
<pre><code class="latex">
<?php
$archivo = 'src/example.tex';
if (file_exists($archivo)) {
    $contenido = file_get_contents($archivo);
    echo htmlspecialchars($contenido);
} 
else 
{
    echo "El archivo '$archivo' no existe.";
}
?>
</code></pre>

<div class="header libgradient">
	<p>
		<div class="whiteblock">
		<a href="src.zip"><img src="example.png"/></a>
		</div>
	</p>
</div>

<?php 
include '../../include/footer-sub-sub.php';
?>

</body>
</html>
