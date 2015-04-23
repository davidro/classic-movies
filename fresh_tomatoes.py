import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="shortcut icon" href="assets/ico/favicon.png">

    <title>Classic Full Length Movies </title>

    <link href="assets/css/hover_pack.css" rel="stylesheet">

    <!-- Bootstrap core CSS -->
    <link href="assets/css/bootstrap.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="assets/css/main.css" rel="stylesheet">
    <link href="assets/css/colors/color-74c9be.css" rel="stylesheet">
    <link href="assets/css/animations.css" rel="stylesheet">
    <link href="assets/css/font-awesome.min.css" rel="stylesheet">

    <style type="text/css" media="screen">
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
            width: 1280px;
            height:  960px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>

    <!-- JavaScripts needed at the beginning
    ================================================== -->

    <!-- Main Jquery & Hover Effects. Should load first -->
    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="assets/js/hover_pack.js"></script>

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
  </head>
'''

# The main page layout and title bar
main_page_content = '''

  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

	<!-- ========== HEADERWRAP ====================================================================================================
	=============================================================================================================================-->
    <div id="headerwrap">
    	<div class="container">
			<div class="row centered">
				<div class="col-lg-8 col-lg-offset-2 mt">
					<h1 class="animation slideDown">Classic Movies</h1>
          <h3 class="animation slideDown">
            Watch full length classic movies published on Youtube
          </h3>
    				<p class="mt"><a type="button" class="btn btn-cta btn-lg" href="https://developers.google.com/youtube/">Via Youtube API</a></p>
				</div>

			</div><!-- /row -->
    	</div><!-- /container -->
    </div> <!-- /headerwrap -->

	<!-- ========== BLOG POSTS ====================================================================================================
	=============================================================================================================================-->
	<div class="container">

        <!--
		<div class="row mt centered ">
			<div class="col-lg-4 col-lg-offset-4">
				<h3>What Is Happening?</h3>
				<hr>
			</div>
		</div>  -->
        <!-- /row -->

		<div class="row mt">
            {movie_tiles}
		</div><!-- /row -->

	</div><!-- /container -->


	<!-- ========== BLACK SECTION =================================================================================================
	=============================================================================================================================-->
	<!-- <div id="black">
		<div class="container pt">
			<div class="row mt centered">
				<div class="col-lg-3">
					<p><i class="fa fa-instagram"></i></p>
					<h1>21.337</h1>
					<hr>
					<h4>Pictures Taken</h4>
				</div>

				<div class="col-lg-3">
					<p><i class="fa fa-music"></i></p>
					<h1>9.764</h1>
					<hr>
					<h4>Songs Listened</h4>
				</div>

				<div class="col-lg-3">
					<p><i class="fa fa-trophy"></i></p>
					<h1>107</h1>
					<hr>
					<h4>Awards Earned</h4>
				</div>

				<div class="col-lg-3">
					<p><i class="fa fa-ticket"></i></p>
					<h1>209</h1>
					<hr>
					<h4>Movies Watched</h4>
				</div>

			</div>
		</div>
	</div> -->
  <!-- /black -->


	<!-- ========== CALL TO ACTION BAR ===============================================================================================
	=============================================================================================================================-->
	<div id="cta-bar">
		<div class="container">
			<div class="row centered">
				<a href="https://www.udacity.com/course/nd004"><h4>Made as part of Udacity Full Stack Web Developer Nanodegree project</h4></a>
			</div>
		</div><!-- /container -->
	</div><!-- /cta-bar -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="assets/js/bootstrap.min.js"></script>
    <script src="assets/js/retina.js"></script>


  	<script>

	</script>

  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''



<div class="col-lg-4 col-md-4 col-xs-12 desc movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img alt="{movie_title}" src="{poster_image_url}" width="350">
	<h3>{movie_title}</h3>
    <p>{storyline}</p>

</div><!-- col-lg-4 -->
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            storyline = movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
