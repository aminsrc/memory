from physical_memory import PhysicalMemory


def run():
    pm = PhysicalMemory(10)
    pm.print_memory()
    pm.write_sector(2, "hello")
    pm.write_segment(4, 2, ["memory", "management", "unit"])
    print(pm.read_sector(2))
    print(pm.read_segment(4, 3))
    pm.print_memory()


if __name__ == "__main__":
    run()