<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Python Course • README</title>
  <meta name="description" content="Python Course landing page with book info" />
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#9aa4b2;
      --accent:#7c3aed;
      --accent-2:#06b6d4;
      --glass: rgba(255,255,255,0.03);
      --radius:16px;
      --mono: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", "Courier New", monospace;
      color-scheme: dark;
    }

    /* Reset-ish */
    *{box-sizing:border-box}
    html,body{height:100%}
    body{
      margin:0;
      font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: radial-gradient(1200px 600px at 10% 10%, rgba(124,58,237,0.09), transparent),
                  linear-gradient(180deg, rgba(255,255,255,0.01), transparent 20%),
                  var(--bg);
      color:#e6eef6;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
      line-height:1.45;
      padding:32px;
    }

    .wrap{
      max-width:1100px;
      margin:0 auto;
      display:grid;
      grid-template-columns: 1fr 360px;
      gap:28px;
    }

    /* Card */
    .card{
      background: linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border-radius: var(--radius);
      padding:24px;
      box-shadow: 0 6px 24px rgba(2,6,23,0.6);
      border: 1px solid rgba(255,255,255,0.03);
    }

    header.course-head{
      display:flex;
      gap:16px;
      align-items:center;
      margin-bottom:12px;
    }
    .logo{
      width:72px;
      height:72px;
      border-radius:12px;
      display:grid;
      place-items:center;
      flex:0 0 72px;
      background: linear-gradient(135deg, rgba(124,58,237,0.12), rgba(6,182,212,0.08));
      border:1px solid rgba(255,255,255,0.03);
    }
    .logo svg{width:44px;height:44px;opacity:0.95}

    h1{
      font-size:20px;
      margin:0;
      letter-spacing:-0.2px;
    }
    p.lead{
      margin:6px 0 0 0;
      color:var(--muted);
      font-size:14px;
    }

    /* Actions */
    .actions{
      margin-top:18px;
      display:flex;
      gap:10px;
      flex-wrap:wrap;
    }
    .btn{
      display:inline-flex;
      align-items:center;
      gap:10px;
      padding:10px 14px;
      border-radius:12px;
      font-weight:600;
      font-size:14px;
      text-decoration:none;
      color:white;
      border: none;
      cursor:pointer;
      background: linear-gradient(90deg,var(--accent),#5b21b6);
      box-shadow: 0 6px 18px rgba(92,33,182,0.15), inset 0 -2px 6px rgba(0,0,0,0.2);
    }
    .btn.ghost{
      background:transparent;
      color:var(--muted);
      border:1px solid rgba(255,255,255,0.03);
      box-shadow:none;
      font-weight:600;
    }
    .btn.secondary{
      background: linear-gradient(90deg,var(--accent-2), #0891b2);
    }

    /* Grid content */
    .content-section{
      margin-top:20px;
    }
    .section-title{
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:12px;
      margin-bottom:10px;
    }
    .section-title h2{
      margin:0;
      font-size:15px;
    }
    .muted{color:var(--muted); font-size:14px}

    ul.syllabus{
      list-style:none;
      padding:0;
      margin:8px 0 0 0;
      display:grid;
      gap:8px;
    }
    ul.syllabus li{
      background:linear-gradient(180deg, rgba(255,255,255,0.01), transparent);
      padding:10px 12px;
      border-radius:10px;
      border:1px solid rgba(255,255,255,0.02);
      display:flex;
      justify-content:space-between;
      align-items:center;
      font-weight:600;
      font-size:14px;
    }
    ul.syllabus li .small{font-weight:500;font-size:13px;color:var(--muted)}

    /* Right column */
    .side{
      position:sticky;
      top:32px;
      height:fit-content;
      align-self:start;
    }
    .book-cover{
      height:200px;
      border-radius:12px;
      background: linear-gradient(135deg, rgba(124,58,237,0.18), rgba(6,182,212,0.12));
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:800;
      font-size:22px;
      color:white;
      letter-spacing:0.6px;
      margin-bottom:12px;
      border:1px solid rgba(255,255,255,0.03);
    }
    .meta{
      display:flex;
      gap:10px;
      margin-bottom:12px;
      flex-wrap:wrap;
    }
    .chip{
      background:var(--glass);
      border:1px solid rgba(255,255,255,0.03);
      padding:8px 10px;
      border-radius:999px;
      font-size:13px;
      color:var(--muted);
      display:inline-flex;
      gap:8px;
      align-items:center;
    }

    /* code block */
    pre.code{
      background: #01040a;
      padding:14px;
      border-radius:10px;
      overflow:auto;
      font-family: var(--mono);
      font-size:13px;
      color:#dbeafe;
      line-height:1.5;
      border:1px solid rgba(255,255,255,0.02);
      box-shadow: inset 0 -6px 20px rgba(0,0,0,0.5);
    }
    pre.code .kw{ color:#c084fc; font-weight:700 } /* keywords */
    pre.code .str{ color:#60a5fa } /* strings */
    pre.code .cm{ color:#94a3b8 } /* comment */

    /* footer */
    footer{
      margin-top:18px;
      display:flex;
      justify-content:space-between;
      align-items:center;
      gap:12px;
      color:var(--muted);
      font-size:13px;
    }

    /* responsive */
    @media (max-width:980px){
      .wrap{ grid-template-columns: 1fr; padding-bottom:40px }
      .side{ position:static }
    }

    /* subtle hover states */
    .btn:hover{ transform:translateY(-2px) }
    ul.syllabus li:hover{ transform:translateY(-3px); transition:all .12s ease; }
  </style>
</head>
<body>
  <main class="wrap" role="main">
    <section class="card" aria-labelledby="course-title">
      <header class="course-head">
        <div class="logo" aria-hidden="true">
          <!-- small Python-ish glyph -->
          <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" >
            <rect x="2" y="2" width="20" height="20" rx="5" fill="url(#g)"/>
            <defs>
              <linearGradient id="g" x1="0" x2="1">
                <stop offset="0" stop-color="#7c3aed"/>
                <stop offset="1" stop-color="#06b6d4"/>
              </linearGradient>
            </defs>
            <path d="M7 7h6v2H9v2H7V7z" fill="white" opacity=".95"/>
            <path d="M17 17h-6v-2h4v-2h2v4z" fill="white" opacity=".95"/>
          </svg>
        </div>

        <div>
          <h1 id="course-title">Python Course • README</h1>
          <p class="lead">Beginner → Intermediate course with hands-on projects. Includes an accompanying book and exercises.</p>

          <div class="actions" role="group" aria-label="Primary actions">
            <a class="btn" href="#getting-started" title="Getting started">🚀 Get Started</a>
            <a class="btn secondary" href="./book.pdf" title="Open the book (PDF)" download>📘 Download Book</a>
            <a class="btn ghost" href="https://github.com/" target="_blank" rel="noopener">⭐ Star Repo</a>
          </div>
        </div>
      </header>

      <div class="content">
        <div class="content-section">
          <div class="section-title">
            <h2>About this course</h2>
            <span class="muted">Duration: 8 weeks • Level: Beginner → Intermediate</span>
          </div>
          <p class="muted">
            This course is structured to build real-world Python skills: fundamentals, data structures, OOP, file I/O,
            web APIs, virtual environments, and small projects to tie everything together. The included book mirrors the lessons and contains extra exercises.
          </p>
        </div>

        <div class="content-section" id="syllabus">
          <div class="section-title">
            <h2>Syllabus</h2>
            <span class="muted">Core lessons & mini-projects</span>
          </div>

          <ul class="syllabus" aria-label="Course syllabus">
            <li><span>Intro & Setup</span> <span class="small">(Install, editors)</span></li>
            <li><span>Variables & Types</span> <span class="small">(Numbers, strings)</span></li>
            <li><span>Control Flow</span> <span class="small">(if, loops)</span></li>
            <li><span>Functions & Modules</span> <span class="small">(def, imports)</span></li>
            <li><span>Data Structures</span> <span class="small">(lists, dicts, sets)</span></li>
            <li><span>File Handling</span> <span class="small">(read/write)</span></li>
            <li><span>OOP Fundamentals</span> <span class="small">(classes)</span></li>
            <li><span>Virtual Envs & Packaging</span> <span class="small">(venv, pip)</span></li>
            <li><span>Final Projects</span> <span class="small">(CLI apps, web scrapers)</span></li>
          </ul>
        </div>

        <div class="content-section" id="sample-code">
          <div class="section-title">
            <h2>Sample snippet</h2>
            <span class="muted">Python example from the book</span>
          </div>

          <pre class="code" aria-label="sample python code"><code>
<span class="cm"># simple function to count words in a file</span>
<span class="kw">def</span> <span class="kw">count_words</span>(path):
    <span class="cm">"""Return number of words in file at path."""</span>
    <span class="kw">with</span> open(path, 'r', encoding='utf-8') <span class="kw">as</span> f:
        text = f.read()
    words = text.split()
    <span class="kw">return</span> len(words)

<span class="kw">if</span> <span class="kw">__name__</span> == '<span class="str">__main__</span>':
    print(count_words('sample.txt'))
          </code></pre>
        </div>

        <div class="content-section" id="getting-started">
          <div class="section-title">
            <h2>Getting started</h2>
            <span class="muted">Clone, install, run</span>
          </div>

          <p class="muted">Quick setup — run these in a terminal:</p>
          <pre class="code"><code>
# clone the repo
git clone https://github.com/your-username/python-course.git
cd python-course

# create and activate venv (macOS / Linux)
python3 -m venv .venv
source .venv/bin/activate

# or (Windows - PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# install dependencies (if any)
pip install -r requirements.txt

# open the book:
# open ./book.pdf in your PDF reader
          </code></pre>
        </div>

        <div class="content-section" id="requirements">
          <div class="section-title">
            <h2>Requirements</h2>
            <span class="muted">What you'll need</span>
          </div>
          <ul class="syllabus" style="grid-template-columns: 1fr 1fr;">
            <li><span>Python 3.8+</span><span class="small">(recommended 3.10+)</span></li>
            <li><span>VS Code / PyCharm</span><span class="small">or your favorite editor</span></li>
            <li><span>Git</span><span class="small">(optional but useful)</span></li>
            <li><span>PDF reader</span><span class="small">for the book</span></li>
          </ul>
        </div>

        <footer>
          <div class="muted">© <span id="year"></span> Your Name • Built with ♥ for learners</div>
          <div class="muted">v1.0 • Last updated: <strong>Oct 03, 2025</strong></div>
        </footer>
      </div>
    </section>

    <aside class="card side" aria-labelledby="book-title">
      <div class="book-cover" id="book-title">PYTHON: HANDS-ON BOOK</div>

      <div class="meta">
        <div class="chip">📚 240 pages</div>
        <div class="chip">🔖 Exercises</div>
        <div class="chip">🛠 Projects</div>
      </div>

      <p class="muted" style="margin-bottom:12px;">
        The companion book mirrors this course and includes extended examples, solutions, and guided projects.
        Use the download button to get the PDF or open it in the browser.
      </p>

      <div style="display:flex;gap:10px;margin-bottom:14px;">
        <a class="btn" href="./book.pdf" download>📘 Download PDF</a>
        <a class="btn ghost" href="./book.pdf" target="_blank" rel="noopener">Open in Browser</a>
      </div>

      <div class="section-title" style="margin-top:6px;">
        <h2>Author</h2>
        <span class="muted">Contact</span>
      </div>

      <p class="muted" style="margin-bottom:8px;">
        <strong>Your Name</strong><br/>
        your.email@example.com
      </p>

      <div style="display:flex;gap:8px;margin-top:6px;">
        <a class="chip" href="https://github.com/your-username" target="_blank" rel="noopener">GitHub</a>
        <a class="chip" href="https://linkedin.com/in/yourprofile" target="_blank" rel="noopener">LinkedIn</a>
      </div>

      <div style="margin-top:16px">
        <div class="section-title">
          <h2>Quick links</h2>
          <span class="muted">resources</span>
        </div>
        <ul style="list-style:none;padding:0;margin:6px 0 0 0;display:grid;gap:8px;">
          <li><a class="chip" href="https://docs.python.org/3/" target="_blank" rel="noopener">Python Docs</a></li>
          <li><a class="chip" href="https://realpython.com/" target="_blank" rel="noopener">Real Python</a></li>
          <li><a class="chip" href="https://pypi.org/" target="_blank" rel="noopener">PyPI</a></li>
        </ul>
      </div>
    </aside>
  </main>

  <script>
    // small niceties
    document.getElementById('year').textContent = new Date().getFullYear();

    // keyboard shortcut: press 'b' to open book (convenience)
    window.addEventListener('keydown', function(e){
      if(e.key === 'b' && !e.metaKey && !e.ctrlKey){
        const win = window.open('./book.pdf', '_blank');
        if(win) win.focus();
      }
    });
  </script>
</body>
</html>
