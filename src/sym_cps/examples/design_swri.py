"""Generate design swri files for all designs in the library"""


from sym_cps.optimizers.concrete_opt import ConcreteOptimizer, ConcreteStrategy
from sym_cps.optimizers.params_opt import ParametersOptimizer
from sym_cps.optimizers.topo_opt import TopologyOptimizer, TopologyStrategy
from sym_cps.representation.design.concrete import DConcrete
from sym_cps.representation.design.topology import DTopology
from sym_cps.representation.tools.parsers.parse import parse_library_and_seed_designs
from sym_cps.representation.tools.parsers.parsing_designs import parse_design_from_design_swri
from sym_cps.shared.paths import output_folder, ExportType

"""Loading Library and Seed Designs"""
c_library, designs = parse_library_and_seed_designs()

def generate_design_swri(design_name: str | None = None):
    if design_name is None:
        for _, design in designs.items():
            design_concrete = design[0]
            design_concrete.export(ExportType.JSON)
    else:
            design_concrete = designs[design_name][0]
            design_concrete.export(ExportType.JSON)        



if __name__ == '__main__':
    generate_design_swri()
