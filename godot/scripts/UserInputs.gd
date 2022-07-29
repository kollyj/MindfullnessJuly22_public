extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	# change background music: 
	Sounds.SetAppState("StartApp")

func move(target):
	var move_tween = get_node("move_tween")
	move_tween.interpolate_property(self, "position", position, target, 2, Tween.TRANS_QUINT, Tween.EASE_OUT)
	move_tween.start()
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

func _on_continue01_pressed():
	get_node("Frage02").move(Vector2(-576,0))
	get_node("Frage01").move(Vector2(-576,0))



func _on_back02_pressed():
	get_node("Frage02").move(Vector2(0,0))
	get_node("Frage01").move(Vector2(0,0))


func _on_continue02_pressed():
	get_node("Frage03").move(Vector2(-1152,0))
	get_node("Frage02").move(Vector2(-1152,0))


func _on_continue03_pressed():
	get_node("Frage03").move(Vector2(-1728,0))
	get_node("LetsGo").move(Vector2(-1728,0))


func _on_start_pressed():
	# I want to enter in the Game!! 
	get_tree().change_scene("res://scenes/game.tscn")


func _on_back03_pressed():
	get_node("Frage02").move(Vector2(-576,0))
	get_node("Frage03").move(Vector2(-576,0))
