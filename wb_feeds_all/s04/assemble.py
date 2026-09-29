import base64, json
from pathlib import Path
b64=open('/mnt/files/four-files/s04.b64').read().strip()
print('b64_len',len(b64))
assert len(b64)==189732, len(b64)
raw=base64.b64decode(b64)
assert raw[:3]==b'\xff\xd8\xff'
Path('/mnt/files/four-files/slide-04.jpg').write_bytes(raw)
print('jpg',len(raw))
res,err=run_composio_tool('GITHUB_COMMIT_MULTIPLE_FILES',{
  'owner':'innovalos','repo':'tmp-four-files-wed-20260930','branch':'main',
  'message':'add slide-04.jpg binary',
  'upserts':[{'path':'slide-04.jpg','content':b64,'encoding':'base64'}]
}, account='github_putty-clod')
print('commit_err',err)
print(str(res)[:600] if res else None)
up,uerr=upload_local_file('/mnt/files/four-files/slide-04.jpg')
print('up_err',uerr)
print(json.dumps(up,default=str)[:800] if up else None)
