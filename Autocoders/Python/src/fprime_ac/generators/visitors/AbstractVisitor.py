# ===============================================================================
# NAME: AbstractVisitor.py
#
# DESCRIPTION: Defines the visitor interface for all code generation.
#
# AUTHOR: reder
# EMAIL:  reder@jpl.nasa.gov
# DATE CREATED  : Feb. 5 2013
#
# Copyright 2013, California Institute of Technology.
# ALL RIGHTS RESERVED. U.S. Government Sponsorship acknowledged.
# ===============================================================================
#
# Python standard modules
#
import logging
import os
import sys

from fprime_ac.utils.buildroot import (
    BuildRootMissingException,
    build_root_relative_path,
)

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
class AbstractVisitor:

    __generate_empty_file = False

    """
    Defines the visitor public methods.
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
    def initFilesVisit(obj):
        """
        Defined to generate files for generated code products.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.initFilesVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def startSourceFilesVisit(obj):
        """
        Defined to generate starting static code within files.
        """
        raise Exception(
            "# AbstractVisitor.startSourceFilesVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def includes1Visit(obj):
        """
        Defined to generate includes within a file.
        Usually used for the base classes but also for Port types
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.includesVisit1() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def includes2Visit(obj):
        """
        Defined to generate internal includes within a file.
        Usually used for data type includes and system includes.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.includesVisit2() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def namespaceVisit(obj):
        """
        Defined to generate namespace code within a file.
        Also any pre-condition code is generated.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.namespaceVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def publicVisit(obj):
        """
        Defined to generate public stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.publicVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def protectedVisit(obj):
        """
        Defined to generate protected stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.protectedVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def privateVisit(obj):
        """
        Defined to generate private stuff within a class.
        @param args: the instance of the concrete element to operation on.
        """
        raise Exception(
            "# AbstractVisitor.privateVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def finishSourceFilesVisit(obj):
        """
        Defined to generate ending static code within files.
        """
        raise Exception(
            "# AbstractVisitor.endSourceFilesVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictStartVisit(obj):
        """
        Defined to generate start of command Python class.
        """
        raise Exception(
            "# DictStartVisit.startCommandVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictHeaderVisit(obj):
        """
        Defined to generate header for Python command class.
        """
        raise Exception(
            "# DictStartVisit.commandHeaderVisit() - Implementation Error: you must supply your own concrete implementation."
        )

    @staticmethod
    def DictBodyVisit(obj):
        """
        Defined to generate body for Python command class.
        """
        raise Exception(
            "# DictStartVisit.commandBodyVisit() - Implementation Error: you must supply your own concrete implementation."
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

    @staticmethod
    def relativePath():
        """
        If BUILD_ROOT is set, get the relative path to current execution location
        """
        path = os.getcwd()
        try:
            relative_path = build_root_relative_path(path)
        except BuildRootMissingException as bre:
            PRINT.info(
                "ERROR: BUILD_ROOT and current execution path (%s) not consistent! %s"
                % (path, str(bre))
            )
            sys.exit(-1)
        DEBUG.debug("Relative path: %s", relative_path)
        return relative_path
