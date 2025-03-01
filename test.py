from svg import SvgPath

l = []
l.append((123, 987))
l.append((876, 456))
l.append((675, 345))
d = SvgPath(123, "simple", l).render()
print(d)