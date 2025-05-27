import hashlib
from pathlib import Path

#locatin of file for scanning
desktop = Path.home() / "Desktop"
print(f"[DEBUG] Desktop: {desktop}")
file_to_scan = desktop / "test.exe"
malware_db_path = desktop / "malware_hashes.txt"

# making hash from SHA256 file
def get_sha256(file_path: Path) -> str:
    sha256 = hashlib.sha256()
    try:
       with file_path.open('rb') as F:
           for chunk in iter(lambda: F.read(4096), b""):
               sha256.update(chunk)
       return sha256.hexdigest()
    except Exception as e:
        print(f"[!] error in reading {str(e)}")
        return ""

 # hash file
if not file_to_scan.exists():
    print(f"[!] file does not exist {file_to_scan.name}")
    print("please make sure the file exists")
    print(f"[!] {file_to_scan.name} file exists")
    print(" name of the file is exactly correct")
    exit()
if not malware_db_path.exists():
    print(f"[!] malware db does not exist {malware_db_path}")
    exit()

file_hash = get_sha256(file_to_scan)
if not file_hash:
    exit()
    
with malware_db_path.open('r') as f:
    known_hashes = {line.strip() for line in f if line.strip()}

print(f"\n results:")
print(f" - file hash: {file_hash}")
print(f"number of known hashes: {len(known_hashes)}")
    
if file_hash in known_hashes:
    print(f"[!] file has a known hash {file_hash}")
else:
    print(f"[!] file has no known hash {file_hash}")
