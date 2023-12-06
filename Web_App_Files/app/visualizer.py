import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

def create_plot(x, y, title):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    ax = plt.gca()
    ticks = np.arange(-2 * np.pi, 2.5 * np.pi, np.pi/2)

    tick_labels = []
    for tick in ticks:
        if tick == 0:
            tick_labels.append("0")
        elif tick / np.pi == 1:
            tick_labels.append("$\pi$")
        elif tick / np.pi == -1:
            tick_labels.append("$-\pi$")
        elif tick / np.pi > 0:
            tick_labels.append(f"${{{int(tick / np.pi)}}}\pi$")
        else:
            tick_labels.append(f"$-{{{int(abs(tick / np.pi))}}}\pi$")
    
    ax.set_xticks(ticks)
    ax.set_xticklabels(tick_labels)

    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    plt.close()

    return f"data:image/png;base64,{image_base64}"

def plot_function(function_name):
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    if function_name == 'sin':
        y = np.sin(x)
        title = 'y = sin(x)'
    elif function_name == 'cos':
        y = np.cos(x)
        title = 'y = cos(x)'
    elif function_name == 'tan':
        y = np.tan(x)
        title = 'y = tan(x)'
    elif function_name == 'cot':
        y = 1 / np.tan(x)
        title = 'y = cot(x)'
    else:
        return None

    return create_plot(x, y, title)

def plot_inverse_function(function_name):
    x = np.linspace(-1, 1, 1000)
    if function_name == 'sin':
        y = np.arcsin(x)
        title = 'y = arcsin(x)'
    elif function_name == 'cos':
        y = np.arccos(x)
        title = 'y = arccos(x)'
    elif function_name == 'tan':
        y = np.arctan(x)
        title = 'y = arctan(x)'
    elif function_name == 'cot':
        y = np.pi / 2 - np.arctan(x)
        title = 'y = arccot(x)'
    else:
        return None

    return create_plot(x, y, title)
