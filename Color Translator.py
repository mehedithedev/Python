def color_translator(color):
    if color=="blue":
        return "#0000ff"
    elif color=="yellow":
        return "unknown"
    elif color=="red":
        return "#ff0000"
    elif color=="black":
        return "unknown"
    elif color=="green":
        return "#00ff00"
    else:
        return "unknown"
print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown