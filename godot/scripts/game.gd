extends Node2D


var IMG_CircleRed = preload("res://sprites/CircleRed.png");
var IMG_CircleBlue = preload("res://sprites/CircleBlue.png")
var IMG_CircleGreen = preload("res://sprites/CircleGreen.png");
var IMG_SquareRed = preload("res://sprites/SquareRed.png")
var IMG_SquareBlue = preload("res://sprites/SquareBlue.png")
var IMG_SquareGreen = preload("res://sprites/SquareGreen.png")
#var array_to_python = [0, 10, 100]

#onready var python_array = array_to_python
onready var http_request = HTTPRequest.new()





# Called when the node enters the scene tree for the first time.
func _ready():
	# change background music: 
	Sounds.SetAppState("Game")
	
	# Create an HTTP request node and connect its completion signal.
	add_child(http_request)
	http_request.connect("request_completed", self, "_http_request_completed")


# Called when the HTTP request is completed.
func _http_request_completed(result, response_code, headers, body):
	var response = parse_json(body.get_string_from_utf8())
	print(" this is the answer (next action) from python when pushing the button:  ", response)  # this is the answer from python
	var new_action = response #  take this variable and draw element on screen
	
	# geht nicht, da es komplett in neue scene geht. 
	# get_tree().change_scene("res://simulations/sprite" + new_action + ".tscn")
	# evt zuerst hier alle stimulations-scenes schliessen. dann mit if statement nur die richtige zeigen.
	 
	if new_action == 'CircleRed':
		get_node("Particles2D").texture = IMG_CircleRed
		get_node("Particles2D").amount = 30 
		get_node("Particles2D").speed_scale = 1
	if new_action == 'CircleBlue':
		get_node("Particles2D").texture = IMG_CircleBlue
		get_node("Particles2D").amount = 10
		get_node("Particles2D").speed_scale = 0.8
	if new_action == 'CircleGreen':
		get_node("Particles2D").texture = IMG_CircleGreen
		get_node("Particles2D").amount = 3
		get_node("Particles2D").speed_scale = 0.5
	if new_action == 'SquareRed':
		get_node("Particles2D").texture = IMG_SquareRed
		get_node("Particles2D").amount = 30
		get_node("Particles2D").speed_scale = 1
	if new_action == 'SquareBlue':
		get_node("Particles2D").texture = IMG_SquareBlue
		get_node("Particles2D").amount = 10
		get_node("Particles2D").speed_scale = 0.8
	if new_action == 'SquareGreen':
		get_node("Particles2D").texture = IMG_SquareGreen
		get_node("Particles2D").amount = 3
		get_node("Particles2D").speed_scale = 0.5		
	
	#var next_screen = load("res://simulations/sprite" + new_action + ".tscn").instance()
	#add_child(next_screen)
	

		
	# instancing sprites, via scenes, depending on if-conditions: 
	#if new_screen == 'CircleRed':
	#	var sprite = load("res://simulations/spriteCircleRed.tscn")
	#	var sprite_ins = sprite.instance()
	#	add_child(sprite_ins)
	#	#sprite_ins.position = Vector2(100,200)
	#if new_screen == 'SquareGreen':
	#	var sprite = load("res://scenes/spriteSquareGreen.tscn")
	#	var sprite_ins = sprite.instance()
	#	add_child(sprite_ins)
	#	#sprite_ins.position = Vector2(100,200)
		
		
		# idee: load scene. dann in scene: on function ready: füge sachen hinzu per script. 
		# am besten sieht momentan particles2D aus. lerne wie das mit scripts geht. 
		#benutze dann dort im script die vairbale "new_screen" um spezifische particles zu bauen. 



func _on_positiveReward_pressed():
	# Perform the HTTP request. The URL below returns some JSON as of writing.
	var fields = 10 #  this is what we send to python
	var result = http_request.request("http://127.0.0.1:5000/positiveReward", 
										PoolStringArray(['Content-Type: application/json']), 
										false, 2, to_json(fields)) # 2= post-request
	if result != OK:
		push_error("An error occurred in the HTTP request.")


func _on_negativeReward_pressed():
	# Perform the HTTP request. The URL below returns some JSON as of writing.
	var fields = -10 #  this is what we send to python
	var result = http_request.request("http://127.0.0.1:5000/negativeReward", PoolStringArray(['Content-Type: application/json']), false, 2, to_json(fields)) # 2= post-request
	if result != OK:
		push_error("An error occurred in the HTTP request.")


func _on_neutralReward_pressed():
	# Perform the HTTP request. The URL below returns some JSON as of writing.
	var fields = 0 #  this is what we send to python
	var result = http_request.request("http://127.0.0.1:5000/neutralReward", PoolStringArray(['Content-Type: application/json']), false, 2, to_json(fields)) # 2= post-request
	if result != OK:
		push_error("An error occurred in the HTTP request.")



func _on_exit_pressed():
	get_tree().change_scene("res://scenes/Exit.tscn")
