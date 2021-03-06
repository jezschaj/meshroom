from meshroom.core import desc


class ExportMayaMVG(desc.CommandLineNode):
    internalFolder = '{cache}/{nodeType}/{uid0}/'
    commandLine = 'aliceVision_exportMayaMVG {allParams}'

    inputs = [
        desc.File(
            name='input',
            label='Input SfMData',
            description='',
            value='',
            uid=[0],
        ),
    ]

    outputs = [
        desc.File(
            name='output',
            label='Output Folder',
            description='Folder for MayaMVG outputs: undistorted images and thumbnails.',
            value='{cache}/{nodeType}/{uid0}/',
            uid=[],
        ),
    ]
