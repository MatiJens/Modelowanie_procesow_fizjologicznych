from Vessel import Vessel


class VascularNetwork:
    @staticmethod
    def serial_connection(*args: float) -> float:
        """Calculate serial resistance of vessels."""
        return sum(args)

    @staticmethod
    def parallel_connection(*args: float) -> float:
        """Calculate parallel resistance of vessels."""
        G = 0.0
        for R in args:
            G += 1 / R
        return 1 / G

    @staticmethod
    def calculate_basic_network(arteolies: list, branches: list, aorta: "Vessel"):
        """Calculates the hydrodynamic resistance of the basic system: two identical parallel arteries connected to two
        identical parallel branches connected to the aorta."""
        R_arteolie1 = arteolies[0] | arteolies[1]
        R_arteolie2 = arteolies[2] | arteolies[3]
        R_branch1 = branches[0] + R_arteolie1
        R_branch2 = branches[1] + R_arteolie2
        return aorta + (VascularNetwork.parallel_connection(R_branch1, R_branch2))
