[Setup]
AppName=weather_finder
AppVersion=1.0
DefaultDirName={localappdata}\weather_finder
DefaultGroupName=weather_finder
UninstallDisplayIcon={app}\icon.ico
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename==weather_finder Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\programmation\Github\API_voile\output\weather_finder.exe"; DestDir: "{localappdata}\weather_finder"; Flags: ignoreversion
Source: "D:\programmation\Github\API_voile\icon.ico"; DestDir: "{localappdata}\weather_finder"; Flags: ignoreversion

[Icons]
Name: "{group}\weather_finder"; Filename: "{app}\weather_finder.exe"
Name: "{group}\Uninstall weather_finder"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le &bureau"; GroupDescription: "Icônes supplémentaires :"; Flags: unchecked

[Run]
Filename: "{app}\weather_finder.exe"; Description: "{cm:LaunchProgram,weather_finder}"; Flags: nowait postinstall skipifsilent