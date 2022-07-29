extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.



func _on_Start_pressed():
# warning-ignore:return_value_discarded
	get_tree().change_scene("res://scenes/game.tscn")





func _on_GetUserInputs_pressed():
	get_tree().change_scene("res://scenes/UserInputs.tscn")
