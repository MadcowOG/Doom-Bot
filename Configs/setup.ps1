mkdir ffmpeg
cd ffmpeg
Invoke-WebRequest -Uri 'https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2021-08-14-12-36/ffmpeg-n4.4-80-gbf87bdd3f6-win64-gpl-4.4.zip' -UseBasicParsing -Outfile './ffmpeg.zip'
Expand-Archive 'ffmpeg.zip' 
cd ffmpeg
cd 'ffmpeg-n4.4-80-gbf87bdd3f6-win64-gpl-4.4'
cd bin
$variable =  Get-Location
# TODO! Get this to add a semi colon to the end of the current path
$Path = [System.Environment]::GetEnvironmentVariable("Path", "Machine")
$NewPath = $Path + $variable
[System.Environment]::SetEnvironmentVariable("Path", $NewPath, "Machine")