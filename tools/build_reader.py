from pathlib import Path
from html import escape
import re,json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
def render(md):
    out=[];buf=[];mode=None;counter=0;code_lines=[];code_language=None
    def inline(text):
        text=escape(text)
        text=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',text)
        text=re.sub(r'`([^`]+)`',r'<code>\1</code>',text)
        return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',text)
    def flush():
        nonlocal mode
        if not buf:return
        if mode=='table':
            rows=[[cell.strip() for cell in row.strip('|').split('|')] for row in buf]
            out.append('<div class="table"><table>'+''.join('<tr>'+''.join('<td>'+inline(cell)+'</td>' for cell in row)+'</tr>' for row in [rows[0]]+rows[2:])+'</table></div>')
        elif mode in ('list','ordered'):
            tag='ol' if mode=='ordered' else 'ul'
            out.append('<'+tag+'>'+''.join('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',value))+'</li>' for value in buf)+'</'+tag+'>')
        else:out.append('<p>'+inline(' '.join(buf))+'</p>')
        mode=None;buf.clear()
    for line in md.splitlines():
        if line.startswith('```'):
            if code_language is None:
                flush();code_language=line[3:].strip();code_lines=[]
            else:
                language=re.sub(r'[^a-zA-Z0-9_-]','',code_language)
                out.append('<pre><code class="language-'+language+'">'+escape('\n'.join(code_lines))+'</code></pre>')
                code_language=None;code_lines=[]
            continue
        if code_language is not None:code_lines.append(line);continue
        if not line.strip():flush();continue
        match=re.match(r'^(#{1,5}) (.*)',line)
        if match:
            flush();level=len(match[1]);counter+=1
            out.append(f'<h{level} id="section-{counter}">'+inline(match[2])+f'</h{level}>');continue
        match=re.fullmatch(r'!\[([^\]]+)\]\(([^)]+)\)',line)
        if match:
            flush();alt,src=match.groups()
            out.append(f'<figure><a href="{escape(src)}"><img loading="lazy" src="{escape(src)}" alt="{escape(alt)}"></a><figcaption>{escape(alt)}</figcaption></figure>');continue
        match=re.fullmatch(r'\[([^\]]+)\]\(([^)]+\.mp4)\)',line)
        if match:
            flush();title,src=match.groups()
            out.append('<figure class="video"><figcaption>'+escape(title)+'</figcaption><video controls preload="none" src="'+escape(src)+'" aria-label="'+escape(title)+'">'+escape(title)+'</video><p><a href="'+escape(src)+'">Open saved MP4</a></p></figure>');continue
        newmode='table' if line.startswith('|') else 'list' if line.startswith('- ') else 'ordered' if re.match(r'^\d+\. ',line) else 'paragraph'
        if newmode!=mode:flush()
        mode=newmode;buf.append(line)
    assert code_language is None,'Unclosed fenced code block'
    flush();return ''.join(out)

css='pre{white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.65;background:#102f4d;color:#edf4fa;padding:20px;border-radius:6px}pre code{background:none;padding:0;color:inherit}video{display:block;width:100%;max-height:650px;background:#0c1b2e;margin-top:12px}body{font:16px system-ui,sans-serif;color:#22374a;background:#f3f6f9;margin:0}header{background:#102f4d;color:white;padding:20px 30px}header a{color:white}main{max-width:1000px;margin:25px auto;background:white;padding:35px;border:1px solid #dce5eb;border-radius:8px}h1,h2{color:#102f4d}h2{margin-top:40px;border-bottom:2px solid #c626ac;padding-bottom:12px}h3{margin-top:30px}p,li{line-height:1.8}li{margin:8px 0}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}td{padding:12px;border:1px solid #dce5eb;line-height:1.7;vertical-align:top}tr:first-child{background:#eaf1f7;font-weight:600}a{color:#006ba6}code{background:#edf2f6;padding:2px 4px}figure{padding:15px;background:#f5f8fb;border:1px solid #dce5eb;border-radius:5px;margin:24px 0}img{display:block;max-width:100%;max-height:550px;margin:auto;background:white;object-fit:contain}img[src*="exercise-"]{max-height:none;width:100%;height:auto}figcaption{font-size:13px;color:#53687b;line-height:1.6;margin-top:12px}.warning{border-left:5px solid #bb7216;background:#fff4dc;padding:18px;line-height:1.8}input{padding:10px;font:inherit;width:100%;box-sizing:border-box;margin-bottom:16px}@media print{body{background:white}header{display:none}main{border:0;margin:0;padding:0}figure,tr{break-inside:avoid}h2,h3{break-after:avoid}}'

def page(title, body, prefix=''):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+escape(title)+'</title><style>'+css+' .topic[hidden]{display:none}nav a{display:block;padding:5px} .status{background:#fff4dc;padding:18px;border-left:5px solid #bb7216}@media(max-width:700px){main{padding:20px;margin:10px}}</style></head><body><header><strong>Identity Security Engineer · IdentityIQ</strong><p>Study edition · updated 16 November 2026</p><a href="'+prefix+'index.html">Study book</a> · <a href="'+prefix+'coverage-report.html">Coverage and missing material</a></header><main>'+body+'</main></body></html>'

study=ROOT/'study'
path=json.loads((ROOT/'inventory/learning-path.json').read_text())
intro_topics=json.loads((ROOT/'inventory/introduction-topics.json').read_text())['topics']
essentials=path['entries'][1]
ess_root=study/'courses/02-essentials'
ess_coverage=json.loads((ess_root/'coverage.json').read_text())
processed=set(ess_coverage['modules_with_notes']);captions=set(ess_coverage['caption_search_reviewed_modules'])
courses=[{'id':'intro','directory':'01-introduction','title':'IdentityIQ Introduction','status':'12 topics have notes; five video demonstrations remain untranscribed.'},{'id':'ess','directory':'02-essentials','title':'IdentityIQ Essentials','status':f'All {len(processed)} numbered modules have notes. {ess_coverage["saved_image_files"]} original handout page illustrations are preserved. Full video narration for Modules 8–33 remains unreviewed.'},{'id':'rules','directory':'03-rules-scripts-api','title':'IdentityIQ Rules, Scripts, and API','status':'All eight topic bodies have notes; 42 inline images, nine saved videos and all 37 exercise-guide pages. Video narration is not fully transcribed.'},{'id':'reports','directory':'04-custom-reports','title':'IdentityIQ Custom Reports','status':'All eight numbered modules have handout-based notes; Original slides and guide images are linked through SailPoint rather than reproduced. Narration and player-state gaps are documented.'}]
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
    combined=md+((chapter/'practice-companion.md').read_text() if (chapter/'practice-companion.md').exists() else '')
    refs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',combined)
    assert set(refs)=={a['file'] for a in manifest},course['title']
    for asset in manifest:
        picture=chapter/asset['file'];assert picture.exists() and hashlib.sha256(picture.read_bytes()).hexdigest()==asset['sha256']
    total_images+=len(manifest)
    lead,*chunks=re.split(r'(?=^## )',md,flags=re.M)
    if course['id']=='ess':assert len(chunks)==33
    if course['id'] in ('rules','reports'):assert len(chunks)==8
    toc='<nav aria-label="'+course['title']+' sections">';sections=[]
    for i,chunk in enumerate(chunks,1):
        identifier=f'{course["id"]}-section-{i}';title=chunk.splitlines()[0][3:]
        toc+=f'<a href="#{identifier}">{escape(title)}</a>'
        html=f'<section class="topic" id="{identifier}">'+unique_html(chunk,identifier)+'</section>'
        sections.append(html)
        if course['id'] in ('ess','rules','reports'):
            child_dir='modules' if course['id'] in ('ess','reports') else 'topics'
            module_md=chunk.replace('](images/','](../images/').replace('](practice-companion','](../practice-companion').replace('](videos/','](../videos/')
            (chapter/f'{child_dir}/{i:02d}.md').write_text(module_md)
            module_nav=f'<p><a href="../index.html#{course["id"]}-section-{i}">All course topics</a> · <a href="../practice-companion.html">Practice companion</a></p>'
            (chapter/f'{child_dir}/{i:02d}.html').write_text(page(title,module_nav+unique_html(module_md,'individual-'+identifier),'../../../'))
    toc+='</nav>'
    chapter_body='<div class="status">'+escape(course['status'])+'</div>'+unique_html(lead,course['id']+'-lead')+toc+search_ui('Search this course')+''.join(sections)+search_script
    if course['id']=='ess':
        roadmap='## Essentials source depth\n\n| Module | Title | Source basis |\n| --- | --- | --- |\n'
        for m in essentials['modules']:roadmap+=f'| {m["number"]} | [{m["title"]}](modules/{m["number"]:02d}.html) | '+('Caption-search and handouts' if m['number'] in captions else 'Handout-based; full narration unreviewed')+' |\n'
        chapter_body=chapter_body.replace(search_script,unique_html(roadmap,'ess-roadmap')+search_script)
    (chapter/'index.html').write_text(page(course['title']+' — Study Notes',chapter_body,'../../'))
    for section in sections:
        def localize(match):
            key,value=match.groups()
            if value.startswith(('#','https:','http:','mailto:')):return match[0]
            return f'{key}="courses/{course["directory"]}/{value}"'
        all_sections.append(re.sub(r'(href|src)="([^"]+)"',localize,section))

practice_counts={}
for course in courses:
    chapter=study/'courses'/course['directory']
    if not (chapter/'practice-sections.json').exists():continue
    practice=json.loads((chapter/'practice-sections.json').read_text())
    practice_counts[course['id']]=len(practice)
    practice_lead=(chapter/'practice-companion.md').read_text().split('\n## ')[0]
    practice_nav='<nav aria-label="Exercise sections">'+''.join(f'<a href="#{p["id"]}">{escape(p["title"])}</a>' for p in practice)+'</nav>'
    practice_body=unique_html(practice_lead,'practice-lead')+practice_nav+search_ui('Filter exercises by name or learning summary')
    for p in practice:
        practice_body+=f'<section class="topic" id="{p["id"]}">'+unique_html(p['markdown'],p['id'])+'</section>'
    (chapter/'practice-companion.html').write_text(page(course['title']+' — Exercise Companion',practice_body+search_script,'../../'))

report=['# Coverage and Missing Material','','**The Engineer learning path remains incomplete.** Introduction has twelve topic notes, Essentials has notes for all 33 numbered teaching modules, Rules / Scripts / API has notes for all eight internal topics, and Custom Reports has notes for all eight numbered modules. The remaining teaching courses are separate work. The path lists five teaching courses (60 hours 30 minutes displayed) plus two certification exam entries.','','## Course status','','| Course | Coverage |','| --- | --- |']
for e in path['entries']:report.append(f'| {e["title"]} | {e.get("capture_status","Exam content excluded")} |')
report+=['','## IdentityIQ Introduction','','All twelve topic bodies and the listed expanded interactions were read. Sixty-two original inline image files are included. Five demonstrations remain unsaved/untranscribed: Access Request (Topic 5), Detective and Preventative Policy Usage (Topic 8), and Identity Search and Reports (Topic 9). Five poster backgrounds also remain unsaved. Exact paths and interaction coverage are in [Introduction coverage](courses/01-introduction/coverage.json).','','## IdentityIQ Essentials — all 33 modules','','Each numbered module has substantive English paraphrased notes. All 429 nonblank presentation pages appear in module order, retaining original English diagrams, flows, interface examples, forms and icons. The practice companion groups all 257 exercise-guide pages by their related exercise, reference section or appendix. The two original PDFs remain unchanged. Thirty-two blank slide separator pages are omitted from the reading flow but retained in the original slide PDF.','','### Source depth by module','','Modules 1–7 incorporate accessible player caption-search results and handouts. **Modules 8–33 are supported by their official slides and related exercise-guide material; their full video narration has not been reviewed.** Searchable captions may contain duplicate or formatting artifacts and are not certified word-perfect transcripts. Uncaptioned visual changes can be missing even where caption text was reviewed.','','Illustrations are original PDF pages rendered to PNG, not extracted video frames. All supplied handout illustrations are represented at that page level; this is not proof that every changing frame or video-only graphic is saved. Full videos, animations and interactive knowledge-check execution are not archived.','','### Exercises and appendix','','All original guide pages, including the appendix, are available in the linked practice companion. Rewritten summaries connect them to modules. Apart from the previously detailed Exercise 1 rewrite, exact low-level fields and command sequences are retained on the original pages rather than comprehensively rephrased line by line. The appendix procedures are preserved, but not independently executed or validated for other environments.','','No VM service was stopped, identity terminated, permission changed, file uploaded to IdentityIQ, access review submitted or lab reset performed. This edition records instructions; it is not evidence that practical work or the LMS is complete. The separate Accessing the Virtual Machine PDF lesson and My lab interface remain uncaptured.','','### Version and numbering differences','','The exercise guide identifies IdentityIQ 8.2b / 2021; some slides use 8.1 and 2020 examples. Platform lists, defaults and limits are retained as course-version context. The slides spell Accelerator Park where narration says Accelerator Pack. Module 6\'s player heading says Product Architecture while navigation/narration say Installation. The Create Identity practice is called Exercise 6 in the slides and Exercise 4.7 in the guide; this book uses the verified PDF pages 220–225. No missing Exercise 4.6 has been invented.','','See [Essentials notes](courses/02-essentials/notes.md), [the full practice companion](courses/02-essentials/practice-companion.html), [detailed evidence record](courses/02-essentials/coverage.json), and [per-topic/module coverage CSV](lesson-coverage.csv).','','## Rules, Scripts, and API','','All eight written topic bodies were read. The four workflow carousel panels and all three performance tabs were expanded into the notes. Forty-two original inline images, nine original MP4 videos and all 37 exercise-guide pages are saved. The original exercise PDF and course artifact ZIP are retained unchanged.','','The nine demonstrations are available for offline playback, but their narration has not been fully transcribed or reviewed frame by frame. This is especially relevant to Object Model, whose four demonstrations carry much of its detailed teaching. The written notes are a companion to those saved videos.','','Code examples are explanatory and were not executed in an IdentityIQ instance. No rule import/execution, capability grant, access request, service change or review decision was performed. The VM-access lesson, My lab interface, linked external documentation and separate wrap-up page remain uncaptured. The separate Answer Key PDF and supplied solution files were not used to generate the notes.','','See [Rules / Scripts / API notes](courses/03-rules-scripts-api/notes.md), [its exercise companion](courses/03-rules-scripts-api/practice-companion.html), and [the exact coverage report](courses/03-rules-scripts-api/coverage.json).','','## IdentityIQ Custom Reports','','Notes cover all eight numbered modules using the official 75-page presentation deck and 39-page exercise guide. Original slide and guide PDFs, diagrams and page images are not reproduced; references point back to SailPoint Course Files.','','The introduction objectives, audience, prerequisites, lesson list and navigation were inspected in the Storyline player. Full narration, audio, animation and changing demonstration states were not archived or transcribed. The presentation deck begins with Module 2; unique introduction-player graphics are not separately saved. The SVG media-export failure and observed image path are recorded in its coverage JSON.','','The guide says it was developed/verified with IdentityIQ 8.1p1; examples are historical course material. VM starter files, the separate VM-access lesson, My lab interface, external references and wrap-up material remain uncaptured. No report execution, schedule, import, capability change, review or VM operation was performed. The separate Answer Key was not used.','','See [Custom Reports notes](courses/04-custom-reports/notes.md), [the exercise companion](courses/04-custom-reports/practice-companion.html), and [exact coverage record](courses/04-custom-reports/coverage.json).','','## Other gaps and restrictions','','Advanced Provisioning and Workflows was gated on completion of an accepted Essentials course during the prior inspection. Preparing study notes does not satisfy the LMS prerequisite. Only its visible outline has been recorded and no restriction was bypassed.','','Certification exam questions/answers are excluded; no attempt was submitted. Separate course Answer Key PDFs were not used. External linked references, current support matrices and software downloads have not been comprehensively archived.','','The full internal lesson total across all five courses is unverified. Outer numbered modules and internal SCORM topics are different levels and must not be combined into a purported complete lesson count. The reader supplies a continuous offline reading layout rather than an exact LMS screen reproduction.']
(study/'coverage-report.md').write_text('\n'.join(report)+'\n')
(study/'coverage-report.html').write_text(page('Coverage and Missing Material',render('\n'.join(report))))
nav='<nav aria-label="Courses"><a href="courses/01-introduction/index.html">Introduction: 12 topics</a><a href="courses/02-essentials/index.html">Essentials: all 33 numbered modules</a><a href="courses/02-essentials/practice-companion.html">Essentials practice companion: all 257 guide pages</a><a href="courses/03-rules-scripts-api/index.html">Rules, Scripts, and API: all eight topics, illustrations and nine videos</a><a href="courses/04-custom-reports/index.html">Custom Reports: all eight numbered modules and exercise companion</a><a href="coverage-report.html">Source depth and missing material</a></nav>'
heading='<h1>Identity Security Engineer, IdentityIQ</h1><div class="status"><strong>Essentials: 33 modules. Rules / Scripts / API: eight topics. Custom Reports: eight modules.</strong><br>Essentials retains 686 handout illustrations. Rules / Scripts / API adds 79 illustrations and nine original videos. Custom Reports adds rewritten explanations and seven exercise summaries; original materials remain on SailPoint. Video transcript gaps are documented. The broader Engineer path remains incomplete.</div><p>English study explanations in course order. Introduction adds 12 topics and 62 original inline images. Select an illustration to open its full local image. The saved notes, handouts and illustrations work offline.</p>'
(study/'index.html').write_text(page('IdentityIQ Engineer — Learning Notes',heading+nav+search_ui('Search all available module notes')+''.join(all_sections)+search_script))
records=[]
for t in intro_topics:records.append({'course':'IdentityIQ Introduction','level':'internal topic','number':t['number'],'title':t['title'],'notes_status':t['notes_status'],'source_basis':'Original topic body and listed interactions','media_status':f'{t["image_files"]} inline images; '+('video gap' if t['video_gap'] else 'see coverage record')})
for m in essentials['modules']:records.append({'course':'IdentityIQ Essentials','level':'numbered teaching module','number':m['number'],'title':m['title'],'notes_status':m['notes_status'],'source_basis':m['source_basis'],'media_status':'Original slide illustrations and related practice pages; full audiovisual archive not saved'})
for topic in path['entries'][3]['internal_topics']:
    records.append({'course':'IdentityIQ Rules, Scripts, and API','level':'internal topic','number':topic['number'],'title':topic['title'],'notes_status':topic['notes_status'],'source_basis':topic['source_basis'],'media_status':topic['video_status']})
for module in path['entries'][4]['modules']:
    records.append({'course':'IdentityIQ Custom Reports','level':'numbered teaching module','number':module['number'],'title':module['title'],'notes_status':module['notes_status'],'source_basis':module['source_basis'],'media_status':'Original PDF pages/images not reproduced; full narration and player-state archive not captured'})
(study/'lesson-coverage.json').write_text(json.dumps(records,indent=2)+'\n')
with (study/'lesson-coverage.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(records[0]),lineterminator="\n");writer.writeheader();writer.writerows(records)
(ROOT/'capture-progress.json').write_text(json.dumps({'edition':'Custom Reports added','verified_date':'2026-11-16','path_complete':False,'teaching_courses':5,'courses_with_some_notes':4,'introduction_topics_with_notes':12,'essentials_modules_with_notes':sorted(processed),'essentials_pending_numbered_modules':[],'essentials_full_audiovisual_capture_complete':False,'essentials_caption_search_reviewed_modules':sorted(captions),'essentials_full_narration_review_pending_modules':list(range(8,34)),'custom_reports_modules_with_notes':list(range(1,9)),'custom_reports_full_audiovisual_capture_complete':False,'rules_api_topics_with_notes':list(range(1,9)),'rules_api_videos_saved':9,'rules_api_videos_fully_transcribed':0,'saved_image_files':total_images,'image_breakdown':{'introduction_inline_originals':62,'essentials_slide_page_renders':429,'essentials_guide_page_renders':257,'rules_api_inline_originals':42,'rules_api_guide_page_renders':37,'custom_reports_slide_page_renders':0,'custom_reports_guide_page_renders':0},'official_essentials_handouts_saved':2,'next_course':'Advanced Provisioning and Workflows (LMS prerequisite gated during prior inspection)','restricted_course':'Advanced Provisioning and Workflows','restriction':'Accepted Essentials completion is an LMS prerequisite, not satisfied by compiling study notes'},indent=2)+'\n')
print(json.dumps({'introduction_topics':12,'essentials_modules':len(processed),'essentials_pending_numbered_modules':0,'saved_images':total_images,'practice_sections':practice_counts,'coverage_rows':len(records)}))
