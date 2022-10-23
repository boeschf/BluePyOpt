try:
    import arbor
except ImportError as e:
    class arbor:
        def __getattribute__(self, _):
            raise ImportError("Exporting cell models to ACC/JSON, loading"
                              " them or optimizing them with the Arbor"
                              " simulator requires missing dependency arbor."
                              " To install BluePyOpt with arbor,"
                              " run 'pip install bluepyopt[arbor]'.")


class ArbLabel:
    """Arbor label"""

    def __init__(self, type, name, defn):
        self._type = type
        self._name = name
        self._defn = defn

    @property
    def defn(self):
        """Label definition for label-dict"""
        return '(%s-def "%s" %s)' % (self._type, self._name, self._defn)

    @property
    def ref(self):
        """Reference to label defined in label-dict"""
        return '(%s "%s")' % (self._type, self._name)

    @property
    def name(self):
        """Name of the label"""
        return self._name

    @property
    def loc(self):
        """Expression defining the location of the label"""
        return self._defn

    def __eq__(self, other):
        return self.defn == other.defn

    def __hash__(self):
        return hash(self.defn)