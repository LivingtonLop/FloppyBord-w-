; Script de ejemplo para Inno Setup

[Setup]
AppName=FloppyBord
AppVersion=1.0
DefaultDirName={pf}\FloppyBord
DefaultGroupName=FloppyBord
OutputDir=output\installer
OutputBaseFilename=FloppyBordInstaller
Compression=lzma
SolidCompression=yes

[Files]
Source: "output\dist\run.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "output\dist\assets\*"; DestDir: "{app}\assets"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "output\dist\src\*"; DestDir: "{app}\src"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "output\dist\.env"; DestDir: "{app}" ; Flags: ignoreversion
[Icons]
Name: "{group}\FloppyBord"; Filename: "{app}\run.exe"

[Run]
Filename: "{app}\run.exe"; Description: "{cm:LaunchProgram,FloppyBord}"; Flags: nowait postinstall skipifsilent
