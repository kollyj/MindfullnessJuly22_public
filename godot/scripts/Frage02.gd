extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
func move(target):
	var move_tween = get_node("move_tween")
	move_tween.interpolate_property(self, "position", position, target, 2, Tween.TRANS_QUINT, Tween.EASE_OUT)
	move_tween.start()


func _on_start_pressed():
	pass # Replace with function body.
