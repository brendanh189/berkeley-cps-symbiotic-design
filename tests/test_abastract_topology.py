from sym_cps.grammar.topology import AbstractTopology
from sym_cps.representation.design.concrete import DConcrete
from sym_cps.shared.designs import designs
from sym_cps.shared.objects import ExportType


def asset_topology(topology_level: ExportType):
    """Test of AbstractTopology at the level of abstraction 1 (lowest)"""
    # Loading DConcrete Object
    test_quad_original = designs["TestQuad"][0]

    # Exporting AbstractTopology to file
    topology_json_path = test_quad_original.export(topology_level)

    # Loading AbstractTopology from file
    abstract_topology = AbstractTopology.from_json(topology_json_path)

    # Creating DConcrete Object
    test_quad_loaded = DConcrete.from_abstract_topology(abstract_topology)

    assert test_quad_original == test_quad_loaded


levels = [ExportType.TOPOLOGY_1, ExportType.TOPOLOGY_2, ExportType.TOPOLOGY_3]


def test_topology_abstraction_1():
    asset_topology(ExportType.TOPOLOGY_1)


def test_topology_abstraction_2():
    asset_topology(ExportType.TOPOLOGY_2)

def test_topology_abstraction_3():
    asset_topology(ExportType.TOPOLOGY_3)
