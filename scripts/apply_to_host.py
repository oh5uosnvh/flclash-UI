#!/usr/bin/env python3
from pathlib import Path
import shutil,sys
kit=Path(__file__).resolve().parents[1]
host=Path(sys.argv[1]).resolve()
assert (host/'pubspec.yaml').is_file(),'full FlClash host is required'
for p in (kit/'lib').rglob('*.dart'):
 q=host/p.relative_to(kit);q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
for p in (kit/'test').glob('*.dart'):
 q=host/'test/views'/p.name;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
print('PASS: UI overlay and real widget regression tests applied')
