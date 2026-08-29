#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds a single self-contained interactive HTML preview of the whole
WOW website (all pages, client-side routed, images inlined as base64).
Run after build.py: python3 build_preview.py
"""
import importlib.util, base64, os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("wowbuild", os.path.join(HERE, "build.py"))
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

ASSETS = mod.ASSETS

def inline_images(html):
    def repl(m):
        rel = m.group(1)
        path = os.path.join(ASSETS, rel)
        if not os.path.isfile(path):
            return m.group(0)
        ext = rel.split('.')[-1].lower()
        mime = "image/png" if ext == "png" else "image/jpeg"
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        return f'src="data:{mime};base64,{b64}"'
    return re.sub(r'src="assets/([^"]+)"', repl, html)

pages = {
    "index.html": mod.home_body,
    "reizen.html": mod.reizen_body,
    "experience-spain.html": mod.spain_body,
    "experience-italy.html": mod.italy_body,
    "experience-snow.html": mod.snow_body,
    "experience-lisboa.html": mod.lisboa_body,
    "aanmelden-snow-exclusive.html": mod.snow_exclusive_form_body,
    "waarom-wow.html": mod.waarom_body,
    "veiligheid.html": mod.veiligheid_body,
    "over-wow.html": mod.over_body,
    "contact.html": mod.contact_body,
}
titles = {k: k for k in pages}

with open(os.path.join(HERE, "css/style.css"), "r", encoding="utf-8") as f:
    css = f.read()

nav_html = inline_images(mod.header_nav("index.html"))
footer_html = inline_images(mod.footer())
footer_html_clean = footer_html.split('<script src="js/main.js"></script>')[0]

templates = []
for fname, body in pages.items():
    body_inlined = inline_images(body)
    templates.append(f'<template id="tpl-{fname}">{body_inlined}</template>')
templates_html = "\n".join(templates)
json_titles = json.dumps(titles)

html = f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WOW — The Experience Company (live preview)</title>
<style>
{css}
.preview-badge{{position:fixed;left:16px;bottom:16px;z-index:200;background:#0a0a0a;color:#fff;font-size:11px;letter-spacing:1px;padding:8px 14px;border-radius:999px;opacity:.85;font-family:sans-serif;}}
</style>
</head>
<body>
{nav_html}
<main id="app"></main>
{footer_html_clean}
<div class="preview-badge">WOW WEBSITE PREVIEW — alle {len(pages)} pagina's, volledig doorklikbaar</div>

{templates_html}

<script>
const TITLES = {json_titles};
const app = document.getElementById('app');

function initPage() {{
  var hamburger = document.querySelector('.hamburger');
  var mobileMenu = document.querySelector('.mobile-menu');
  var mobileClose = document.querySelector('.mobile-menu-close');
  if (hamburger && mobileMenu) {{
    hamburger.onclick = function () {{ mobileMenu.classList.add('open'); document.body.style.overflow='hidden'; }};
  }}
  if (mobileClose && mobileMenu) {{
    mobileClose.onclick = function () {{ mobileMenu.classList.remove('open'); document.body.style.overflow=''; }};
  }}

  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {{
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (entry) {{
        if (entry.isIntersecting) {{ entry.target.classList.add('in'); io.unobserve(entry.target); }}
      }});
    }}, {{ threshold: 0.12 }});
    revealEls.forEach(function (el) {{ io.observe(el); }});
  }} else {{
    revealEls.forEach(function (el) {{ el.classList.add('in'); }});
  }}

  document.querySelectorAll('.faq-item').forEach(function (item) {{
    var q = item.querySelector('.faq-q');
    var a = item.querySelector('.faq-a');
    if (!q || !a) return;
    q.onclick = function () {{
      var isOpen = item.classList.contains('open');
      var list = item.closest('.faq-list');
      if (list) {{
        list.querySelectorAll('.faq-item.open').forEach(function (openItem) {{
          if (openItem !== item) {{ openItem.classList.remove('open'); openItem.querySelector('.faq-a').style.maxHeight = null; }}
        }});
      }}
      if (isOpen) {{ item.classList.remove('open'); a.style.maxHeight = null; }}
      else {{ item.classList.add('open'); a.style.maxHeight = a.scrollHeight + 'px'; }}
    }};
  }});

  var catButtons = document.querySelectorAll('.faq-cat-btn');
  if (catButtons.length) {{
    catButtons.forEach(function (btn) {{
      btn.onclick = function () {{
        catButtons.forEach(function (b) {{ b.classList.remove('active'); }});
        btn.classList.add('active');
        var cat = btn.getAttribute('data-cat');
        document.querySelectorAll('.faq-item').forEach(function (item) {{
          item.style.display = (cat === 'all' || item.getAttribute('data-cat') === cat) ? '' : 'none';
        }});
      }};
    }});
  }}

  var counters = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window && counters.length) {{
    var counterIo = new IntersectionObserver(function (entries) {{
      entries.forEach(function (entry) {{
        if (entry.isIntersecting) {{ animateCount(entry.target); counterIo.unobserve(entry.target); }}
      }});
    }}, {{ threshold: 0.5 }});
    counters.forEach(function (el) {{ counterIo.observe(el); }});
  }}
  function animateCount(el) {{
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var duration = 1200, startTime = null;
    function step(ts) {{
      if (!startTime) startTime = ts;
      var progress = Math.min((ts - startTime) / duration, 1);
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (progress < 1) window.requestAnimationFrame(step);
    }}
    window.requestAnimationFrame(step);
  }}

  document.querySelectorAll('.lead-form').forEach(function (form) {{
    form.onsubmit = function (e) {{
      e.preventDefault();
      if (!form.checkValidity()) {{ form.reportValidity(); return; }}
      form.style.display = 'none';
      var success = form.parentElement.querySelector('.form-success');
      if (success) success.classList.add('show');
    }};
  }});
}}

function loadPage(name, push) {{
  var tpl = document.getElementById('tpl-' + name);
  if (!tpl) return;
  app.innerHTML = '';
  app.appendChild(tpl.content.cloneNode(true));
  document.querySelectorAll('nav.main-nav a, .mobile-menu a').forEach(function (a) {{
    a.classList.toggle('active', a.getAttribute('href') === name);
  }});
  window.scrollTo(0, 0);
  initPage();
  if (push !== false) history.pushState({{page: name}}, '', '#' + name);
}}

document.addEventListener('click', function (e) {{
  var a = e.target.closest('a');
  if (!a) return;
  var href = a.getAttribute('href');
  if (href && TITLES.hasOwnProperty(href)) {{
    e.preventDefault();
    loadPage(href);
    var mobileMenu = document.querySelector('.mobile-menu');
    if (mobileMenu) {{ mobileMenu.classList.remove('open'); document.body.style.overflow=''; }}
  }}
}});

window.addEventListener('popstate', function (e) {{
  var page = (e.state && e.state.page) || (location.hash ? location.hash.slice(1) : 'index.html');
  loadPage(page, false);
}});

var initial = location.hash ? location.hash.slice(1) : 'index.html';
if (!TITLES.hasOwnProperty(initial)) initial = 'index.html';
loadPage(initial, false);
</script>
</body>
</html>
"""

out_path = "/home/claude/wow-website-preview.html"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)

print("written", out_path, os.path.getsize(out_path))
