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
assert asset_count==827

rules=ROOT/'study/courses/03-rules-scripts-api'
rules_notes=(rules/'notes.md').read_text()
assert list(map(int,re.findall(r'^## (\d+)\. ',rules_notes,re.M)))==list(range(1,9))
assert len(list((rules/'topics').glob('*.html')))==8
assert len(parsed[(rules/'index.html').resolve()].images)==42
assert len(parsed[(rules/'practice-companion.html').resolve()].images)==37
assert '<pre><code class="language-java">' in (rules/'index.html').read_text()
assert '&lt;ReferencedRules&gt;' in (rules/'index.html').read_text()
media=json.loads((rules/'saved-videos.json').read_text())
assert len(media)==9
for video in media:
    file=rules/video['file'];assert file.exists() and hashlib.sha256(file.read_bytes()).hexdigest()==video['sha256']
    assert video['duration_seconds']>0
    assert video['file'] in rules_notes
    assert file.stat().st_size<100_000_000
import zipfile
with zipfile.ZipFile(rules/'handouts/course-artifacts.zip') as archive:assert archive.testzip() is None
for item in json.loads((rules/'coverage.json').read_text())['downloads']:
    assert hashlib.sha256((rules/item['file']).read_bytes()).hexdigest()==item['sha256']

reports=ROOT/'study/courses/04-custom-reports'
reports_notes=(reports/'notes.md').read_text()
assert list(map(int,re.findall(r'^## (\d+)\. ',reports_notes,re.M)))==list(range(1,9))
assert len(list((reports/'modules').glob('*.html')))==8
assert len(parsed[(reports/'index.html').resolve()].images)==0
assert len(parsed[(reports/'practice-companion.html').resolve()].images)==0
assert '&lt;QueryParameters&gt;' in (reports/'index.html').read_text()
assert '&lt;![CDATA[' in (reports/'index.html').read_text()
for item in json.loads((reports/'coverage.json').read_text())['downloads']:
    assert hashlib.sha256((reports/item['file']).read_bytes()).hexdigest()==item['sha256']
print(json.dumps({'html_pages_checked':len(parsed),'local_links_checked':link_count,'verified_image_files':asset_count,'essentials_modules_with_substantive_notes':len(chunks),'custom_reports_modules':8,'rules_api_topics':8,'saved_videos_checked':len(media),'full_path_complete':False}))
