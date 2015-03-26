import QtQuick 2.2
import QtQuick.Controls 1.1

Item {
    property alias open: openAction;
    property alias save: saveAction;
    property alias quit: quitAction;

    property alias undo: undoAction;
    property alias redo: redoAction;

    property alias deleteSelection: deleteSelectionAction;

    property alias deleteObject: deleteObjectAction;
    property alias centerObject: centerObjectAction;
    property alias multiplyObject: multiplyObjectAction;
    property alias splitObject: splitObjectAction;

    property alias deleteAll: deleteAllAction;
    property alias reloadAll: reloadAllAction;
    property alias resetAllTranslation: resetAllTranslationAction;
    property alias resetAll: resetAllAction;

    property alias addMachine: addMachineAction;
    property alias configureMachines: settingsAction;

    property alias preferences: preferencesAction;
    property alias help: helpAction;
    property alias about: aboutAction;

    Action {
        id: undoAction;
        //: Undo action
        text: qsTr("Undo");
        iconName: "edit-undo";
        shortcut: StandardKey.Undo;
    }

    Action {
        id: redoAction;
        //: Redo action
        text: qsTr("Redo");
        iconName: "edit-redo";
        shortcut: StandardKey.Redo;
    }

    Action {
        id: quitAction;
        //: Quit action
        text: qsTr("Quit");
        iconName: "application-exit";
        shortcut: StandardKey.Quit;
    }

    Action {
        id: preferencesAction;
        //: Preferences action
        text: qsTr("Preferences");
        iconName: "configure";
    }

    Action {
        id: addMachineAction;
        //: Add a Machine action
        text: qsTr("Add Printer...");
    }

    Action {
        id: settingsAction;
        //: Manage Printers action
        text: qsTr("Configure Printers");
        iconName: "configure";
    }

    Action {
        id: helpAction;
        //: Show Manual action
        text: qsTr("Show Manual");
        iconName: "help-contents";
        shortcut: StandardKey.Help;
    }

    Action {
        id: aboutAction;
        //: About action
        text: qsTr("About...");
        iconName: "help-about";
    }

    Action {
        id: deleteSelectionAction;
        //: Delete selection action
        text: qsTr("Delete Selection");
        iconName: "edit-delete";
        shortcut: StandardKey.Delete;
    }

    Action {
        id: deleteObjectAction;
        //: Delete object action
        text: qsTr("Delete Object");
        iconName: "edit-delete";
    }

    Action {
        id: centerObjectAction;
        //: Center object action
        text: qsTr("Center Object on Platform");
    }

    Action {
        id: multiplyObjectAction;
        //: Duplicate object action
        text: qsTr("Duplicate Object");
    }

    Action {
        id: splitObjectAction;
        //: Split object action
        text: qsTr("Split Object into Parts");
        enabled: false;
    }

    Action {
        id: deleteAllAction;
        //: Clear build platform action
        text: qsTr("Clear Build Platform");
        iconName: "edit-clear";
    }

    Action {
        id: reloadAllAction;
        //: Reload all objects action
        text: qsTr("Reload All Objects");
    }

    Action {
        id: resetAllTranslationAction;
        //: Reset all positions action
        text: qsTr("Reset All Object Positions");
    }

    Action {
        id: resetAllAction;
        //: Reset all positions action
        text: qsTr("Reset All Object Transformations");
    }

    Action {
        id: openAction;
        //: Open file action
        text: qsTr("Open...");
        iconName: "document-open";
        shortcut: StandardKey.Open;
    }

    Action {
        id: saveAction;
        //: Save file action
        text: qsTr("Save...");
        iconName: "document-save";
        shortcut: StandardKey.Save;
    }
}
