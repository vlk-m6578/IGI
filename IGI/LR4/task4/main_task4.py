import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle
from task4.square import Square
from task4.utils import validate_float

def create_square():
    """Square creation workflow."""
    try:
        radius = validate_float("Enter circle radius: ")
        color = input("Enter square color: ").strip()
        label = input("Enter shape label: ").strip()
        
        square = Square(radius, color)
        side = square.side_length
        center = side / 2  # Center
        # Create
        fig, ax = plt.subplots()
        
        circle = Circle(
            (center, center), 
            radius,
            edgecolor="black", 
            fill=False, 
            linestyle="--"
        )
        ax.add_patch(circle)
        
        # Square
        square_plot = Rectangle(
            (0, 0), side, side,
            edgecolor=color, 
            facecolor=color,   
            fill=True, 
            linewidth=2
        )
        ax.add_patch(square_plot)
        
        # Settings
        ax.annotate(label, (center, center),
                    ha='center', va='center', fontsize=12)
        plt.xlim(center - radius - 1, center + radius + 1)
        plt.ylim(center - radius - 1, center + radius + 1)
        plt.gca().set_aspect('equal')
        
        # Save
        plt.savefig("square.png")
        print("Square saved to square.png")

        plt.title("Square Inscribed in Circle")
        
        plt.show()

        square = Square(radius, color)
        print("\n" + str(square))
        
    except Exception as e:
        print(f"Error: {str(e)}")