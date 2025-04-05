from .coordinate import SvgCoordinate

class SvgGrid:

    def generate(self, width, height, center_x, center_y, grid_spacing, coordinate_system) -> str:

        svg = '<g id="grid">'

        # Axes
        c0 = coordinate_system.get_svg_point(center_x, center_y)
        print(c0)

        d = f'M {-width} {c0[1]} H {2*width} M {c0[0]} {-height} V {2*height}'
        svg += f'<path d="{d}" stroke="black" stroke-width="0.2" fill="none" />'

        # Grid
        d = ""
        
        # Vertical
        x = -width
        while x <= 2*width:
            if x != c0[0]:  # Skip axis X
                d += f'M {x} {-height} V {height} '
            x += grid_spacing
        
        # Horizontal
        y = 0
        while y <= height:
            if y != c0[1]:  # Skip axis Y
                d += f'M {-width} {y} H {2*width} '
            y += grid_spacing
        
        svg += f'<path d="{d}" stroke="black" stroke-width="0.1" stroke-dasharray="1 1" fill="none" />'

        # Center
        svg += f'<circle cx="{c0[0]}" cy="{c0[1]}" r="3" fill="none" stroke="black" stroke-width="0.1" />'
        svg += '</g>'
        return svg