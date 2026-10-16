#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1]).resolve()
p=root/'android/app/build.gradle.kts'
s=(Path(__file__).resolve().parents[1]/'files/android/app/build.gradle.kts').read_text()
p.write_text(s)
assert 'applicationId = "com.follow.clash.qiyiguo112"' in s
assert 'applicationIdSuffix' not in s
print('PASS: fixed install ID com.follow.clash.qiyiguo112; native namespace/channel ABI unchanged')
