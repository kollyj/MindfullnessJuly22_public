extends Node
# following: https://www.youtube.com/watch?v=6VZnabKdlQ8&ab_channel=GameDevelopmentCenter
onready var background_music_normal = get_tree().get_root().get_node("AppRoot/BackgroundNormal")
onready var background_music_game = get_tree().get_root().get_node("AppRoot/BackgroundGame")

#onready var background_music_normal = get_parent().get_node("AppRoot/BackgroundNormal")
#onready var background_music_game = get_parent().get_node("AppRoot/BackgroundGame")

var app_state setget SetAppState

# Called when the node enters the scene tree for the first time.
func _ready():
	SetAppState("StartApp")

func SetAppState(new_value):
	if not app_state == new_value: 
		app_state = new_value 
		print("app state = " + app_state)
		ChangeMusic()
	else: 
		pass

func ChangeMusic(): 
	match app_state: 
		"StartApp":
			background_music_normal._set_playing(true)
		"Game":
			background_music_normal._set_playing(false)
			background_music_game._set_playing(true)
		"Exit": 
			background_music_normal._set_playing(true)
			background_music_game._set_playing(false)
