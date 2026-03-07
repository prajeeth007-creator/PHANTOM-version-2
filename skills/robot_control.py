def move_robot(direction):
    direction = direction.lower().strip()

    if direction == "forward":
        return "Robot moving forward"

    elif direction == "backward":
        return "Robot moving backward"

    elif direction == "left":
        return "Robot turning left"

    elif direction == "right":
        return "Robot turning right"

    else:
        return "Unknown direction. Try forward, backward, left, or right."