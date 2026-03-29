def greet(name):
    return f"Hello {name}"

def get_initials(full_name):
    return "".join(name[0].upper() for name in full_name.split())
    
