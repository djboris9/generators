# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Dust Detector Bricklet communication config

from commonconstants import THRESHOLD_OPTION_CONSTANTS

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 260,
    'name': 'Dust Detector',
    'display_name': 'Dust Detector',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Measures dust density',
        'de': 'Misst Staubdichte'
    },
    'released': True,
    'documented': True,
    'discontinued': False,
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Get Dust Density',
'elements': [('Dust Density', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the dust density in µg/m³.

If you want to get the dust density periodically, it is recommended
to use the :cb:`Dust Density` callback and set the period with
:func:`Set Dust Density Callback Period`.
""",
'de':
"""
Gibt die Staubdichte in µg/m³ zurück.

Wenn die Staubdichte periodisch abgefragt werden soll, wird empfohlen
den :cb:`Dust Density` Callback zu nutzen und die Periode mit
:func:`Set Dust Density Callback Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Dust Density Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :cb:`Dust Density` callback is triggered
periodically. A value of 0 turns the callback off.

The :cb:`Dust Density` callback is only triggered if the dust density has
changed since the last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :cb:`Dust Density` Callback ausgelöst
wird. Ein Wert von 0 deaktiviert den Callback.

Der :cb:`Dust Density` Callback wird nur ausgelöst wenn sich die Staubdichte
seit der letzten Auslösung geändert hat.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Dust Density Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Dust Density Callback Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Dust Density Callback Period`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Dust Density Callback Threshold',
'elements': [('Option', 'char', 1, 'in', THRESHOLD_OPTION_CONSTANTS),
             ('Min', 'uint16', 1, 'in'),
             ('Max', 'uint16', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the thresholds for the :cb:`Dust Density Reached` callback.

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'",    "Callback is turned off"
 "'o'",    "Callback is triggered when the dust density value is *outside* the min and max values"
 "'i'",    "Callback is triggered when the dust density value is *inside* the min and max values"
 "'<'",    "Callback is triggered when the dust density value is smaller than the min value (max is ignored)"
 "'>'",    "Callback is triggered when the dust density value is greater than the min value (max is ignored)"

The default value is ('x', 0, 0).
""",
'de':
"""
Setzt den Schwellwert für den :cb:`Dust Density Reached` Callback.

Die folgenden Optionen sind möglich:

.. csv-table::
 :header: "Option", "Beschreibung"
 :widths: 10, 100

 "'x'",    "Callback ist inaktiv"
 "'o'",    "Callback wird ausgelöst wenn die Staubdichte *außerhalb* des min und max Wertes ist"
 "'i'",    "Callback wird ausgelöst wenn der Staubdichte *innerhalb* des min und max Wertes ist"
 "'<'",    "Callback wird ausgelöst wenn der Staubdichte kleiner als der min Wert ist (max wird ignoriert)"
 "'>'",    "Callback wird ausgelöst wenn der Staubdichte größer als der min Wert ist (max wird ignoriert)"

Der Standardwert ist ('x', 0, 0).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Dust Density Callback Threshold',
'elements': [('Option', 'char', 1, 'out', THRESHOLD_OPTION_CONSTANTS),
             ('Min', 'uint16', 1, 'out'),
             ('Max', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the threshold as set by :func:`Set Dust Density Callback Threshold`.
""",
'de':
"""
Gibt den Schwellwert zurück, wie von :func:`Set Dust Density Callback Threshold`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the threshold callback

* :cb:`Dust Density Reached`

is triggered, if the threshold

* :func:`Set Dust Density Callback Threshold`

keeps being reached.

The default value is 100.
""",
'de':
"""
Setzt die Periode in ms mit welcher die Schwellwert Callback

* :cb:`Dust Density Reached`

ausgelöst wird, wenn der Schwellwert

* :func:`Set Dust Density Callback Threshold`

weiterhin erreicht bleibt.

Der Standardwert ist 100.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the debounce period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Gibt die Entprellperiode zurück, wie von :func:`Set Debounce Period`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Dust Density',
'elements': [('Dust Density', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Dust Density Callback Period`. The :word:`parameter` is the
dust density of the sensor.

Der :cb:`Dust Density` callback is only triggered if the dust density value has
changed since the last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set Dust Density Callback Period`,
ausgelöst. Der :word:`parameter` ist die Staubdichte des Sensors.

Der :cb:`Dust Density` Callback wird nur ausgelöst wenn sich die Staubdichte
seit der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Dust Density Reached',
'elements': [('Dust Density', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered when the threshold as set by
:func:`Set Dust Density Callback Threshold` is reached.
The :word:`parameter` is the dust density of the sensor.

If the threshold keeps being reached, the callback is triggered periodically
with the period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Dieser Callback wird ausgelöst wenn der Schwellwert, wie von
:func:`Set Dust Density Callback Threshold` gesetzt, erreicht wird.
Der :word:`parameter` ist die Staubdichte des Sensors.

Wenn der Schwellwert erreicht bleibt, wird der Callback mit der Periode, wie
mit :func:`Set Debounce Period` gesetzt, ausgelöst.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Moving Average',
'elements': [('Average', 'uint8', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the length of a `moving averaging <https://en.wikipedia.org/wiki/Moving_average>`__
for the dust_density.

Setting the length to 0 will turn the averaging completely off. With less
averaging, there is more noise on the data.

The range for the averaging is 0-100.

The default value is 100.
""",
'de':
"""
Setzt die Länge eines gleitenden Mittelwerts für die Staubdichte.

Wenn die Länge auf 0 gesetzt wird, ist das Averaging komplett aus. Desto kleiner
die Länge des Mittelwerts ist, desto mehr Rauschen ist auf den Daten.

Der Wertebereich liegt bei 0-100.

Der Standardwert ist 100.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Moving Average',
'elements': [('Average', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the length moving average as set by :func:`Set Moving Average`.
""",
'de':
"""
Gibt die Länge des gleitenden Mittelwerts zurück, wie von
:func:`Set Moving Average` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Dust Density', 'dust density'), [(('Dust Density', 'Dust Density'), 'uint16', 1, None, 'µg/m³', None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Dust Density', 'dust density'), [(('Dust Density', 'Dust Density'), 'uint16', 1, None, 'µg/m³', None)], None, None),
              ('callback_period', ('Dust Density', 'dust density'), [], 1000)]
})

com['examples'].append({
'name': 'Threshold',
'functions': [('debounce_period', 10000),
              ('callback', ('Dust Density Reached', 'dust density reached'), [(('Dust Density', 'Dust Density'), 'uint16', 1, None, 'µg/m³', None)], None, None),
              ('callback_threshold', ('Dust Density', 'dust density'), [], '>', [(10, 0)])]
})
