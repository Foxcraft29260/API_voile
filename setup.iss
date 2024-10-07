[Setup]
AppName=weather_finder
AppVersion=1.0
DefaultDirName={localappdata}\weather_finder
DefaultGroupName=weather_finder
UninstallDisplayIcon={app}\icon.ico
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=setup_weather_finder
Compression=lzma
SolidCompression=yes

[Files]
Source: "D:\programmation\Github\API_voile\output\Weather finder.exe"; DestDir: "{localappdata}\weather_finder"; Flags: ignoreversion
Source: "D:\programmation\Github\API_voile\icon.ico"; DestDir: "{localappdata}\weather_finder"; Flags: ignoreversion

[Icons]
Name: "{group}\weather_finder"; Filename: "{app}\weather_finder.exe"
Name: "{group}\Uninstall weather_finder"; Filename: "{uninstallexe}"