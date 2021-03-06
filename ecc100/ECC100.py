#!/usr/bin/env python
# -*- coding:utf-8 -*-


# ############################################################################
#  license :
# ============================================================================
#
#  File :        ECC100.py
#
#  Project :     dev-maxiv-ecc100
#
# This file is part of Tango device class.
# 
# Tango is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tango is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tango.  If not, see <http://www.gnu.org/licenses/>.
# 
#
#  $Author :      mikel.eguiraun$
#
#  $Revision :    $
#
#  $Date :        $
#
#  $HeadUrl :     $
# ============================================================================
#            This file is generated by POGO
#     (Program Obviously used to Generate tango Object)
# ############################################################################

__all__ = ["ECC100", "ECC100Class", "main"]

__docformat__ = 'restructuredtext'

import PyTango
import sys
# Add additional import
#----- PROTECTED REGION ID(ECC100.additionnal_import) ENABLED START -----#
import libecc100.libECC100
#----- PROTECTED REGION END -----#	//	ECC100.additionnal_import

# Device States Description
# No states for this device


class ECC100 (PyTango.Device_4Impl):
    """Device server for the Attocube ECC100 motion controller"""
    
    # -------- Add you global variables here --------------------------
    #----- PROTECTED REGION ID(ECC100.global_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	ECC100.global_variables

    def __init__(self, cl, name):
        PyTango.Device_4Impl.__init__(self,cl,name)
        self.debug_stream("In __init__()")
        ECC100.init_device(self)
        #----- PROTECTED REGION ID(ECC100.__init__) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	ECC100.__init__
        
    def delete_device(self):
        self.debug_stream("In delete_device()")
        #----- PROTECTED REGION ID(ECC100.delete_device) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	ECC100.delete_device

    def init_device(self):
        self.debug_stream("In init_device()")
        self.get_device_properties(self.get_device_class())
        self.attr_PositionAxis0_read = 0.0
        self.attr_PositionAxis1_read = 0.0
        self.attr_PositionAxis2_read = 0.0
        self.attr_Axis0Connected_read = False
        self.attr_Axis1Connected_read = False
        self.attr_Axis2Connected_read = False
        self.attr_Axis0ReferencePosition_read = 0.0
        self.attr_Axis1ReferencePosition_read = 0.0
        self.attr_Axis2ReferencePosition_read = 0.0
        self.attr_MovementDelay_read = 1.0
        self.attr_Axis0ReferencePositionValid_read = False
        self.attr_Axis1ReferencePositionValid_read = False
        self.attr_Axis2ReferencePositionValid_read = False
        #----- PROTECTED REGION ID(ECC100.init_device) ENABLED START -----#
        try:
            self.ecc100 = libecc100.libECC100.ECC100(self.Host)
            self.set_state(PyTango.DevState.ON)
        except:
            self.set_state(PyTango.DevState.FAULT)
        #----- PROTECTED REGION END -----#	//	ECC100.init_device

    def always_executed_hook(self):
        self.debug_stream("In always_excuted_hook()")
        #----- PROTECTED REGION ID(ECC100.always_executed_hook) ENABLED START -----#

        #----- PROTECTED REGION END -----#	//	ECC100.always_executed_hook

    # -------------------------------------------------------------------------
    #    ECC100 read/write attribute methods
    # -------------------------------------------------------------------------
    
    def read_PositionAxis0(self, attr):
        self.debug_stream("In read_PositionAxis0()")
        #----- PROTECTED REGION ID(ECC100.PositionAxis0_read) ENABLED START -----#
        self.attr_PositionAxis0_read = self.ecc100.get_position(0) / 1e6
        attr.set_value(self.attr_PositionAxis0_read)
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis0_read
        
    def write_PositionAxis0(self, attr):
        self.debug_stream("In write_PositionAxis0()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(ECC100.PositionAxis0_write) ENABLED START -----#
        self.ecc100.enable_movement(0)
        self.ecc100.set_position(0, int(data * 1e6))
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis0_write
        
    def read_PositionAxis1(self, attr):
        self.debug_stream("In read_PositionAxis1()")
        #----- PROTECTED REGION ID(ECC100.PositionAxis1_read) ENABLED START -----#
        self.attr_PositionAxis1_read = self.ecc100.get_position(1) / 1e6
        attr.set_value(self.attr_PositionAxis1_read)
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis1_read
        
    def write_PositionAxis1(self, attr):
        self.debug_stream("In write_PositionAxis1()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(ECC100.PositionAxis1_write) ENABLED START -----#
        self.ecc100.enable_movement(1)
        self.ecc100.set_position(1, int(data * 1e6))
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis1_write
        
    def read_PositionAxis2(self, attr):
        self.debug_stream("In read_PositionAxis2()")
        #----- PROTECTED REGION ID(ECC100.PositionAxis2_read) ENABLED START -----#
        self.attr_PositionAxis2_read = self.ecc100.get_position(2) / 1e6
        attr.set_value(self.attr_PositionAxis2_read)
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis2_read
        
    def write_PositionAxis2(self, attr):
        self.debug_stream("In write_PositionAxis2()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(ECC100.PositionAxis2_write) ENABLED START -----#
        self.ecc100.enable_movement(2)
        self.ecc100.set_position(2, int(data * 1e6))
        #----- PROTECTED REGION END -----#	//	ECC100.PositionAxis2_write
        
    def read_Axis0Connected(self, attr):
        self.debug_stream("In read_Axis0Connected()")
        #----- PROTECTED REGION ID(ECC100.Axis0Connected_read) ENABLED START -----#
        try:
            self.attr_Axis0Connected_read = self.ecc100.axis_connected(0)
            attr.set_value(self.attr_Axis0Connected_read)
        except:
            self.ecc100.restart()
        #----- PROTECTED REGION END -----#	//	ECC100.Axis0Connected_read
        
    def read_Axis1Connected(self, attr):
        self.debug_stream("In read_Axis1Connected()")
        #----- PROTECTED REGION ID(ECC100.Axis1Connected_read) ENABLED START -----#
        self.attr_Axis1Connected_read = self.ecc100.axis_connected(1)
        attr.set_value(self.attr_Axis1Connected_read)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis1Connected_read
        
    def read_Axis2Connected(self, attr):
        self.debug_stream("In read_Axis2Connected()")
        #----- PROTECTED REGION ID(ECC100.Axis2Connected_read) ENABLED START -----#
        self.attr_Axis2Connected_read = self.ecc100.axis_connected(2)
        attr.set_value(self.attr_Axis2Connected_read)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis2Connected_read
        
    def read_Axis0ReferencePosition(self, attr):
        self.debug_stream("In read_Axis0ReferencePosition()")
        #----- PROTECTED REGION ID(ECC100.Axis0ReferencePosition_read) ENABLED START -----#
        if self.attr_Axis0Connected_read & self.attr_Axis0ReferencePositionValid_read:
            self.attr_Axis0ReferencePosition_read = self.ecc100.get_reference_position(0) / 1e6
            attr.set_value(self.attr_Axis0ReferencePosition_read)
        else:
            attr.set_value(0)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis0ReferencePosition_read
        
    def read_Axis1ReferencePosition(self, attr):
        self.debug_stream("In read_Axis1ReferencePosition()")
        #----- PROTECTED REGION ID(ECC100.Axis1ReferencePosition_read) ENABLED START -----#
        if self.attr_Axis1Connected_read & self.attr_Axis1ReferencePositionValid_read:
            self.attr_Axis1ReferencePosition_read = self.ecc100.get_reference_position(1) / 1e6
            attr.set_value(self.attr_Axis1ReferencePosition_read)
        else:
            attr.set_value(0)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis1ReferencePosition_read
        
    def read_Axis2ReferencePosition(self, attr):
        self.debug_stream("In read_Axis2ReferencePosition()")
        #----- PROTECTED REGION ID(ECC100.Axis2ReferencePosition_read) ENABLED START -----#
        if self.attr_Axis2Connected_read & self.attr_Axis2ReferencePositionValid_read:
            self.attr_Axis2ReferencePosition_read = self.ecc100.get_reference_position(2) / 1e6
            attr.set_value(self.attr_Axis2ReferencePosition_read)
        else:
            attr.set_value(0)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis2ReferencePosition_read
        
    def read_MovementDelay(self, attr):
        self.debug_stream("In read_MovementDelay()")
        #----- PROTECTED REGION ID(ECC100.MovementDelay_read) ENABLED START -----#
        attr.set_value(self.attr_MovementDelay_read)
        
        #----- PROTECTED REGION END -----#	//	ECC100.MovementDelay_read
        
    def write_MovementDelay(self, attr):
        self.debug_stream("In write_MovementDelay()")
        data = attr.get_write_value()
        #----- PROTECTED REGION ID(ECC100.MovementDelay_write) ENABLED START -----#
        self.attr_MovementDelay_read = data
        #----- PROTECTED REGION END -----#	//	ECC100.MovementDelay_write
        
    def read_Axis0ReferencePositionValid(self, attr):
        self.debug_stream("In read_Axis0ReferencePositionValid()")
        #----- PROTECTED REGION ID(ECC100.Axis0ReferencePositionValid_read) ENABLED START -----#
        if self.attr_Axis0Connected_read:
            self.attr_Axis0ReferencePositionValid_read = bool(self.ecc100.get_reference_position_valid(0))
            attr.set_value(self.attr_Axis0ReferencePositionValid_read)
        else:
            attr.set_value(False)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis0ReferencePositionValid_read
        
    def read_Axis1ReferencePositionValid(self, attr):
        self.debug_stream("In read_Axis1ReferencePositionValid()")
        #----- PROTECTED REGION ID(ECC100.Axis1ReferencePositionValid_read) ENABLED START -----#
        if self.attr_Axis1Connected_read:
            self.attr_Axis1ReferencePositionValid_read = bool(self.ecc100.get_reference_position_valid(1))
            attr.set_value(self.attr_Axis1ReferencePositionValid_read)
        else:
            attr.set_value(False)  
        #----- PROTECTED REGION END -----#	//	ECC100.Axis1ReferencePositionValid_read
        
    def read_Axis2ReferencePositionValid(self, attr):
        self.debug_stream("In read_Axis2ReferencePositionValid()")
        #----- PROTECTED REGION ID(ECC100.Axis2ReferencePositionValid_read) ENABLED START -----#
        if self.attr_Axis2Connected_read:
            self.attr_Axis2ReferencePositionValid_read = bool(self.ecc100.get_reference_position_valid(2))
            attr.set_value(self.attr_Axis2ReferencePositionValid_read)
        else:
            attr.set_value(False)
        #----- PROTECTED REGION END -----#	//	ECC100.Axis2ReferencePositionValid_read
        
    
    
            
    def read_attr_hardware(self, data):
        self.debug_stream("In read_attr_hardware()")
        #----- PROTECTED REGION ID(ECC100.read_attr_hardware) ENABLED START -----#
        
        #----- PROTECTED REGION END -----#	//	ECC100.read_attr_hardware


    # -------------------------------------------------------------------------
    #    ECC100 command methods
    # -------------------------------------------------------------------------
    
    def ResetPosition(self, argin):
        """ 
        :param argin: 
        :type argin: PyTango.DevULong
        """
        self.debug_stream("In ResetPosition()")
        #----- PROTECTED REGION ID(ECC100.ResetPosition) ENABLED START -----#
        self.ecc100.reset_position(argin)
        #----- PROTECTED REGION END -----#	//	ECC100.ResetPosition
        
    def TimedContinousForward(self, argin):
        """ 
        :param argin: axis
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In TimedContinousForward()")
        #----- PROTECTED REGION ID(ECC100.TimedContinousForward) ENABLED START -----#
        self.ecc100.timed_continous_forward(argin, self.attr_MovementDelay_read)
        #----- PROTECTED REGION END -----#	//	ECC100.TimedContinousForward
        
    def TimedContinousBackward(self, argin):
        """ 
        :param argin: axis,delay
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In TimedContinousBackward()")
        #----- PROTECTED REGION ID(ECC100.TimedContinousBackward) ENABLED START -----#
        self.ecc100.timed_continous_backward(argin, self.attr_MovementDelay_read)
        #----- PROTECTED REGION END -----#	//	ECC100.TimedContinousBackward
        
    def EnableMovement(self, argin):
        """ 
        :param argin: axis
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In EnableMovement()")
        #----- PROTECTED REGION ID(ECC100.EnableMovement) ENABLED START -----#
        self.ecc100.enable_movement(argin)
        #----- PROTECTED REGION END -----#	//	ECC100.EnableMovement
        
    def DisableMovement(self, argin):
        """ 
        :param argin: axis
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In DisableMovement()")
        #----- PROTECTED REGION ID(ECC100.DisableMovement) ENABLED START -----#
        self.ecc100.disable_movement(argin)
        #----- PROTECTED REGION END -----#	//	ECC100.DisableMovement
        
    def EnableOutputRelay(self, argin):
        """ 
        :param argin: axis
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In EnableOutputRelay()")
        #----- PROTECTED REGION ID(ECC100.EnableOutputRelay) ENABLED START -----#
        self.ecc100.enable_output_relay(argin)
        #----- PROTECTED REGION END -----#	//	ECC100.EnableOutputRelay
        
    def DisableOutputRelay(self, argin):
        """ 
        :param argin: axis
        :type argin: PyTango.DevLong
        """
        self.debug_stream("In DisableOutputRelay()")
        #----- PROTECTED REGION ID(ECC100.DisableOutputRelay) ENABLED START -----#
        self.ecc100.disable_output_relay(argin)
        #----- PROTECTED REGION END -----#	//	ECC100.DisableOutputRelay
        

    #----- PROTECTED REGION ID(ECC100.programmer_methods) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	ECC100.programmer_methods

class ECC100Class(PyTango.DeviceClass):
    # -------- Add you global class variables here --------------------------
    #----- PROTECTED REGION ID(ECC100.global_class_variables) ENABLED START -----#
    
    #----- PROTECTED REGION END -----#	//	ECC100.global_class_variables


    #    Class Properties
    class_property_list = {
        }


    #    Device Properties
    device_property_list = {
        'Host':
            [PyTango.DevString, 
             '',
            [] ],
        }


    #    Command definitions
    cmd_list = {
        'ResetPosition':
            [[PyTango.DevULong, "none"],
            [PyTango.DevVoid, "none"]],
        'TimedContinousForward':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        'TimedContinousBackward':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        'EnableMovement':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        'DisableMovement':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        'EnableOutputRelay':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        'DisableOutputRelay':
            [[PyTango.DevLong, "axis"],
            [PyTango.DevVoid, "none"]],
        }


    #    Attribute definitions
    attr_list = {
        'PositionAxis0':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'PositionAxis1':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'PositionAxis2':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'Axis0Connected':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        'Axis1Connected':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        'Axis2Connected':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        'Axis0ReferencePosition':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'Axis1ReferencePosition':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'Axis2ReferencePosition':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ],
            {
                'unit': "um",
                'format': "%6.6f",
            } ],
        'MovementDelay':
            [[PyTango.DevDouble,
            PyTango.SCALAR,
            PyTango.READ_WRITE]],
        'Axis0ReferencePositionValid':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        'Axis1ReferencePositionValid':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        'Axis2ReferencePositionValid':
            [[PyTango.DevBoolean,
            PyTango.SCALAR,
            PyTango.READ]],
        }


def main():
    try:
        py = PyTango.Util(sys.argv)
        py.add_class(ECC100Class, ECC100, 'ECC100')
        #----- PROTECTED REGION ID(ECC100.add_classes) ENABLED START -----#
        #----- PROTECTED REGION END -----#	//	ECC100.add_classes

        U = PyTango.Util.instance()
        U.server_init()
        U.server_run()

    except PyTango.DevFailed as e:
        print ('-------> Received a DevFailed exception:', e)
    except Exception as e:
        print ('-------> An unforeseen exception occured....', e)

if __name__ == '__main__':
    main()
