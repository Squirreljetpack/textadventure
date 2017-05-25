help="\n"*2+"-"*90+"""
	Hello and welcome to Ether. This is a text-based adventure game, featuring natural
	language style input controls. Just type your command into the prompt '>' and the game
	will try to carry out your controls. Most of your commands will take the form of a command
	and an object (e.g.: 'throw' 'ball', 'look' 'around', 'use' 'item'). In special instances,
	modifiers may be used, (e.g. 'and', to perform multiple operations simultaneously, 'with'
	to combine multiple items).
	In addition to these, there are several special commands you can type in the prompt:
	'p' to bring up the menu.
	'i' to bring up your inventory.
	'm' to bring up the map.
	's' to bring up your stats and save.
	and 'h' to bring up this prompt again.

	The first part of this game focuses on survival. Your goal is make it through the days and
	nights and random dangers of this mysterious forest, all the while searching for an exit.
	There are three aspects you have to watch out for particularly: health, hunger and energy.
	The maximum for each of these stats can be augmented or decreased throughout the story.
	You start with 3 health. When your health reaches zero, you lose.
	You gain 4 hunger every night. Every night you spend with over 10 hunger, you lose one
	health.
	As for energy, its a marker of the actions remaining before the day ends. When it reaches
	zero, you go to sleep automatically, regardless of where you are. Ideally, you want to be
	in a shelter when that happens.
	All these stats can be viewed by typing 's'.
	Your first act should be to build a house, to keep yourself safe when night comes. Next,
	you can worry about acquiring and accumulating food and supplies. Once you have a
	sufficient supply, you can then set out on longer, more substantial journeys to explore
	your surroundings.
"""+"-"*90+"\n"

r7c6_1="""
	...

	You open your eyes to a kaleidoscope of lights, pearls that shimmer and coalesce around
	the edges of your vision. High above you a dry wind rustles the highest leaves, the quiet
	noise a sensible complement to the susurrus of the forest. You become aware of a prickly
	sensation: the bed of grass you are lying on sharp, short and vibrant, as if freshly cut -
	though its hard to imagine this place gets many visitors. As your vision sharpens, you
	notice a number of things. You are wearing comfortable t-shirt, a robust army jacket and a
	pair of worn jeans. Your feet are snuggly fitted into a pair of thick olefin socks. By
	your side, lay your leather hiking boots and backpack. You seem to be pretty deep into the
	forest: the forest is uniform in every direction and teems with signs of wildlife."""
r7c6_d="""
	The dense trees open into a bright clearing. Warm sunshine floods in; the sight of your
	origin brings you inexplicable peace."""
r7c6_n="""
	The dense trees open into a bright clearing. The moon basks the spot in a mysterious glow;
	the sight of your origin brings you inexplicable peace."""
r6c6="""
	There are many trees."""
rcmountains="""
	You walk into an insurmountably tall mountain range. Its barren peaks penetrate deep into
	the clouds even on a clear day as this. You cannot proceed any further this way."""
rcseas="""
	In front of you, the sea stretches into infinity in every direction. Though the weather is
	calm, far off into the distance roiling waves churn foam with barely restrained power. This
	is not something man can conquer. You cannot proceed any further this way."""
