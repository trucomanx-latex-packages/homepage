<html>
<head>
	<title> ..:: LATEX-MACROS-PACKAGES ::..</title>
	<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
  	<link href="imagenes/base.css" media="screen" rel="stylesheet" type="text/css">
	 <meta http-equiv="X-UA-Compatible" content="chrome=1">
</head>
<body>

<?php
 ini_set('default_charset','ISO-8859-1');
?>

	<div class="header gradient">
      <div class="top-nav darkblock">
        <a href="http://latex-macros-packages.sf.net/">Home</a> |
        <a href="http://sourceforge.net/projects/latex-macros-packages/">Develop</a> |
        <a href="http://sourceforge.net/projects/latex-macros-packages/files/">Download</a> |                
        <a href="https://sourceforge.net/p/latex-macros-packages/_members/">Contact</a>
      </div>

      <img width="4%" src="imagenes/latex-macros-packages.png">

      <div class="promo-area">

        <img style="float: left;" width="50%" src="imagenes/latex-macros-packages-screenshot.png">
        
        <h2>LATEX-MACROS-PACKAGES</h2>
        <p>Varios macros en latex.
		</p>
		<p>
			Desde la pagina des descargas de
			<a href="https://sourceforge.net/projects/latex-macros-packages/files/"><b>latex-macros-packages</b></a> 
			pueden ser obtenidos los paquetes.
		</p>        
      </div>
      
	</div>

	<div class="content">

      <div class="box">
		<h3>Que es el software libre?</h3>
        <div class="box-content">
<iframe width="180" height="150" src="https://www.youtube.com/embed/FvLJ2JotttM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        </div>       
      </div>
      
      <div class="box">
        <h3>Social</h3>
        <div class="box-content">
          <ul class="services">
            <li><a href="https://gnusocial.net/trucomanx"><img src="imagenes/gnusocial.png">GnuSocial</a></li>
          </ul>
          <ul class="services">
            <li><a href="https://diasp.org/people/68e40bb7f3f6d792"><img src="imagenes/diaspora+logo.png">Diaspora</a></li>
          </ul>
        </div>
        <h3>Sourceforge</h3>
        <div class="box-content">
        <a href="https://sourceforge.net/projects/latex-macros-packages/files/latest/download"><img alt="Download latex-macros-packages" src="https://img.shields.io/sourceforge/dm/latex-macros-packages.svg" ></a>
        </div>
      </div>      
       
      <div class="box">
        <h3>News</h3>
        <div class="box-content">
<?php
$rss_feed = simplexml_load_file("https://sourceforge.net/p/latex-macros-packages/activity/feed");
if(!empty($rss_feed)) 
{
    $i=0;
    foreach ($rss_feed->channel->item as $feed_item) 
    {
        if($i>=4) break;
        ?>
        <div><a class="feed_title" href="<?php echo $feed_item->link; ?>"><b><?php echo $feed_item->title; ?></b></a></div>
        <div><?php echo implode(' ', array_slice(explode(' ', $feed_item->description), 0, 14)) . "..."; ?></div>
        <?php		
        $i++;	
    }
}
?>
        </div>
      </div>

    </div>

  </body></html>
