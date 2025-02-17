from abc import ABC, abstractmethod 
import numpy.typing as npt

class ProblemBase(ABC):
    """The base class for the Optimization Problem
    _bounds:  list[Tuple[float, float]]the bound (box constraints) for the design problem.
    The first element of the tuple is the lower bound and the other element is the upper bound
    For example, [(1,5), (2,4)] can be used to represent the box constraints $1 < x < 5, 2 < y < 4$.
    _opt_array: the numpy array that are used as initial value.
    """
    def __init__(self):
        self._bounds: list[tuple[float, float]] = None
        self._opt_array: npt.ArrayLike = None 
        self._obj_dim = 0
        self._con_dim = 0

    @property
    def dim(self):
        """Number of optimization variables"""
        return len(self._bounds)

    @property
    def obj_dim(self):
        return self._obj_dim

    def set_obj_dim(self, dim: int):
        self._obj_dim = dim

    @property
    def opt_array(self) -> npt.ArrayLike:
        return self._opt_array

    @property
    def con_dim(self):
        return self._con_dim

    def set_con_dim(self, dim: int):
        self._con_dim = dim

    @abstractmethod
    def obj_dominate(self, obj1: npt.ArrayLike, obj2: npt.ArrayLike):
        pass

    @property
    def bounds(self):
        """The bounds of the optimization problem"""
        return self._bounds


    @abstractmethod
    def evaluate(self, parameters: npt.ArrayLike) -> tuple[list[float], list[bool]]:
        """return the objective function or invalid parameters"""
        pass

    @abstractmethod
    def set_parameters(self, parameters: npt.ArrayLike) -> None:
        pass
    