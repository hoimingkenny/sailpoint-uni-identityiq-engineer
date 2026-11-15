from pathlib import Path
from html import escape
import re,json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
def render(md):
 out=[];buf=[];mode=None;counter=0
 def inline(s):
  s=escape(s);s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s);s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s);s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s);return s
 def flush():
  nonlocal mode
  if not buf:return
  if mode=='table':
   rows=[[c.strip() for c in r.strip('|').split('|')] for r in buf];out.append('<div class="table"><table>'+''.join('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>' for row in [rows[0]]+rows[2:])+'</table></div>')
  elif mode=='list':out.append('<ul>'+''.join('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',v))+'</li>' for v in buf)+'</ul>')
  else:out.append('<p>'+inline(' '.join(buf))+'</p>')
  mode=None;buf.clear()
 for line in md.splitlines():
  if not line.strip():flush();continue
  match=re.match(r'^(#{1,5}) (.*)',line)
  if match:
   flush();level=len(match[1]);counter+=1;out.append(f'<h{level} id="section-{counter}">'+inline(match[2])+f'</h{level}>');continue
  match=re.fullmatch(r'!\[([^\]]+)\]\(([^)]+)\)',line)
  if match:
   flush();alt,src=match.groups();out.append(f'<figure><a href="{escape(src)}"><img loading="lazy" src="{escape(src)}" alt="{escape(alt)}"></a><figcaption>{escape(alt)}</figcaption></figure>');continue
  newmode='table' if line.startswith('|') else 'list' if line.startswith('- ') or re.match(r'^\d+\. ',line) else 'paragraph'
  if newmode!=mode:flush()
  mode=newmode;buf.append(line)
 flush();return ''.join(out)

css='body{font:16px system-ui,sans-serif;color:#22374a;background:#f3f6f9;margin:0}header{background:#102f4d;color:white;padding:20px 30px}header a{color:white}main{max-width:1000px;margin:25px auto;background:white;padding:35px;border:1px solid #dce5eb;border-radius:8px}h1,h2{color:#102f4d}h2{margin-top:40px;border-bottom:2px solid #c626ac;padding-bottom:12px}h3{margin-top:30px}p,li{line-height:1.8}li{margin:8px 0}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}td{padding:12px;border:1px solid #dce5eb;line-height:1.7;vertical-align:top}tr:first-child{background:#eaf1f7;font-weight:600}a{color:#006ba6}code{background:#edf2f6;padding:2px 4px}figure{padding:15px;background:#f5f8fb;border:1px solid #dce5eb;border-radius:5px;margin:24px 0}img{display:block;max-width:100%;max-height:550px;margin:auto;background:white;object-fit:contain}figcaption{font-size:13px;color:#53687b;line-height:1.6;margin-top:12px}.warning{border-left:5px solid #bb7216;background:#fff4dc;padding:18px;line-height:1.8}input{padding:10px;font:inherit;width:100%;box-sizing:border-box;margin-bottom:16px}@media print{body{background:white}header{display:none}main{border:0;margin:0;padding:0}figure,tr{break-inside:avoid}h2,h3{break-after:avoid}}'

def page(title, body, prefix=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+css+' .topic[hidden]{display:none}nav a{display:block;padding:5px} .status{background:#fff4dc;padding:18px;border-left:5px solid #bb7216}@media(max-width:700px){main{padding:20px;margin:10px}}</style></head><body><header><strong>Identity Security Engineer · IdentityIQ</strong><p>Initial study edition · 15 November 2026</p><a href="'+prefix+'index.html">Study book</a> · <a href="'+prefix+'coverage-report.html">Coverage and missing material</a></header><main>'+body+'</main></body></html>'

study=ROOT/'study'; chapter=study/'courses/01-introduction'
path=json.loads((ROOT/'inventory/learning-path.json').read_text())
topics=json.loads((ROOT/'inventory/introduction-topics.json').read_text())['topics']
coverage=json.loads((chapter/'coverage.json').read_text())
assets=json.loads((chapter/'saved-assets.json').read_text())
notes=(chapter/'notes.md').read_text()
assert '{IMAGE' not in notes
for asset in assets:
    image=chapter/asset['file']
    assert image.exists() and hashlib.sha256(image.read_bytes()).hexdigest()==asset['sha256']
refs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',notes)
assert len(refs)==62 and set(refs)=={a['file'] for a in assets}
intro,*sections=re.split(r'(?=^## \d+\.)',notes,flags=re.M)
assert len(sections)==12
body=render(intro).replace('id="section-', 'id="intro-section-')+'<nav aria-label="Introduction topics">'+''.join(f'<a href="#topic-{t["number"]}">{t["number"]}. {escape(t["title"])}</a>' for t in topics)+'</nav><p><label for="search">Search Introduction notes</label></p><input id="search" type="search" placeholder="Search concepts, examples or steps"><p id="count" aria-live="polite">12 topics shown</p>'
for i,section in enumerate(sections,1):
    html=render(section)
    html=re.sub(r'id="section-(\d+)"',lambda m:f'id="t{i}-section-{m[1]}"',html)
    body+=f'<section class="topic" id="topic-{i}">'+html+'</section>'
body+='''<script>const search=document.querySelector('#search');search.addEventListener('input',()=>{const query=search.value.trim().toLowerCase();let count=0;document.querySelectorAll('.topic').forEach(section=>{section.hidden=!section.textContent.toLowerCase().includes(query);if(!section.hidden)count++});document.querySelector('#count').textContent=count+' topics shown'});document.querySelectorAll('nav a').forEach(link=>link.addEventListener('click',()=>{search.value='';search.dispatchEvent(new Event('input'))}));</script>'''
(chapter/'index.html').write_text(page('IdentityIQ Introduction — Study Notes',body,'../../'))
summary=['# Coverage and Missing Material','','This is an initial study edition, not a complete copy of the 60-hour-30-minute learning path. Five teaching courses and two separate certification exam entries are listed in the verified path. Only Introduction currently has substantive notes.','','## Course coverage','','| Course | Current status |','| --- | --- |']
for entry in path['entries']:
    summary.append(f'| {entry["title"]} | {entry.get("capture_status", "Certification exam excluded from study capture")} |')
summary+=['','## IdentityIQ Introduction','','All twelve topic bodies were read in course order. Available flashcards, five access-request markers, three event accordions, the certification timeline and four role-example tabs were expanded into English paraphrased notes. The 62 downloaded inline image files retain their original bytes and English content. This does not establish that all visual assets of the original course were saved.','','### Videos not saved or fully transcribed','','The following demonstrations remain gaps. Their narration and complete screen-by-screen operations are not represented by the notes. English captions were available for the access-request demonstration, but a complete transcript was not obtained.','']
for v in coverage['videos_not_saved_or_transcribed']:summary.append(f'- Topic {v["topic"]}: {v["title"]}.')
summary+=['','### Known unsaved video-poster backgrounds','','The following background paths were observed in the original player but are not included as local images. They are relative to the course content directory.','']
summary+=['- `'+p+'`' for p in coverage['known_unsaved_background_paths']]
summary+=['','## Pending and restricted content','','Essentials, Rules / Scripts / API, and Custom Reports have verified outlines, but their teaching explanations, images and expanded interactions are still pending. Pending work is not an access-denied finding. Internal lesson totals across the whole path have not yet been verified, so outer module counts and internal topics must not be added together as a complete lesson total.','','Advanced Provisioning and Workflows requires completion of an accepted IdentityIQ Essentials course before registration. Only its visible nine-module outline was recorded. No prerequisite or registration restriction was bypassed.','','Certification exam content is excluded. No assessment answers, live tenant operations or lab configuration changes were submitted.','','External resources and linked downloads are not comprehensively archived. Interactive execution, LMS progress tracking, audiovisual playback and original screen layout are not reproduced. Illustrations open in their original local files when selected.','','See [the complete verified outline](../inventory/learning-path.md), [topic coverage CSV](lesson-coverage.csv), and [Introduction source and media record](courses/01-introduction/coverage.json).']
report='\n'.join(summary)+'\n'
(study/'coverage-report.md').write_text(report)
(study/'coverage-report.html').write_text(page('Coverage and Missing Material',render(report)))
path_intro='# Identity Security Engineer, IdentityIQ\n\nEnglish learning notes in course order. This initial edition contains the complete twelve-topic Introduction reading pass with 62 retained inline images. Five video demonstrations remain untranscribed. The other four teaching courses do not yet have study notes.\n\n## Learning path\n\n| Course | Status |\n| --- | --- |\n'
for entry in path['entries']:path_intro+=f'| {entry["title"]} | {entry.get("capture_status","Exam excluded")} |\n'
(study/'index.html').write_text(page('IdentityIQ Engineer — Learning Notes',render(path_intro).replace('id="section-', 'id="path-section-')+'<hr>'+body.replace('src="images/','src="courses/01-introduction/images/').replace('href="images/','href="courses/01-introduction/images/')))
records=[]
for t in topics:records.append({'course':'IdentityIQ Introduction','level':'internal topic','number':t['number'],'title':t['title'],'notes_status':t['notes_status'],'saved_image_files':t['image_files'],'video_gap':t['video_gap']})
(study/'lesson-coverage.json').write_text(json.dumps(records,indent=2)+'\n')
with (study/'lesson-coverage.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
(ROOT/'capture-progress.json').write_text(json.dumps({'edition':'Initial','path_complete':False,'teaching_courses':5,'courses_with_notes':1,'topics_with_notes':12,'saved_inline_images':62,'video_transcripts_pending':5,'next_course':'IdentityIQ Essentials','restricted_course':'IdentityIQ Implementation: Advanced Provisioning and Workflows','restriction':'Completion of an accepted IdentityIQ Essentials course required before registration','verified_date':'2026-11-15'},indent=2)+'\n')
print(json.dumps({'topics':len(sections),'image_references':len(refs),'verified_saved_files':len(assets),'path_complete':False}))
