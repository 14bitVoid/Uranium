from . import USBPrinterManager

from UM.i18n import i18nCatalog

i18n_catalog = i18nCatalog('plugins')

def getMetaData():
    return {
        'type': 'extension',
        'plugin': {
            'name': 'USB printing',
            'author': 'Jaime van Kessel',
            'version': '1.0',
            'description': i18n_catalog.i18nc('usb printing description','Accepts G-Code and sends them to a printer. Plugin can also update firmware')
        }
    }
        
def register(app):
    return USBPrinterManager.USBPrinterManager()
