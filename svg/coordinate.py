from outline import VProject

class SvgCoordinate:

    def __init__(self) -> None:
        self.center_x: float = float(0.0)
        self.center_y: float = float(0.0)
        self.max_x: float = float(0.0)
        self.max_y: float = float(0.0)
        self.zoom_factor: int = 1
    
    def up_to_date_with_project(self, project_data: VProject) -> None:
        self.center_x = project_data.Info.Center.X
        self.center_y = project_data.Info.Center.Y
        self.max_x = project_data.Info.Size.X
        self.max_y = project_data.Info.Size.Y        
        pass
    
    def get_svg_point(self, x: float, y: float) -> (float, float):
        svg_x = self.center_x + x
        svg_y = self.max_y - (self.center_y + y)
        return (svg_x, svg_y)