from __future__ import print_function
from serial import Serial
from serial import SerialException
from serial import SerialTimeoutException


class ModemcmdTimeoutException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ModemcmdException(Exception):
    def __init__(self, msg):
        self.msg = msg


def modemcmd(port='/dev/ttyACM0', baudrate=115200, rts_cts=False, cmd='', timeout=0, *waitrsps):
    if (timeout == 0):
        timeout = 30

    try:
        serial = Serial(port, baudrate, 
                        timeout=float(timeout), rtscts=rts_cts)
    except SerialException as e:
        raise ModemcmdException(e)

    if (len(cmd)):
        cmd = cmd + '\r'
        try:
            serial.write(cmd.encode('utf-8'))
        except SerialTimeoutException:
            raise ModemcmdTimeoutException('Write timeout')

    lines = b''
    rsps=[]
    if waitrsps is not None:
        for rsp in waitrsps:
            rsps.append(rsp.encode('utf-8'))

    waiting = True
    while waiting:
        line = serial.readline()
        lines += line
        if line == b'':  #timeout
           waiting = False
        elif len(rsps) > 0:
            for rsp in rsps:
                if rsp in line:
                    waiting = False
                    break

    return lines.decode('utf-8')
