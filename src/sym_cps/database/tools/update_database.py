from sym_cps.shared.designs import designs
from sym_cps.shared.library import c_library
from sym_cps.tools.update_library import update_dat_files_and_export


def update_library_to_db():
    for library_component in c_library.components:
        """TODO IMPLEMENT"""
        pass

    for component_type in c_library.component_types:
        """TODO IMPLEMENT"""
        pass


def update_designs_to_db():
    for design in designs:
        pass



if __name__ == "__main__":
    update_dat_files_and_export()
    update_library_to_db()
    update_designs_to_db()