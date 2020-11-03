$location = Get-Location
pyinstaller --noconfirm --onefile --windowed  "$location/client.py"
