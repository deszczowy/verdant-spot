"""
from svg import SvgPath
l = []
l.append((123, 987))
l.append((876, 456))
l.append((675, 345))
d = SvgPath(123, "simple", l).render()
print(d)
"""

"""
from db import ProjectDb
db = ProjectDb("dev/database.db")
print(db.get_elements())
print(db.get_layers())
"""

"""
from db import DbUpgrader
upg = DbUpgrader("dev/upg.db")
upg.upgrade()
"""

from db import ProjectDb
from svg import ProjectBuilder, ProjectRenderer

pd = ProjectDb("dev/database.db")
elements = pd.get_elements()
info = pd.get_info()
rs = ProjectBuilder().build(info, elements)
rr = ProjectRenderer().render(rs)
print(rs)
print(rr)