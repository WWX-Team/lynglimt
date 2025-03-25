<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Projet Lynglimt</title>
		<link rel="stylesheet" href="css/default.css" />
		<link rel="stylesheet" href="css/footer.css" />
		<link rel="stylesheet" href="css/prompt.css" />
	</head>
	<body>
		<div id="view">
			<div class="navBar">
				<a href="main.html"><img src="assets/svg/logo.svg" class="mainLogo"/></a>
			</div>
			<div id="main" class="pageFitC">
				<div class="box">
					<h1 class="firstTitle" id="discover">Découvrez Lynglimt</h1> 
					<p class="boxText">Le <b>Projet Lynglimt</b> permet d'identifier des tableaux ou sculptures à partir d'une description usuelle.</p>
					<div class="box">
						<div class="example">
							<div class="examplePrompt">
								<p class="exPromptText"></p>
								<svg class="exPromptIMG" version="1.1" viewBox="0 0 512 512"><path fill="currentColor" d="M460 52a177 177 0 0 0-269 228l-41 40-7-8c-4-4-10-4-13 0L15 427l-8 10a50 50 0 0 0 78 60l59-58a9 9 0 1 0-14-14l-58 59-1 1-44-44 1-1 108-108 44 44-30 29a9 9 0 1 0 14 14l36-37a9 9 0 0 0 0-13l-8-7 40-41a176 176 0 0 0 228-19c69-69 69-181 0-250zM53 493a31 31 0 0 1-34-34l34 34zm126-145-15-15 38-39a178 178 0 0 0 16 16l-39 38zm268-59a158 158 0 0 1-237-14 158 158 0 1 1 237 14z"/><path fill="currentColor" d="M424 88a9 9 0 1 0-13 13 106 106 0 0 1 0 152 107 107 0 1 1-21-168 9 9 0 1 0 9-16 125 125 0 1 0 25 19z"/></svg>
							</div>
							<div class="exampleResult">
								<img class="exResultIMG" src="assets/img/example/1.jpg" id="exampleIMG" style="filter: opacity(0);">
								<p class="exResultText"></p>
							</div>
						</div>
						<div class="exampleNav">
							<span class="dot active" data-index="0"></span>
							<span class="dot" data-index="1"></span>
							<span class="dot" data-index="2"></span>
							<span class="dot" data-index="3"></span>
							<span class="dot" data-index="4"></span>
							<span class="dot" data-index="5"></span>
						</div>
					</div>
					<div class="alignC"><a class="button" href="pages/app.html">Découvrir Lynglimt</a></div>
					<div class="box">
						<h3 id="about">À propos</h3>
						<p class="boxText">Le <b>Projet Lynglimt</b>, commencé en mars 2025, est un projet réalisé par des lycéens français.</p>
						<p class="boxText">Il propose un moteur de recherche, Lynglimt, permettant de rechercher diverses œuvres d'art en les décrivant,
							sans forcément connaître leur titre, leur auteur. Plus la description est précise, plus le résultat sera cohérent.</p>
						<p class="boxText"><a href="pages/about.html">Lire la suite...</a></p>
					</div>
				</div>
			</div>
		</div>
		<footer>
			<div class="footerBar alignC">
			<ul class="footerLST pageFitC">
				<li class="footerTitle"> Informations légales
					<ul class="footerColumn">
						<li> <a class="footerEl" href="pages/terms_of_use.html">Conditions d'utilisation</a> </li>
						<li> <a class="footerEl" href="pages/privacy_policy.html">Politique de confidentialité</a> </li>
						<li> <a class="footerEl" href="pages/terms_of_use.html">Mentions légales</a> </li>
					</ul> </li>
				<li class="footerTitle"> À Propos
					<ul class="footerColumn">
						<li class="footerEl"> <a href="pages/about.html">À propos</a> </li> 
						<li class="footerEl"> <a href="pages/about_us.html">Notre équipe</a></li>
					</ul> </li>
				<li class="footerTitle"> Aide
					<ul class="footerColumn">
						<li class="footerEl"> <a href="pages/FAQ.html">F.A.Q.</a> </li>
					</ul> </li>
				<li class="footerTitle"> Ressources
					<ul class="footerColumn">
						<li class="footerEl"> <a href="pages/about.html">Documentation</a> </li> 
					</ul> </li>
			</ul>
		</footer>
		<script src="js/main.js"></script>
	</body>
</html>
