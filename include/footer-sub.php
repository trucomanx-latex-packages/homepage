
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
			<li><a href="https://gnusocial.net/trucomanx"><img src="../imagenes/gnusocial.png">GnuSocial</a></li>
		  </ul>
		  <ul class="services">
			<li><a href="https://diasp.org/people/68e40bb7f3f6d792"><img src="../imagenes/diaspora+logo.png">Diaspora</a></li>
		  </ul>
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
