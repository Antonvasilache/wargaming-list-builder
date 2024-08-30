# Enable mouse wheel scrolling
def on_mouse_wheel(event, canvas):
    if event.delta:
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    else:
        if event.num == 4:
            canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            canvas.yview_scroll(1, "units")
            
def bind_mousewheel_to_widget(widget, canvas):
    widget.bind("<MouseWheel>", lambda e: on_mouse_wheel(e, canvas))  # Windows and MacOS
    widget.bind("<Button-4>", lambda e: on_mouse_wheel(e, canvas))    # Linux Scroll Up
    widget.bind("<Button-5>", lambda e: on_mouse_wheel(e, canvas))    # Linux Scroll Down
    for child in widget.winfo_children():
        bind_mousewheel_to_widget(child, canvas)  # Recursively bind to all children   