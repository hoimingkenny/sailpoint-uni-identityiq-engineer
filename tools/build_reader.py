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
  elif mode in ('list','ordered'):
   tag='ol' if mode=='ordered' else 'ul';out.append('<'+tag+'>'+''.join('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',v))+'</li>' for v in buf)+'</'+tag+'>')
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
  newmode='table' if line.startswith('|') else 'list' if line.startswith('- ') else 'ordered' if re.match(r'^\d+\. ',line) else 'paragraph'
  if newmode!=mode:flush()
  mode=newmode;buf.append(line)
 flush();return ''.join(out)

css='body{font:16px system-ui,sans-serif;color:#22374a;background:#f3f6f9;margin:0}header{background:#102f4d;color:white;padding:20px 30px}header a{color:white}main{max-width:1000px;margin:25px auto;background:white;padding:35px;border:1px solid #dce5eb;border-radius:8px}h1,h2{color:#102f4d}h2{margin-top:40px;border-bottom:2px solid #c626ac;padding-bottom:12px}h3{margin-top:30px}p,li{line-height:1.8}li{margin:8px 0}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}td{padding:12px;border:1px solid #dce5eb;line-height:1.7;vertical-align:top}tr:first-child{background:#eaf1f7;font-weight:600}a{color:#006ba6}code{background:#edf2f6;padding:2px 4px}figure{padding:15px;background:#f5f8fb;border:1px solid #dce5eb;border-radius:5px;margin:24px 0}img{display:block;max-width:100%;max-height:550px;margin:auto;background:white;object-fit:contain}figcaption{font-size:13px;color:#53687b;line-height:1.6;margin-top:12px}.warning{border-left:5px solid #bb7216;background:#fff4dc;padding:18px;line-height:1.8}input{padding:10px;font:inherit;width:100%;box-sizing:border-box;margin-bottom:16px}@media print{body{background:white}header{display:none}main{border:0;margin:0;padding:0}figure,tr{break-inside:avoid}h2,h3{break-after:avoid}}'

def page(title, body, prefix=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+css+' .topic[hidden]{display:none}nav a{display:block;padding:5px} .status{background:#fff4dc;padding:18px;border-left:5px solid #bb7216}@media(max-width:700px){main{padding:20px;margin:10px}}</style></head><body><header><strong>Identity Security Engineer · IdentityIQ</strong><p>Study edition · updated 16 November 2026</p><a href="'+prefix+'index.html">Study book</a> · <a href="'+prefix+'coverage-report.html">Coverage and missing material</a></header><main>'+body+'</main></body></html>'

study=ROOT/'study'
path=json.loads((ROOT/'inventory/learning-path.json').read_text())
intro_topics=json.loads((ROOT/'inventory/introduction-topics.json').read_text())['topics']
essentials=path['entries'][1]
courses=[{'id':'intro','directory':'01-introduction','title':'IdentityIQ Introduction','status':'12 topics have notes; five video demonstrations remain untranscribed.'},{'id':'ess','directory':'02-essentials','title':'IdentityIQ Essentials','status':'Modules 1–6 of 33 have notes and 49 handout illustrations. Modules 7–33 remain pending.'}]
all_sections=[];total_images=0

def unique_html(md,prefix):
    return re.sub(r'id="section-(\d+)"',lambda m:f'id="{prefix}-h{m[1]}"',render(md))

def search_ui(label):
    return '<p><label for="search">'+escape(label)+'</label></p><input id="search" type="search" placeholder="Search concepts, examples or steps"><p id="count" aria-live="polite"></p>'

search_script='''<script>const search=document.querySelector('#search');const topics=[...document.querySelectorAll('.topic')];function filter(){const query=search.value.trim().toLowerCase();let count=0;topics.forEach(section=>{section.hidden=!section.textContent.toLowerCase().includes(query);if(!section.hidden)count++});document.querySelector('#count').textContent=count+' of '+topics.length+' reading sections shown'}search.addEventListener('input',filter);document.querySelectorAll('nav a').forEach(link=>link.addEventListener('click',()=>{search.value='';filter()}));filter();</script>'''

for course in courses:
    chapter=study/'courses'/course['directory'];md=(chapter/'notes.md').read_text()
    assert not re.search(r'\{(?:SLIDES|GUIDE|IMAGE)',md)
    manifest=json.loads((chapter/'saved-assets.json').read_text())
    refs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',md)
    assert set(refs)=={a['file'] for a in manifest},course['title']
    for asset in manifest:
        image=chapter/asset['file'];assert image.exists() and hashlib.sha256(image.read_bytes()).hexdigest()==asset['sha256']
    total_images+=len(manifest)
    lead,*chunks=re.split(r'(?=^## )',md,flags=re.M)
    toc='<nav aria-label="'+course['title']+' sections">'
    sections=[]
    for i,chunk in enumerate(chunks,1):
        identifier=f'{course["id"]}-section-{i}'
        title=chunk.splitlines()[0][3:]
        toc+=f'<a href="#{identifier}">{escape(title)}</a>'
        html=f'<section class="topic" id="{identifier}">'+unique_html(chunk,identifier)+'</section>'
        sections.append(html)
    toc+='</nav>'
    chapter_body='<div class="status">'+escape(course['status'])+'</div>'+unique_html(lead,course['id']+'-lead')+toc+search_ui('Search this course')+''.join(sections)+search_script
    if course['id']=='ess':
        roadmap='# Essentials module status\n\n| Module | Title | Notes |\n| --- | --- | --- |\n'
        for m in essentials['modules']:roadmap+=f'| {m["number"]} | {m["title"]} | '+('Available; audiovisual gaps documented' if m['number']<=6 else 'Pending')+' |\n'
        chapter_body=chapter_body.replace(search_script,unique_html(roadmap,'ess-roadmap')+search_script)
    (chapter/'index.html').write_text(page(course['title']+' — Study Notes',chapter_body,'../../'))
    for section in sections:
        def localize(match):
            key,value=match.groups()
            if value.startswith(('#','https:','http:','mailto:')):return match[0]
            return f'{key}="courses/{course["directory"]}/{value}"'
        all_sections.append(re.sub(r'(href|src)="([^"]+)"',localize,section))

report=['# Coverage and Missing Material','','**This is an incomplete study edition.** The verified learning path lists five teaching courses with a displayed duration of 60 hours 30 minutes, plus two certification exam entries. Introduction has twelve topic notes. Essentials now has notes for its first six of 33 numbered teaching modules.','','## Course status','','| Course | Coverage |','| --- | --- |']
for e in path['entries']:report.append(f'| {e["title"]} | {e.get("capture_status","Exam content excluded")} |')
report+=['','## IdentityIQ Introduction','','All twelve topic bodies were read with available flashcards, five request markers, three event accordions, the certification timeline and four role-example tabs. Sixty-two downloaded inline images are included unchanged.','','The following videos are **not saved or fully transcribed**: Access Request (Topic 5); Detective and Preventative Policy Usage (Topic 8); Identity Search and Reports (Topic 9). Five associated poster backgrounds were also not saved. Exact observed paths are recorded in [Introduction coverage](courses/01-introduction/coverage.json). External linked resources are not comprehensively archived.','','## IdentityIQ Essentials','','Modules 1–6 have English paraphrased notes based on the accessible Camtasia caption-search results and the relevant handouts. Forty nonblank presentation pages and nine Exercise 1 guide pages are rendered as 49 illustrations. These are original English PDF-page illustrations, not extracted video frames. Both official handouts are saved in full: 461 presentation pages and 257 exercise-guide pages. Later pages remain unprocessed as study notes.','','Caption search can contain duplicate lines or formatting artifacts and does not certify a word-perfect transcript. Uncaptioned visuals, animation and all changing video frames have not been fully captured. Original videos and executable knowledge checks are not archived.','','Modules **7–33** remain pending. The Accessing the Virtual Machine lesson, My lab interface, remaining exercise instructions, appendix procedures and linked references are not yet incorporated. Start Here was empty in the inspected state; its automatic LMS completion marker does not establish completion of other content. No VM operations or live configuration changes were performed.','','The guide identifies IdentityIQ 8.2b / 2021; some slides show 8.1 and 2020 examples. Platform lists and settings are presented as course-version material. The Module 6 player heading incorrectly says Product Architecture; its captions and navigation describe Installation. The slide spelling Accelerator Park differs from the narration Accelerator Pack. Original illustrations are unchanged.','','See [the detailed Essentials evidence record](courses/02-essentials/coverage.json), [Essentials notes](courses/02-essentials/notes.md), and the [per-topic / module coverage CSV](lesson-coverage.csv).','','## Restricted and excluded content','','Advanced Provisioning and Workflows requires completion of an accepted IdentityIQ Essentials course before registration. Only its visible outline has been recorded. No prerequisite restriction was bypassed.','','Rules / Scripts / API and Custom Reports remain at outline-only coverage. Certification exam questions and answers are excluded; no assessment attempt was submitted. The exercise Answer Key was not used.','','The full internal lesson count across all courses is not verified. Do not add outer numbered modules to internal SCORM topics and interpret that as a complete path lesson total.','','The reader uses an offline reading layout, rather than recreating the original LMS screens. Source diagrams, interface illustrations and icons are retained inside the saved inline images or PDF pages described above. A complete all-media copy of the learning path has not been achieved.']
(study/'coverage-report.md').write_text('\n'.join(report)+'\n')
(study/'coverage-report.html').write_text(page('Coverage and Missing Material',render('\n'.join(report))))
nav='<nav aria-label="Courses"><a href="courses/01-introduction/index.html">Introduction: 12 topics</a><a href="courses/02-essentials/index.html">Essentials: Modules 1–6 plus Exercise 1</a><a href="coverage-report.html">Pending and missing material</a></nav>'
heading='<h1>Identity Security Engineer, IdentityIQ</h1><div class="status"><strong>Essentials has started: 6 of 33 modules have notes.</strong><br>Introduction: 12 topics / 62 original images. Essentials: 6 modules / 49 handout page illustrations. The whole path remains incomplete.</div><p>English study notes in course order, with diagrams and examples beside their explanations. Select an illustration to open its full local image. No internet connection is required for the saved notes and media.</p>'
(study/'index.html').write_text(page('IdentityIQ Engineer — Learning Notes',heading+nav+search_ui('Search all available notes')+''.join(all_sections)+search_script))
records=[]
for t in intro_topics:records.append({'course':'IdentityIQ Introduction','level':'internal topic','number':t['number'],'title':t['title'],'notes_status':t['notes_status'],'media_status':f'{t["image_files"]} inline images; '+('video gap' if t['video_gap'] else 'see coverage record')})
for m in essentials['modules']:records.append({'course':'IdentityIQ Essentials','level':'numbered teaching module','number':m['number'],'title':m['title'],'notes_status':'English paraphrased notes available' if m['number']<=6 else 'Pending','media_status':'Caption-search text reviewed; handout illustrations included where available; audiovisual gaps' if m['number']<=6 else 'Handouts saved; no lesson-level study processing yet'})
(study/'lesson-coverage.json').write_text(json.dumps(records,indent=2)+'\n')
with (study/'lesson-coverage.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
(ROOT/'capture-progress.json').write_text(json.dumps({'edition':'Essentials first batch','verified_date':'2026-11-16','path_complete':False,'teaching_courses':5,'courses_with_some_notes':2,'introduction_topics_with_notes':12,'essentials_modules_with_notes':list(range(1,7)),'essentials_pending_modules':list(range(7,34)),'saved_image_files':total_images,'image_breakdown':{'introduction_inline_originals':62,'essentials_rendered_handout_pages':49},'official_essentials_handouts_saved':2,'next_module':'Essentials 7 — Creating Identity Cubes','restricted_course':'Advanced Provisioning and Workflows','restriction':'Accepted IdentityIQ Essentials completion required before registration'},indent=2)+'\n')
print(json.dumps({'introduction_topics':12,'essentials_modules':6,'essentials_pending':27,'saved_images':total_images,'coverage_rows':len(records)}))
