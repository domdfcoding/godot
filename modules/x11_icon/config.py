def can_build(env, platform):
    return env["platform"] == "linuxbsd"

def configure(env):
    pass

def get_opts(platform):
    if platform == "linuxbsd":
        return [("x11_icon", "Window icon for X11 (BSD/Linux only). Defaults to the godot logo", "default_icon.png")]
