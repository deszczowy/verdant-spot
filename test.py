from engine import VEngine

file_name = "dev/data.txt"
e = VEngine()
e.load_project(file_name)
e.store_project("{}-2".format(file_name))