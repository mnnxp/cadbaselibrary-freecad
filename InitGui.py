import os
import FreeCAD as App


class CadbaseLibrary(Workbench):

    from CdbsModules.Translate import translate

    MenuText = translate('InitGui', 'CADBase Library')
    ToolTip = translate(
        'InitGui',
        'The workbench is designed to use components (parts) from CADBase in the FreeCAD interface. \
Component modifications contain sets of files for various CAD systems. \
This workbench will work with data from the FreeCAD set, without downloading documentation and data from other file sets.'
    )
    Icon = os.path.join(
        App.getUserAppDataDir() + 'Mod/CadbaseLibrary/Icons',
        'CadbaseLibrary.xpm'
    )

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import CadbaseMacro

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        from PySide import QtGui
        m = Gui.getMainWindow()
        w = m.findChild(QtGui.QDockWidget, 'CADBaseLibrary')
        if w and hasattr(w, 'isVisible') and not w.isVisible():
            w.show()
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"

    def GetClassName(self):
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return 'Gui::PythonWorkbench'

Gui.addWorkbench(CadbaseLibrary())
