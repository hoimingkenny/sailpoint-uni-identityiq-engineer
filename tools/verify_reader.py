"""Verify local reader navigation, illustration references, source hashes and scope."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
class Document(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.links=[];self.images=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        for key in ('href','src'):
            if key in attrs:self.links.append(attrs[key])
        if tag=='img':self.images.append(attrs.get('src'))
parsed={}
for file in ROOT.rglob('*.html'):
    doc=Document();doc.feed(file.read_text());assert len(doc.ids)==len(set(doc.ids)),f'Duplicate ID: {file}'
    parsed[file.resolve()]=doc
link_count=0
for file,doc in parsed.items():
    for link in doc.links:
        if link.startswith(('http:','https:','mailto:','data:')):continue
        target,_,anchor=link.partition('#')
        destination=(file.parent/unquote(target)).resolve() if target else file
        assert destination.exists(),f'Missing local target: {file}: {link}'
        if anchor and destination.suffix=='.html':assert unquote(anchor) in parsed[destination].ids,f'Missing anchor: {file}: {link}'
        link_count+=1
asset_count=0
for chapter in (ROOT/'study/courses').iterdir():
    manifest=json.loads((chapter/'saved-assets.json').read_text())
    note_sources=(chapter/'notes.md').read_text()
    if (chapter/'practice-companion.md').exists():note_sources+='\n'+(chapter/'practice-companion.md').read_text()
    refs=set(re.findall(r'!\[[^\]]*\]\(([^)]+)\)',note_sources))
    assert refs=={a['file'] for a in manifest},f'Illustration coverage mismatch: {chapter}'
    for asset in manifest:
        file=chapter/asset['file'];assert hashlib.sha256(file.read_bytes()).hexdigest()==asset['sha256'],file
    asset_count+=len(manifest)
ess=ROOT/'study/courses/02-essentials'
notes=(ess/'notes.md').read_text();numbered=re.findall(r'^## (\d+)\. ',notes,re.M)
assert list(map(int,numbered))==list(range(1,34))
chunks=re.split(r'(?=^## \d+\.)',notes,flags=re.M)[1:]
for number,chunk in enumerate(chunks,1):
    prose=re.sub(r'!\[[^\]]*\]\([^)]*\)','',chunk)
    assert len(prose.split())>130,f'Insufficient prose in module {number}'
coverage=json.loads((ess/'coverage.json').read_text())
for source in coverage['official_downloads']:
    file=ess/source['file'];assert hashlib.sha256(file.read_bytes()).hexdigest()==source['sha256'],file
assert coverage['full_audiovisual_capture_complete'] is False
assert json.loads((ROOT/'capture-progress.json').read_text())['path_complete'] is False
assert len(list((ess/'modules').glob('*.html')))==33
assert len(parsed[(ess/'index.html').resolve()].images)==429
assert len(parsed[(ess/'practice-companion.html').resolve()].images)==257
assert asset_count==748
print(json.dumps({'html_pages_checked':len(parsed),'local_links_checked':link_count,'verified_image_files':asset_count,'essentials_modules_with_substantive_notes':len(chunks),'full_path_complete':False}))
