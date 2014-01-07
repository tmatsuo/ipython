"""IntRangeWidget class.  

Represents a bounded int using a widget.
"""
#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
from .widget import DOMWidget
from IPython.utils.traitlets import Unicode, Int, Bool, List

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------
class IntRangeWidget(DOMWidget):
    target_name = Unicode('IntRangeWidgetModel')
    default_view_name = Unicode('IntSliderView')

    # Keys
    keys = ['value', 'step', 'max', 'min', 'disabled', 'orientation', 'description'] + DOMWidget.keys
    value = Int(0, help="Int value") 
    max = Int(100, help="Max value")
    min = Int(0, help="Min value")
    disabled = Bool(False, help="Enable or disable user changes")
    step = Int(1, help="Minimum step that the value can take (ignored by some views)")
    orientation = Unicode(u'horizontal', help="Vertical or horizontal (ignored by some views)")
    description = Unicode(help="Description of the value this widget represents")
