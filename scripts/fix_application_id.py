#!/usr/bin/env python3
from pathlib import Path
import sys
root=Path(sys.argv[1]).resolve()
p=root/'android/app/build.gradle.kts'
s=p.read_text()
s=s.replace('applicationId = "com.follow.clash"','applicationId = "com.follow.clash.qiyiguo112"')
s=s.replace('applicationIdSuffix = ".dev"','')
s=s.replace('    id("com.google.gms.google-services")','    // Custom application ID has no upstream Firebase registration.')
p.write_text(s)
assert 'applicationId = "com.follow.clash.qiyiguo112"' in s
assert 'applicationIdSuffix' not in s
print('PASS: fixed install ID com.follow.clash.qiyiguo112; native namespace/channel ABI unchanged')
