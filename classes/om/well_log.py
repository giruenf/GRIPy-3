from collections import OrderedDict

from classes.om import OMBaseObject
from classes.om import DataObject
from classes.om import ObjectManager


class Log(DataObject):
    tid = "log"
    _TID_FRIENDLY_NAME = 'Log'
    _SHOWN_ATTRIBUTES = [('datatype', 'Curve Type'),
                         ('unit', 'Units'),
                         ('min', 'Min Value'),
                         ('max', 'Max Value')
    ]
    
    def __init__(self, *args, **attributes):
        super().__init__(*args, **attributes) 
     
    @classmethod
    def _is_tree_tid_node_needed(cls):
        #From matplotlib.docstring.py 
        #@_autogen_docstring(Axes.plot)
        #@_autogen_docstring(OMBaseObject._is_tree_tid_node_needed)
        __doc__ = OMBaseObject._is_tree_tid_node_needed.__doc__
        return False
#    _is_tree_tid_node_needed.__doc__ = OMBaseObject._is_tree_tid_node_needed.__doc__
    
    
    # https://docs.scipy.org/doc/numpy-1.15.0/docs/howto_document.html
    
    # TODO: Usar Sphinx, como modelo abaixo do MPL - confirmar visitando respectiva pagina do MPL
    # neste caso eh a pagina Artist.set_clip_path do docs online.
    

    def _get_max_dimensions(self):
        return 1
    
    def get_friendly_name(self):
        """
        Metodo duplicado em Log e DataIndex
        """
        OM = ObjectManager()
        parent_well_uid = OM._getparentuid(self.uid)
        parent_well = OM.get(parent_well_uid)         
        return self.name + '@' + parent_well.name

    def get_curve_set(self):
        """
        Metodo de conveniencia.
        
        Se o objeto possui curve_set, o retorna. Senão retorna None.
        
        Metodo duplicado em DataIndex e Log.
        """
        OM = ObjectManager()
        curve_set_uid = OM._getparentuid(self.uid)
        return OM.get(curve_set_uid)
     
    def _get_pg_properties_dict(self):
        """
        """
        props = OrderedDict()
        props['datatype'] = {
            'type': str,
            'label': 'Datatype',
            'enabled': False
        }    
        props['unit'] = {
            'type': str,
            'label': 'Unit',
            'enabled': False
        }
        props['min'] = {
            'type': str,
            'label': 'Min Value',
            'enabled': False
        }    
        props['max'] = {
            'type': str,
            'label': 'Max Value',
            'enabled': False
        }        
        return props


    
    """
    Set the artist's clip path, which may be:

    - a :class:`~matplotlib.patches.Patch` (or subclass) instance; or
    - a :class:`~matplotlib.path.Path` instance, in which case a
      :class:`~matplotlib.transforms.Transform` instance, which will be
      applied to the path before using it for clipping, must be provided;
      or
    - ``None``, to remove a previously set clipping path.

    For efficiency, if the path happens to be an axis-aligned rectangle,
    this method will set the clipping box to the corresponding rectangle
    and set the clipping path to ``None``.

    ACCEPTS: [(`~matplotlib.path.Path`, `.Transform`) | `.Patch` | None]
        """    
    
    
    '''
    #From matplotlib.axes._base.py line 3152
    
    get_xscale.__doc__ = "Return the xaxis scale string: %s""" % (
    ", ".join(mscale.get_scale_names()))
    
    Written after function
    
    '''
    
    '''
    #From matplotlib.pyplot.py 
    
    def _autogen_docstring(base):
    """Autogenerated wrappers will get their docstring from a base function
    with an addendum."""
    #msg = "\n\nAdditional kwargs: hold = [True|False] overrides default hold state"
    msg = ''
    addendum = docstring.Appender(msg, '\n\n')
    return lambda func: addendum(docstring.copy_dedent(base)(func))
    '''