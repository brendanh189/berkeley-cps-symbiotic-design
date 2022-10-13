import igraph
from sym_cps.representation.design.concrete import DConcrete
from sym_cps.representation.design.topology import DTopology
from sym_cps.shared.paths import ExportType, designs_folder
from sym_cps.tools.io import save_to_file



def generate_designs_info_files(designs: dict[str, tuple[DConcrete, DTopology]], design_name: str):
    d_concrete, d_topology = designs[design_name]
    d_concrete.export(ExportType.JSON)
    d_concrete.export(ExportType.PDF)
    d_concrete.export(ExportType.DOT)
    d_topology.export(ExportType.DOT)
    d_topology.export(ExportType.PDF)
    d_concrete.export(ExportType.TOPOLOGY)
