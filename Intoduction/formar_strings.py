#the str.format allows for variable substitution and string concatenation

message = "Hello {2} {1} {0}," + " " + "How are you doing?"
print(message.format("Isaac", "Yaw", "Amponsah"))