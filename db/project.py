from .client import DbBaseClient

class ProjectDb(DbBaseClient):
    QUERIES = {
        "get_elements": """
        select
            l.id as [layer_id],
            e.id as [id],
            e.caption as [caption],
            k.symbol as [kind],
            p.x as [x],
            p.y as [y]
        from layer as l
        join element as e on e.layer = l.id
        join kind as k on k.id = e.kind
        join point as p on e.id = p.element
        order by l.succession, e.id, p.succession""",

        "get_layers": """
        select
            l.id as [layer_id],
            l.label as [label],
            l.succession as [order],
            l.visible as [is_visible]
        from layer as l
        order by l.succession""",

        "get_kinds": """
        select
            k.id as [kind_id],
            k.label as [label],
            k.symbol as [symbol],
            k.svg as [picture]
        from kind as k""",

        "get_elements_on_layer": """
        select
            l.id as [layer_id],
            e.id as [id],
            e.caption as [caption],
            k.symbol as [kind],
            p.x as [x],
            p.y as [y]
        from layer as l
        join element as e on e.layer = l.id
        join kind as k on k.id = e.kind
        join point as p on e.id = p.element
        where l.id = ?
        order by l.succession, e.id, p.succession""",
    }

    def get_elements(self) -> list[dict]:
        return self.execute_select(self.QUERIES["get_elements"])

    def get_layers(self) -> list[dict]:
        return self.execute_select(self.QUERIES["get_layers"])

    def get_kinds(self) -> list[dict]:
        return self.execute_select(self.QUERIES["get_kinds"])

    def get_elements_on_layer(self, layer_id: int) -> list[dict]:
        return self.execute_select(self.QUERIES["get_elements_on_layer"], (layer_id,))