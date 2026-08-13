import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

hwnd = 19664652

# Get window class name
class_buf = ctypes.create_unicode_buffer(256)
user32.GetClassNameW(hwnd, class_buf, 256)
print(f"Class name: {class_buf.value}")

# Get window text
text_buf = ctypes.create_unicode_buffer(256)
user32.GetWindowTextW(hwnd, text_buf, 256)
print(f"Window text: '{text_buf.value}'")

# Get extended style
ex_style = user32.GetWindowLongW(hwnd, -20)
print(f"Extended style: {hex(ex_style)}")

# Get normal style
style = user32.GetWindowLongW(hwnd, -16)
print(f"Style: {hex(style)}")

# Check if window is visible
visible = user32.IsWindowVisible(hwnd)
print(f"Is visible: {visible}")

# Enumerate child windows
children = []
def enum_child(child_hwnd, lparam):
    child_class = ctypes.create_unicode_buffer(256)
    user32.GetClassNameW(child_hwnd, child_class, 256)
    child_text = ctypes.create_unicode_buffer(256)
    user32.GetWindowTextW(child_hwnd, child_text, 256)
    r = ctypes.c_long * 4
    rect = (ctypes.c_long * 4)()
    user32.GetWindowRect(child_hwnd, ctypes.byref(rect))
    children.append({
        'hwnd': child_hwnd,
        'class': child_class.value,
        'text': child_text.value,
        'rect': (rect[0], rect[1], rect[2], rect[3])
    })
    return True

WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)
user32.EnumChildWindows(hwnd, WNDENUMPROC(enum_child), 0)

print(f"\nChild windows ({len(children)}):")
for c in children:
    print(f"  hwnd={c['hwnd']} class='{c['class']}' text='{c['text']}' rect={c['rect']}")

# Also check parent
parent = user32.GetParent(hwnd)
print(f"\nParent hwnd: {parent}")

# Get owner
owner = user32.GetWindow(hwnd, 4)  # GW_OWNER
print(f"Owner hwnd: {owner}")
