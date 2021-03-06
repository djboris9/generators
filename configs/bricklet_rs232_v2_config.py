# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# RS232 Bricklet 2.0 communication config

com = {
    'author': 'Ishraq Ibne Ashraf <ishraq@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 2108,
    'name': 'RS232 V2',
    'display_name': 'RS232 2.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Communicates with RS232 devices',
        'de': 'Kommuniziert mit RS232 Geräten'
    },
    'comcu': True,
    'released': False,
    'documented': False,
    'discontinued': False,
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Write Low Level',
'elements': [('Message Length', 'uint16', 1, 'in'),
             ('Message Chunk Offset', 'uint16', 1, 'in'),
             ('Message Chunk Data', 'char', 60, 'in'),
             ('Message Chunk Written', 'uint8', 1, 'out')],
'high_level': {'stream_in': {'name': 'Message', 'short_write': True}},
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Writes characters to the RS232 interface. The characters can be binary data,
ASCII or similar is not necessary.

The return value is the number of characters that were written.

See :func:`Set Configuration` for configuration possibilities
regarding baudrate, parity and so on.
""",
'de':
"""
Schreibt Zeichen auf die RS232-Schnittstelle. Die Zeichen können Binärdaten
sein, ASCII o.ä. ist nicht notwendig.

Der Rückgabewert ist die Anzahl der Zeichen die geschrieben wurden.

Siehe :func:`Set Configuration` für Konfigurationsmöglichkeiten
bezüglich Baudrate, Parität usw.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Read Low Level',
'elements': [('Length', 'uint16', 1, 'in'),
             ('Message Length', 'uint16', 1, 'out'),
             ('Message Chunk Offset', 'uint16', 1, 'out'),
             ('Message Chunk Data', 'char', 60, 'out')],
'high_level': {'stream_out': {'name': 'Message'}},
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns up to *length* characters from receive buffer.

Instead of polling with this function, you can also use
callbacks. But note that this function will return available
data only when the read callback is disabled.
See :func:`Enable Read Callback` and :cb:`Read` callback.
""",
'de':
"""
Gibt bis zu *length* Zeichen aus dem Empfangsbuffer zurück.

Anstatt mit dieser Funktion zu pollen, ist es auch möglich
Callbacks zu nutzen. Diese Funktion gibt nur Daten zurück wenn
der Read-Callback nich aktiv ist.
Siehe :func:`Enable Read Callback` und :cb:`Read` Callback.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Enable Read Callback',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Enables the :cb:`Read` callback.

By default the callback is disabled.
""",
'de':
"""
Aktiviert den :cb:`Read` Callback.

Im Startzustand ist der Callback deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Disable Read Callback',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Disables the :cb:`Read` callback.

By default the callback is disabled.
""",
'de':
"""
Deaktiviert den :cb:`Read` Callback.

Im Startzustand ist der Callback deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Is Read Callback Enabled',
'elements': [('Enabled', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns *true* if the :cb:`Read` callback is enabled,
*false* otherwise.
""",
'de':
"""
Gibt *true* zurück falls :cb:`Read` Callback aktiviert ist,
*false* sonst.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Configuration',
'elements': [('Baudrate', 'uint8', 1, 'in', ('Baudrate', [('300', 0),
                                                          ('600', 1),
                                                          ('1200', 2),
                                                          ('2400', 3),
                                                          ('4800', 4),
                                                          ('9600', 5),
                                                          ('14400', 6),
                                                          ('19200', 7),
                                                          ('28800', 8),
                                                          ('38400', 9),
                                                          ('57600', 10),
                                                          ('115200', 11),
                                                          ('230400', 12)])),
             ('Parity', 'uint8', 1, 'in', ('Parity', [('None', 0),
                                                      ('Odd', 1),
                                                      ('Even', 2),
                                                      ('Forced Parity 1', 3),
                                                      ('Forced Parity 0', 4)])),
             ('Stopbits', 'uint8', 1, 'in', ('Stopbits', [('1', 1),
                                                          ('2', 2)])),
             ('Wordlength', 'uint8', 1, 'in', ('Wordlength', [('5', 5),
                                                              ('6', 6),
                                                              ('7', 7),
                                                              ('8', 8)])),
             ('Hardware Flowcontrol', 'uint8', 1, 'in', ('Hardware Flowcontrol', [('Off', 0),
                                                                                  ('On', 1)])),
             ('Software Flowcontrol', 'uint8', 1, 'in', ('Software Flowcontrol', [('Off', 0),
                                                                                  ('On', 1)]))],

'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the configuration for the RS232 communication. Available options:

* Baudrate between 300 and 230400 baud.
* Parity of none, odd, even or forced parity.
* Stopbits can be 1 or 2.
* Word length of 5 to 8.
* Hard-/Software flow control can each be on or off.

The default is: 115200 baud, parity none, 1 stop bit, word length 8, hard-/software flow control off.
""",
'de':
"""
Setzt die Konfiguration für die RS232-Kommunikation.
Verfügbare Optionen sind:

* Baudrate zwischen 300 und 230400 Baud.
* Parität von None, Odd, Even und Forced Parity.
* Stop Bits von 1 oder 2.
* Wortlänge zwischen 5 und 8.
* Hard-/Software Flow Control kann je an oder aus sein.

Der Standard ist: 115200 Baud, Parität None, 1 Stop Bits, Wortlänge 8, Hard-/Software Flow Control aus.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Configuration',
'elements': [('Baudrate', 'uint8', 1, 'out', ('Baudrate', [('300', 0),
                                                           ('600', 1),
                                                           ('1200', 2),
                                                           ('2400', 3),
                                                           ('4800', 4),
                                                           ('9600', 5),
                                                           ('14400', 6),
                                                           ('19200', 7),
                                                           ('28800', 8),
                                                           ('38400', 9),
                                                           ('57600', 10),
                                                           ('115200', 11),
                                                           ('230400', 12)])),
             ('Parity', 'uint8', 1, 'out', ('Parity', [('None', 0),
                                                       ('Odd', 1),
                                                       ('Even', 2),
                                                       ('Forced Parity 1', 3),
                                                       ('Forced Parity 0', 4)])),
             ('Stopbits', 'uint8', 1, 'out', ('Stopbits', [('1', 1),
                                                           ('2', 2)])),
             ('Wordlength', 'uint8', 1, 'out', ('Wordlength', [('5', 5),
                                                               ('6', 6),
                                                               ('7', 7),
                                                               ('8', 8)])),
             ('Hardware Flowcontrol', 'uint8', 1, 'out', ('Hardware Flowcontrol', [('Off', 0),
                                                                                   ('On', 1)])),
             ('Software Flowcontrol', 'uint8', 1, 'out', ('Software Flowcontrol', [('Off', 0),
                                                                                   ('On', 1)]))],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the configuration as set by :func:`Set Configuration`.
""",
'de':
"""
Gibt die Konfiguration zurück, wie von :func:`Set Configuration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Break Condition',
'elements': [('Break Time', 'uint16', 1, 'in')],
'since_firmware': [2, 0, 2],
'doc': ['bf', {
'en':
"""
Sets a break condition (the TX output is forced to a logic 0 state).
The parameter sets the hold-time of the break condition (in ms).
""",
'de':
"""
Setzt eine Break Condition (die TX-Ausgabe wird fest of logisch 0 gezwungen).
Der Parameter setzt die Haltezeit der Break Condition (in ms).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Buffer Config',
'elements': [('Send Buffer Size', 'uint16', 1, 'in'),
             ('Receive Buffer Size', 'uint16', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the send and receive buffer size in byte. In sum there is
10240 byte (10kb) buffer available and the minimum buffer size
is 1024 byte (1kb) for both.

The current buffer content is lost if this function is called.

The send buffer holds data that is given by :func:`Write` and
can not be written yet. The receive buffer holds data that is
received through RS232 but could not yet be send to the
user, either by :func:`Read` or through :cb:`Read` callback.

The default configuration is 5120 byte (5kb) per buffer.
""",
'de':
"""
Setzt die Größe des Senden- und Empfangsbuffers. In Summe können
die Buffer eine Größe von 10240 Byte (10kb) haben, die Minimumalgröße
ist 1024 byte (1kb) für beide.

Der aktuelle Bufferinhalt geht bei einem Aufruf dieser Funktion verloren.

Der Sendenbuffer hält die Daten welche über :func:`Write` übergeben und noch
nicht geschrieben werden konnten. Der Empfangsbuffer hält Daten welche
über RS232 empfangen wurden aber noch nicht über :func:`Read` oder
:cb:`Read` Callback an ein Nutzerprogramm übertragen werden konnten.

Die Standardkonfiguration ist 5120 Byte (5kb) pro Buffer.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Buffer Config',
'elements': [('Send Buffer Size', 'uint16', 1, 'out'),
             ('Receive Buffer Size', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the buffer configuration as set by :func:`Set Buffer Config`.
""",
'de':
"""
Gibt die Buffer-Konfiguration zurück, wie von :func:`Set Buffer Config` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Buffer Status',
'elements': [('Send Buffer Used', 'uint16', 1, 'out'),
             ('Receive Buffer Used', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the currently used bytes for the send and received buffer.

See :func:`Set Buffer Config` for buffer size configuration.
""",
'de':
"""
Gibt die aktuell genutzten Bytes des Sende- und Empfangsbuffers zurück.

Siehe :func:`Set Buffer Config` zur Konfiguration der Buffergrößen.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Read Low Level',
'elements': [('Message Length', 'uint16', 1, 'out'),
             ('Message Chunk Offset', 'uint16', 1, 'out'),
             ('Message Chunk Data', 'char', 60, 'out')],
'high_level': {'stream_out': {'name': 'Message'}},
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is called if new data is available.

To enable this callback, use :func:`Enable Read Callback`.
""",
'de':
"""
Dieser Callback wird aufgerufen wenn neue Daten zur Verfügung stehen.

Dieser Callback kann durch :func:`Enable Read Callback` aktiviert werden.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Error',
'elements': [('Error', 'uint8', 1, 'out', ('Error', [('Overrun', 1),
                                                     ('Parity', 2),
                                                     ('Framing', 4)]))],
'since_firmware': [2, 0, 1],
'doc': ['c', {
'en':
"""
This callback is called if an error occurs.
Possible errors are overrun, parity or framing error.
""",
'de':
"""
Dieser Callback wird aufgerufen wenn ein Fehler auftritt.
Mögliche Fehler sind Overrun-, Parity- oder Framing-Fehler.
"""
}]
})

com['examples'].append({
'name': 'Loopback',
'description': 'For this example connect the RX and TX pin to receive the sent message',
'functions': [('callback', ('Read', 'read'), [(('Message', 'Message'), 'char', 60, None, None, None), (('Length', 'Length'), 'uint8', 1, None, None, None)], None, None), # FIXME: wrong message type
              ('setter', 'Enable Read Callback', [], 'Enable read callback', None)],
'incomplete': True # because of special logic and callback with array parameter
})
