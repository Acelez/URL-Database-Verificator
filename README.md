Installiere die benötigten Pakete: Stelle sicher, dass Python und pip installiert sind. Installiere dann die benötigten Python-Pakete:
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests pymongo

----------

Downloade die Dateien

----------

Danach:

Ersetze in domain domain_checker.service /path/to/your/domain_checker.py mit dem tatsächlichen Pfad zu deinem Skript und your_username sowie your_group mit deinem Benutzernamen und deiner Gruppe.
Installiere und starte den Dienst: Kopiere die Dienstdatei nach /etc/systemd/system/ und lade die Systemd-Konfiguration neu:

Danach: 

sudo cp domain_checker.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable domain_checker.service
sudo systemctl start domain_checker.service


Überprüfe den Dienst: Stelle sicher, dass der Dienst läuft:
sudo systemctl status domain_checker.service

Mit diesen Schritten sollte dein Skript als Dienst auf dem Server laufen und kontinuierlich die Domains überprüfen. Wenn du Fragen hast oder weitere Hilfe benötigst, lass es mich wissen!
