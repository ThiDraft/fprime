# ===============================================================================
# NAME: AbstractWriter.py
#
# DESCRIPTION: Defines the writer interface for all code generation.
#
# AUTHOR: Jordan Ishii
# EMAIL:  jordan.ishii@jpl.nasa.gov
# DATE CREATED  : Feb. 5 2013
#
# Copyright 2013, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
# ===============================================================================
#
# Python standard modules
#
import logging

#
# Python extension modules and custom interfaces
#

#
# Universal globals used within module go here.
# (DO NOT USE MANY!)
#
# Global logger init. below.
PRINT = logging.getLogger("output")
DEBUG = logging.getLogger("debug")

# Abstract base class definition
class AbstractWriter:

    __generate_empty_file = False

    """
    Defines the writer public methods.
    """

    def __init__(self):

        self.__generate_empty_file = False

    def setGenerateEmptyFile(self):
        """
        This method is used to set a flag indicating that an empty file
        should be generated. This is just a flag. It is up to the derived
        class to ensure an empty file is generated for the code snippet
        producers.
        """
        self.__generate_empty_file = True

    def generateEmptyFile(self):
        """
        Return flag indicating if a file should be created.
        """
        return self.__generate_empty_file

    @staticmethod
    def write(obj):
        """
        Defined to call all other write methods at once
        @params args: the instance of the concrete element to operate on.
        """
        raise Exception(
            "# AbstractWriter.write() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def initFilesWrite(obj):
        """
        Defined to generate files for generated code products.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.initFilesWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def startSourceFilesWrite(obj):
        """
        Defined to generate starting static code within files.
        """
        raise Exception(
            "# AbstractWriter.startSourceFilesWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def includes1Write(obj):
        """
        Defined to generate includes within a file.
        Usually used for the base classes but also for Port types
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.includesWrite1() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def includes2Write(obj):
        """
        Defined to generate internal includes within a file.
        Usually used for data type includes and system includes.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.includesWrite2() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def namespaceWrite(obj):
        """
        Defined to generate namespace code within a file.
        Also any pre-condition code is generated.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.namespaceWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def publicWrite(obj):
        """
        Defined to generate public stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.publicWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def protectedWrite(obj):
        """
        Defined to generate protected stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.protectedWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def privateWrite(obj):
        """
        Defined to generate private stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractWriter.privateWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def finishSourceFilesWrite(obj):
        """
        Defined to generate ending static code within files.
        """
        raise Exception(
            "# AbstractWriter.endSourceFilesWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictStartWrite(obj):
        """
        Defined to generate start of command Python class.
        """
        raise Exception(
            "# DictStartWrite.startCommandWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictHeaderWrite(obj):
        """
        Defined to generate header for Python command class.
        """
        raise Exception(
            "# DictStartWrite.commandHeaderWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictBodyWrite(obj):
        """
        Defined to generate body for Python command class.
        """
        raise Exception(
            "# DictStartWrite.commandBodyWrite() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def isSync(str):
        return str is not None and str.lower() == "sync"

    @staticmethod
    def isAsync(str):
        return str is not None and str.lower() == "async"

    @staticmethod
    def isSerial(str):
        return str is not None and str.lower() == "serial"

    @staticmethod
    def isInput(str):
        return str is not None and str.lower() == "input"
