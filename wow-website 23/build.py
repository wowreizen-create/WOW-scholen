#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script for WOW — THE EXPERIENCE COMPANY website.
Generates all static HTML pages from shared templates + page content.
Run: python3 build.py
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(ROOT, "assets")

def has_asset(relpath):
    return os.path.isfile(os.path.join(ASSETS, relpath))

def IMG(relpath, alt, cls="", ph_label=None, ph_dark=False, tag_class=""):
    """Return an <img> tag if the asset exists, otherwise an elegant placeholder block."""
    if has_asset(relpath):
        return f'<img src="assets/{relpath}" alt="{alt}" class="{cls}">'
    label = ph_label or alt
    dark = " dark" if ph_dark else ""
    return f'<div class="placeholder-block{dark} {cls}"><span>{label}</span></div>'

SITE_NAME = "WOW — The Experience Company"
CALENDLY = "https://calendly.com/wowreizen/30min"
INSTAGRAM = "https://www.instagram.com/wowreizen"

NAV_ITEMS = [
    ("index.html", "Home"),
    ("reizen.html", "Reizen"),
    ("waarom-wow.html", "Waarom WOW"),
    ("veiligheid.html", "Veiligheid"),
    ("over-wow.html", "Over WOW"),
    ("contact.html", "Contact"),
]

def head(title, description):
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/wow-logo-black.png">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
"""

def nav_link_html(href, label, active):
    cls = ' class="active"' if href == active else ''
    return '<a href="' + href + '"' + cls + '>' + label + '</a>'

def header_nav(active):
    links = "\n      ".join(
        nav_link_html(href, label, active) for href, label in NAV_ITEMS
    )
    mobile_links = "\n      ".join(
        f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS
    )
    return f"""<header>
  <div class="wrap nav-inner">
    <a class="brand" href="index.html">
      <img src="assets/wow-logo-white.png" alt="WOW logo">
    </a>
    <nav class="main-nav">
      {links}
    </nav>
    <div class="nav-right">
      <a class="btn btn-sm" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <button class="hamburger" aria-label="Menu" onclick="document.querySelector('.mobile-menu').classList.add('open');document.body.style.overflow='hidden';">
        &#9776;
      </button>
    </div>
  </div>
</header>

<div class="mobile-menu">
  <div class="mobile-menu-top">
    <img src="assets/wow-logo-white.png" alt="WOW logo">
    <button class="mobile-menu-close" aria-label="Sluiten" onclick="document.querySelector('.mobile-menu').classList.remove('open');document.body.style.overflow='';">&times;</button>
  </div>
  {mobile_links}
  <a class="btn btn-block" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
</div>
"""

def footer():
    return f"""<footer>
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="assets/wow-logo-white.png" alt="WOW logo">
        <p>WOW is geen reisorganisatie die ook schoolreizen doet. WOW komt uit het onderwijs — en combineert onderwijskennis, professionele organisatie, sport &amp; avontuur, veiligheid en persoonlijke groei tot The WOW Experience.</p>
        <div class="footer-social">
          <a href="{INSTAGRAM}" target="_blank" rel="noopener" aria-label="Instagram">IG</a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Navigatie</h4>
        <a href="reizen.html">Reizen</a>
        <a href="waarom-wow.html">Waarom WOW</a>
        <a href="veiligheid.html">Veiligheid</a>
        <a href="over-wow.html">Over WOW</a>
      </div>
      <div class="footer-col">
        <h4>Experiences</h4>
        <a href="experience-spain.html">WOW Espana</a>
        <a href="experience-italy.html">WOW Italia</a>
        <a href="experience-snow.html">WOW in the Snow</a>
        <a href="experience-lisboa.html">WOW Lisboa Super Surf</a>
      </div>
      <div class="footer-col">
        <h4>Contact</h4>
        <a href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking</a>
        <a href="contact.html">Contactformulier</a>
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 WOW Reizen — The Experience Company. Sport, Cultuur en Plezier.</span>
      <span>Deze site is een ontwerp/opzet klaar voor verdere invulling (CMS, echte cijfers en testimonials).</span>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""

def sticky_cta(text="Plan een kennismaking"):
    return f"""<div class="sticky-cta">
  <a class="btn btn-block" href="{CALENDLY}" target="_blank" rel="noopener">{text} &rarr;</a>
</div>
"""

def page(filename, title, description, active, body_html, sticky=True):
    html = head(title, description) + header_nav(active) + body_html
    if sticky:
        html += sticky_cta()
    html += footer()
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# =========================================================================
# HOME
# =========================================================================
home_body = f"""
<section class="hero-full">
  <div class="hero-media">
    {IMG("wow-hero-palamos-sup.jpg", "WOW instructeur begeleidt scholieren met suppboard, bodyboard en padelracket in Palamos, Spanje")}
  </div>
  <div class="wrap hero-content">
    <span class="kicker">Sport &middot; Cultuur &middot; Fun</span>
    <h1 class="h1-sm">WOW is een onderwijs leerplatform met <em>het allerbeste reisconcept voor scholen</em>.</h1>
    <p class="hero-sub">Professioneel georganiseerd vanuit jarenlange ervaring in het onderwijs. WOW combineert onderwijs, experience, sport, persoonlijke groei en veiligheid tot &eacute;&eacute;n onvergetelijke schoolreis.</p>
    <div class="hero-cta-row">
      <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <a class="btn btn-outline btn-lg" href="reizen.html">Ontdek WOW &rarr;</a>
    </div>
  </div>
  <div class="hero-scroll-tag">Dit is geen gewone schoolreis &middot; dit is WOW</div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Waarom scholen kiezen voor WOW</span>
      <h2>Meer beleving voor leerlingen. Minder organisatie voor school.</h2>
    </div>
    <div class="usp-grid">
      <a href="waarom-wow.html" class="usp-card" style="color:inherit;">
        <span class="num">01</span>
        <h3>Ontzorgen</h3>
        <p>Wij regelen. Jullie begeleiden. Vervoer, accommodatie, activiteiten, planning en veiligheid &mdash; volledig uit handen genomen.</p>
      </a>
      <a href="waarom-wow.html" class="usp-card" style="color:inherit;">
        <span class="num">02</span>
        <h3>Onderwijs &amp; leerplatform</h3>
        <p>Studenten leren, leerlingen groeien. WOW verbindt scholieren, onderwijs en toekomstige sportprofessionals.</p>
      </a>
      <a href="veiligheid.html" class="usp-card" style="color:inherit;">
        <span class="num">03</span>
        <h3>Veiligheid</h3>
        <p>Vrijheid binnen duidelijke kaders. Maximale beleving, duidelijke afspraken, professionele verantwoordelijkheid.</p>
      </a>
      <a href="waarom-wow.html" class="usp-card" style="color:inherit;">
        <span class="num">04</span>
        <h3>Slim met budget</h3>
        <p>Maximale kwaliteit en beleving binnen een verantwoord schoolbudget.</p>
      </a>
    </div>
  </div>
</section>

<section class="experiences-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">The WOW Experiences</span>
      <h2>Choose your WOW.</h2>
      <p>Vier bestemmingen. E&eacute;n gedachte: leerlingen iets laten beleven dat ze bijblijft.</p>
    </div>
    <div class="exp-grid exp-grid-4">
      <a class="exp-card" href="experience-spain.html">
        {IMG("wow-hero-palamos.jpg", "WOW Espana — Palamos en Barcelona")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127466;&#127480;</span>
          <span class="exp-kicker">WOW Espana</span>
          <h3>Palam&oacute;s &amp; Barcelona</h3>
          <p>Zee. Sport. SUP. Snorkelen. Padel. Cultuur. Barcelona.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Espana &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-italy.html">
        {IMG("italy-milaan-fontein.jpg", "WOW groep bij de fontein in Milaan")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127470;&#127481;</span>
          <span class="exp-kicker">WOW Italia</span>
          <h3>Milaan &middot; Veneti&euml; &middot; Caorle</h3>
          <p>Sport. Cultuur. Strand. Italiaanse beleving.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Italia &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-snow.html">
        {IMG("snow-goggles-groep.jpg", "WOW groep met skibril tijdens WOW in the Snow")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127956;</span>
          <span class="exp-kicker">WOW in the Snow</span>
          <h3>Zell am See &amp; Kaprun</h3>
          <p>Wintersport. Bergen. Uitdaging. Vrijheid. Samen beleven.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW in the Snow &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-lisboa.html">
        {IMG("founder-surf-test.jpg", "Surfen aan de Atlantische kust bij Ericeira, Portugal")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127477;&#127481;</span>
          <span class="exp-kicker">WOW Lisboa Super Surf</span>
          <h3>Ericeira &amp; Lissabon</h3>
          <p>Surf. Culture. Freedom. Connection.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Lisboa Super Surf &rarr;</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-media">
        {IMG("wow-hero-palamos.jpg", "WOW ontzorgt de hele organisatie van de schoolreis", ph_label="Foto volgt")}
      </div>
      <div class="split-text">
        <span class="kicker">Volledige ontzorging</span>
        <h2>Jullie de leerlingen. Wij de organisatie.</h2>
        <p>WOW neemt zoveel mogelijk organisatie uit handen: vervoer, accommodatie, activiteiten, lokale partners, planning, draaiboek, praktische voorbereiding, communicatie, begeleiding, veiligheidsorganisatie en ondersteuning tijdens de reis.</p>
        <p><strong>Minder organiseren. Minder werkdruk. Meer aandacht voor leerlingen.</strong></p>
        <div class="flow-diagram" style="justify-content:flex-start;margin:32px 0 0;">
          <span class="flow-pair"><span class="flow-step">Vervoer</span><span class="flow-arrow">&rarr;</span></span>
          <span class="flow-pair"><span class="flow-step">Accommodatie</span><span class="flow-arrow">&rarr;</span></span>
          <span class="flow-pair"><span class="flow-step">Activiteiten</span><span class="flow-arrow">&rarr;</span></span>
          <span class="flow-step">Veiligheid</span>
        </div>
        <a class="link-arrow" href="waarom-wow.html" style="margin-top:26px;display:inline-flex;">Ontdek hoe WOW ontzorgt &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="effect-section reveal">
  <div class="wrap">
    <span class="kicker" style="text-align:center;display:block;">The WOW Effect</span>
    <div class="effect-headline">Een schoolreis gaat niet alleen over <span class="coral">waar je bent geweest.</span><br>Maar ook over <span class="coral">wie je onderweg wordt.</span></div>
    <p class="effect-sub">Zelfvertrouwen. Zelfstandigheid. Samenwerking. Nieuwe vriendschappen. Veerkracht.</p>
    <div class="effect-story">
      <p>Een leerling twijfelt. &ldquo;Dit kan ik niet.&rdquo; Toch stapt hij op die SUP. Hij valt. Probeert opnieuw. En even later staat hij. Trots.</p>
      <p class="payoff">Dat moment? Dat is WOW.</p>
    </div>
    <div class="effect-tags">
      <span>Zelfvertrouwen</span><span>Vriendschap</span><span>Doorzetten</span><span>Samenwerken</span><span>Dankbaarheid</span><span>Uitdaging</span><span>Verbinding</span>
    </div>
  </div>
</section>

<section class="stats-band reveal">
  <div class="wrap">
    <div class="stats-grid">
      <div><strong data-count="1000" data-suffix="+">1000+</strong><span>Begeleide leerlingen</span></div>
      <div><strong data-count="4" data-suffix="">4</strong><span>WOW bestemmingen</span></div>
      <div><strong data-count="160" data-suffix="">160</strong><span>Maximale groepsgrootte</span></div>
      <div><strong>24/7</strong><span>Ondersteuning tijdens de reis</span></div>
    </div>
  </div>
</section>

<section class="process-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Hoe werkt WOW?</span>
      <h2>Van eerste gesprek naar WOW.</h2>
    </div>
    <div class="process-grid">
      <div class="process-step"><span class="step-num">01</span><h3>Kennismaken</h3><p>We bespreken jullie school, leerlingen en wensen.</p></div>
      <div class="process-step"><span class="step-num">02</span><h3>Samenstellen</h3><p>We cre&euml;ren een Experience die bij jullie school past.</p></div>
      <div class="process-step"><span class="step-num">03</span><h3>Voorbereiden</h3><p>Programma, vervoer, accommodatie, communicatie en veiligheid worden geregeld.</p></div>
      <div class="process-step"><span class="step-num">04</span><h3>Experience</h3><p>Leerlingen beleven hun WOW.</p></div>
      <div class="process-step"><span class="step-num">05</span><h3>Impact</h3><p>Ze komen terug met verhalen, verbindingen en ervaringen die blijven hangen.</p></div>
    </div>
    <div class="center" style="margin-top:46px;">
      <a class="btn btn-outline-dark btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Start met een kennismaking &rarr;</a>
    </div>
  </div>
</section>

<section class="stories-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">WOW Stories</span>
      <h2>Echte momenten tijdens WOW-reizen</h2>
      <p>Korte, authentieke verhalen &mdash; klaar om aangevuld te worden met echte foto&rsquo;s en quotes per reis.</p>
    </div>
    <div class="stories-grid">
      <div class="story-card">
        <div class="story-media">{IMG("founder-surf-test.jpg", "WOW Story — Zelfvertrouwen")}<span class="story-theme">Zelfvertrouwen</span></div>
        <div class="story-body">
          <h3>&ldquo;Dit kan ik niet&rdquo; &mdash; tot ze het wel kon</h3>
          <p>Plek voor een echt verhaal van een leerling die een grens verlegde tijdens een WOW-experience.</p>
          <div class="story-quote">Placeholder &mdash; quote volgt</div>
        </div>
      </div>
      <div class="story-card">
        <div class="story-media">{IMG("italy-venetie-groep.jpg", "WOW Story — Vriendschap")}<span class="story-theme">Vriendschap</span></div>
        <div class="story-body">
          <h3>Onverwachte vriendschappen</h3>
          <p>Plek voor een verhaal over groepsdynamiek en nieuwe verbindingen tussen leerlingen.</p>
          <div class="story-quote">Placeholder &mdash; quote volgt</div>
        </div>
      </div>
      <div class="story-card">
        <div class="story-media">{IMG("snow-groep.jpg", "WOW Story — Doorzetten")}<span class="story-theme">Doorzetten</span></div>
        <div class="story-body">
          <h3>Opstaan na de val</h3>
          <p>Plek voor een verhaal over doorzettingsvermogen tijdens sportactiviteiten.</p>
          <div class="story-quote">Placeholder &mdash; quote volgt</div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="testimonials-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Social proof</span>
      <h2>Wat scholen en leerlingen zeggen</h2>
      <p>Echte reacties van ouders en leerlingen &mdash; we verzinnen niets.</p>
    </div>
    <div class="testi-grid">
      <div class="testi-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p>&ldquo;Onze zoon is mee geweest met WOW in the Snow!! Hij heeft het waanzinnig naar zijn zin gehad. Allemaal mooie verhalen, een top accommodatie evenals het eten. Met Kaprun als hoogtepunt. Dankjewel voor de goede organisatie!!!&rdquo;</p>
        <div class="testi-who"><div class="testi-avatar">MR</div><div><strong>Marc Riebroek</strong><span>Ouder van een deelnemer &middot; WOW in the Snow</span></div></div>
      </div>
      <div class="testi-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p>&ldquo;Wij hebben als ouders mee kunnen genieten van een fantastische reis naar Itali&euml; via goed gedoseerde updates en filmpjes. De reis was heel goed georganiseerd en de begeleiding was positief, betrokken en betrouwbaar. Deze reis is zeker aan te raden!&rdquo;</p>
        <div class="testi-who"><div class="testi-avatar">MS</div><div><strong>Meindert Spijksma</strong><span>Ouder van een deelnemer &middot; WOW Italia</span></div></div>
      </div>
      <div class="testi-card">
        <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p>&ldquo;Het was echt een geweldige reis met een fantastische leider maar vooral leuke momenten en veel nieuwe vrienden gemaakt.&rdquo;</p>
        <div class="testi-who"><div class="testi-avatar">DJ</div><div><strong>Dane Jol</strong><span>Leerling</span></div></div>
      </div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Good Practice &middot; Evaluatierapport WOW schoolreis 2026</span>
      <h2>Een reis vol vrijheid &eacute;n groei. Onvergetelijke herinneringen.</h2>
      <p>Na afloop van de reis hebben alle leerlingen een uitgebreide evaluatie ingevuld. De resultaten laten een prachtig beeld zien van hoe de reis is ervaren. De algemene conclusie is overduidelijk: leerlingen hebben een geweldige week gehad.</p>
      <div class="badge-row" style="justify-content:center;">
        <span class="badge">104 leerlingen</span>
        <span class="badge">7 studenten</span>
        <span class="badge">7 docenten</span>
      </div>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(4,1fr);">
      <div class="price-card"><div class="amount">9.2</div><p>Groepssfeer</p></div>
      <div class="price-card"><div class="amount">9.4</div><p>Vrijheid &amp; beleving</p></div>
      <div class="price-card"><div class="amount">8.8</div><p>Activiteiten</p></div>
      <div class="price-card"><div class="amount">9.1</div><p>Begeleiding</p></div>
    </div>
    <div class="testi-card" style="max-width:760px;margin:32px auto 0;">
      <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p>&ldquo;Onze beste schoolreis tot nu toe!! Een fantastische, goed georganiseerde reis met hele gave activiteiten, veel keuze en vrijheid. Begeleid door gave studenten van de sportacademie HALO. Mega gave herinneringen.&rdquo;</p>
      <div class="testi-who"><div class="testi-avatar">&#9733;</div><div><strong>Uit de evaluatie</strong><span>Leerling &middot; WOW schoolreis 2026</span></div></div>
    </div>
    <div class="badge-row" style="justify-content:center;margin-top:28px;">
      <span class="badge">Gezellig</span><span class="badge">Ontspannen</span><span class="badge">Vrij</span><span class="badge">Goed georganiseerd</span><span class="badge">Onvergetelijk</span>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW schoolreis")}</div>
  <div class="wrap final-content">
    <h2>De volgende schoolreis mag een WOW worden.</h2>
    <p>Ontdek wat we voor jullie leerlingen kunnen cre&euml;ren.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>

<section class="reveal partner-logos">
  <div class="wrap partner-logos-row">
    <a href="https://vzr-garant.nl/" target="_blank" rel="noopener" title="VZR Garant">
      {IMG("logo-vzr-garant.png", "VZR Garant &mdash; garantiefonds voor reizen")}
    </a>
    <a href="https://www.vvkr.nl/" target="_blank" rel="noopener" title="VvKR &mdash; Vereniging van Kleinschalige Reisorganisaties">
      {IMG("logo-vvkr.png", "VvKR &mdash; Vereniging van Kleinschalige Reisorganisaties")}
    </a>
  </div>
</section>
"""
page("index.html", "WOW — The Experience Company | Onvergetelijke schoolreizen",
     "WOW organiseert unieke buitenlandse schoolreizen voor middelbare scholen. Sport, cultuur, persoonlijke groei en veiligheid — professioneel georganiseerd vanuit het onderwijs.",
     "index.html", home_body)

print("Home done.")

# =========================================================================
# REIZEN (overview)
# =========================================================================
reizen_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW reizen overzicht")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; Reizen</div>
    <span class="kicker">The WOW Experiences</span>
    <h1>Choose your WOW.</h1>
    <p class="hero-sub">Vier bestemmingen, opgebouwd rond &eacute;&eacute;n gedachte: leerlingen iets laten beleven dat ze bijblijft. Elke Experience combineert sport, cultuur en fun &mdash; professioneel georganiseerd van A tot Z.</p>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="exp-grid exp-grid-4">
      <a class="exp-card" href="experience-spain.html">
        {IMG("wow-hero-palamos.jpg", "WOW Espana — Palamos en Barcelona")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127466;&#127480;</span>
          <span class="exp-kicker">WOW Espana</span>
          <h3>Palam&oacute;s &amp; Barcelona</h3>
          <p>Zee, SUP, snorkelen, padel, tennis, beachvolleybal en een dagtrip naar Barcelona.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Espana &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-italy.html">
        {IMG("italy-milaan-fontein.jpg", "WOW groep bij de fontein in Milaan")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127470;&#127481;</span>
          <span class="exp-kicker">WOW Italia</span>
          <h3>Milaan &middot; Veneti&euml; &middot; Caorle</h3>
          <p>Sport, cultuur, strand en Italiaanse beleving in &eacute;&eacute;n reis.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Italia &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-snow.html">
        {IMG("snow-goggles-groep.jpg", "WOW groep met skibril tijdens WOW in the Snow")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127956;</span>
          <span class="exp-kicker">WOW in the Snow</span>
          <h3>Zell am See &amp; Kaprun</h3>
          <p>Skien, snowboarden en samen de bergen ontdekken in Oostenrijk.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW in the Snow &rarr;</span>
        </div>
      </a>
      <a class="exp-card" href="experience-lisboa.html">
        {IMG("founder-surf-test.jpg", "Surfen aan de Atlantische kust bij Ericeira, Portugal")}
        <div class="exp-overlay"></div>
        <div class="exp-body">
          <span class="exp-flag">&#127477;&#127481;</span>
          <span class="exp-kicker">WOW Lisboa Super Surf</span>
          <h3>Ericeira &amp; Lissabon</h3>
          <p>5-daagse surfreis: Ericeira, Praia da Foz do Lizandro en een dagtrip Lissabon.</p>
          <span class="link-arrow" style="color:#fff;border-color:#e6432f;">Ontdek WOW Lisboa Super Surf &rarr;</span>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="compare-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Op een rij</span>
      <h2>Bestemmingen in het kort</h2>
    </div>
    <div class="info-grid">
      <div class="info-card">
        <span class="icon">&#127466;&#127480;</span>
        <h3>WOW Espana &mdash; Palam&oacute;s</h3>
        <p>&euro;550 p.p. 6-daagse busreis. Groepen van 40 t/m 160 leerlingen. Accommodatie in bungalows op Camping Palam&oacute;s. Inclusief dagtrip Barcelona.</p>
      </div>
      <div class="info-card">
        <span class="icon">&#127470;&#127481;</span>
        <h3>WOW Italia &mdash; Milaan &amp; Caorle</h3>
        <p>&euro;650 p.p. 6-daagse busreis via Milaan, Caorle en een dagtrip Veneti&euml;. Verblijf op 5&#9733; Villaggio San Francesco.</p>
      </div>
      <div class="info-card">
        <span class="icon">&#127956;</span>
        <h3>WOW in the Snow &mdash; Zell am See</h3>
        <p>&euro;650 p.p. 6-daagse wintersportreis. Tot 74 deelnemers. Accommodatie in Villa Lukashansl. 4-daagse skipas voor scholen inbegrepen.</p>
      </div>
      <div class="info-card">
        <span class="icon">&#127477;&#127481;</span>
        <h3>WOW Lisboa Super Surf &mdash; Ericeira &amp; Lissabon</h3>
        <p>&euro;800 p.p. 5-daagse surfreis naar Ericeira met een dagtrip Lissabon. Surfen, SUP, bodyboarden en strandsport aan de Atlantische kust.</p>
      </div>
    </div>
    <p class="muted" style="margin-top:24px;font-size:13px;">Alle richtprijzen zijn compleet: vervoer, verblijf, maaltijden en programma inbegrepen &mdash; geen verborgen kosten.</p>
  </div>
</section>

<section class="final-cta reveal">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW schoolreis")}</div>
  <div class="wrap final-content">
    <h2>Welke WOW past bij jullie school?</h2>
    <p>We denken graag mee over de beste Experience voor jullie leerlingen.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("reizen.html", "Reizen | WOW — The Experience Company",
     "Ontdek de WOW Experiences: WOW Espana (Palamos & Barcelona), WOW Italia, WOW in the Snow (Zell am See & Kaprun) en WOW Lisboa Super Surf.",
     "reizen.html", reizen_body)

# =========================================================================
# WOW SPAIN — Palamos & Barcelona
# =========================================================================
spain_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW Espana — Palamos, Costa Brava")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="reizen.html">Reizen</a> &rarr; WOW Espana</div>
    <span class="kicker">&#127466;&#127480; WOW Espana</span>
    <h1>Palam&oacute;s &amp; Barcelona</h1>
    <p class="hero-sub">Zee. Sport. SUP. Snorkelen. Padel. Cultuur. Barcelona. Aan de Costa Brava beleven leerlingen zes dagen sport, zon en groepsgevoel &mdash; met een dagtrip naar Barcelona als culturele hoogtepunt.</p>
    <div class="hero-cta-row">
      <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <a class="btn btn-outline btn-lg" href="contact.html">Vraag informatie aan &rarr;</a>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">In &eacute;&eacute;n oogopslag</span>
      <h2>Alles wat je moet weten over de reis</h2>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(4,1fr);">
      <div class="info-card"><span class="icon">&#128205;</span><h3>Bestemming</h3><p>Palam&oacute;s, Costa Brava &mdash; Spanje</p></div>
      <div class="info-card"><span class="icon">&#128652;</span><h3>Vertrek</h3><p>Zondag &mdash; 18:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127937;</span><h3>Terugkomst</h3><p>Vrijdag &mdash; &plusmn; 10:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127968;</span><h3>Verblijf</h3><p>Bungalows 2&ndash;5 personen</p></div>
      <div class="info-card"><span class="icon">&#128653;</span><h3>Vervoer</h3><p>Luxe touringcars of dubbeldekker</p></div>
      <div class="info-card"><span class="icon">&#128104;&#8205;&#127979;</span><h3>Begeleiding</h3><p>Docenten &amp; sportbegeleiders</p></div>
      <div class="info-card"><span class="icon">&#128222;</span><h3>Contact</h3><p>Via school</p></div>
      <div class="info-card"><span class="icon">&#127919;</span><h3>Thema</h3><p>Sport &middot; Cultuur &middot; Samenwerking</p></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">Waarom deze Experience</span>
        <h2>De bestemming die perfect past bij het WOW schoolreis concept</h2>
        <p>Palam&oacute;s aan de Costa Brava is de thuisbasis van WOW. Een plek die we persoonlijk hebben bezocht, getest en ieder jaar opnieuw verbeteren.</p>
        <p>Leerlingen verblijven op Camping Palam&oacute;s in gezellige bungalows voor 2 tot 5 personen, op korte afstand van zee. Vanuit daar ontdekken ze de omgeving, sporten ze samen en beleven ze elke dag iets nieuws. Van watersport tot padel, tennis en beachvolleybal. En natuurlijk staat ook een dagtrip naar Barcelona op het programma &mdash; cultuur, ontdekken en lekker samen de stad in.</p>
        <p>De setting is onderdeel van het programma.</p>
        <p>Leerlingen delen hun bungalow met klasgenoten en zijn samen verantwoordelijk voor hun eigen plek. Ze maken ontbijt, verzorgen het diner, ruimen op en helpen elkaar. Geen hotel waar alles voor je wordt geregeld, maar een omgeving waarin je leert samenwerken, verantwoordelijkheid nemen en zelfstandig keuzes maken.</p>
        <p>Onze sportstudenten en begeleiders zorgen voor structuur, persoonlijke aandacht en een positief klimaat waarin leerlingen zich veilig voelen om nieuwe dingen te proberen. Iedere leerling wordt gezien, uitgedaagd en aangemoedigd om het beste uit zichzelf &eacute;n uit de groep te halen.</p>
        <p>Want uiteindelijk is dat waar WOW voor staat:</p>
        <p style="font-weight:700;">Samen beleven. Samen groeien. Samen herinneringen maken.</p>
        <div class="badge-row">
          <span class="badge">&euro;550 p.p.</span>
          <span class="badge">Geen verborgen kosten</span>
          <span class="badge">6-daagse busreis</span>
          <span class="badge">40&ndash;160 leerlingen</span>
          <span class="badge">Dagtrip Barcelona</span>
        </div>
      </div>
      <div class="split-media">{IMG("spain-groep-strandboulevard.jpg", "WOW leerlingen met SUP, bodyboard en padelracket op de boulevard in Palam&oacute;s")}</div>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Activiteiten</span>
      <h2>Sport, water en cultuur door elkaar</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127940;</span><h3>Watersport</h3><p>SUP-boarden, surfen, snorkelen en zwemmen in de Middellandse Zee.</p></div>
      <div class="info-card"><span class="icon">&#127934;</span><h3>Landsport</h3><p>Padel, tennis, beachvolleybal, voetbal en tafeltennis &mdash; inclusief toernooien.</p></div>
      <div class="info-card"><span class="icon">&#127358;</span><h3>Cultuur</h3><p>Dagtrip Barcelona met de Sagrada Fam&iacute;lia en Las Ramblas, plus een kustwandeling langs de Costa Brava.</p></div>
      <div class="info-card"><span class="icon">&#127871;</span><h3>Sociaal</h3><p>BBQ-avonden en samen koken met de WOW Box &mdash; groepsgevoel staat centraal.</p></div>
      <div class="info-card"><span class="icon">&#127958;</span><h3>Accommodatie</h3><p>Bungalows voor 2&ndash;5 personen op Camping Palam&oacute;s, met zwembaden en een chill zone.</p></div>
      <div class="info-card"><span class="icon">&#128652;</span><h3>Vervoer</h3><p>Comfortabele touringcar heen en terug, onderdeel van een complete 6-daagse reis.</p></div>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Weekschema</span>
      <h2>Dag voor dag</h2>
    </div>
    <div class="day-grid">
      <div class="day-card">
        <span class="day-num">Dag 1 &middot; Vertrek</span>
        <h3>Op reis naar Spanje</h3>
        <ul>
          <li><span class="time">17:30</span><span>Verzamelen op school (check ID/paspoort)</span></li>
          <li><span class="time">18:00</span><span>Vertrek richting Spanje &mdash; neem eten/drinken mee voor in de bus</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 2 &middot; Aankomst</span>
        <h3>Welkom in Palam&oacute;s</h3>
        <ul>
          <li><span class="time">10:00</span><span>Aankomst Palam&oacute;s &mdash; opening van de reis, broodjes &amp; koffie</span></li>
          <li><span class="time">13:00</span><span>Gezamenlijke lunch</span></li>
          <li><span class="time">13:30</span><span>Activiteitenronde 1 &mdash; keuzeactiviteiten</span></li>
          <li><span class="time">18:00</span><span>Diner ophalen</span></li>
          <li><span class="time">20:30</span><span>Avondprogramma</span></li>
          <li><span class="time">23:00</span><span>Iedereen in zijn eigen huisje</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 3 &middot; Actief</span>
        <h3>Sport en strand</h3>
        <ul>
          <li><span class="time">09:00</span><span>Opstaan, ontbijt &amp; lunchpakket maken</span></li>
          <li><span class="time">10:00</span><span>Activiteitenronde 2</span></li>
          <li><span class="time">13:00</span><span>Lunchpakket op het strand</span></li>
          <li><span class="time">14:00</span><span>Activiteitenronde 3</span></li>
          <li><span class="time">16:00</span><span>Vrije tijd op de camping</span></li>
          <li><span class="time">18:00</span><span>BBQ diner samen &mdash; kaartje schrijven naar huis</span></li>
          <li><span class="time">20:00</span><span>Avondprogramma &mdash; plan maken voor Barcelona</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 4 &middot; Barcelona</span>
        <h3>Dagtrip Barcelona</h3>
        <ul>
          <li><span class="time">08:30</span><span>Opstaan, ontbijt &amp; lunchpakket maken</span></li>
          <li><span class="time">09:00</span><span>Vertrek naar Barcelona</span></li>
          <li><span class="time">10:30</span><span>Programma Barcelona: culturele highlights, shoppen, chill &amp; fun</span></li>
          <li><span class="time">17:30</span><span>Terug richting Palam&oacute;s</span></li>
          <li><span class="time">18:45</span><span>Make your own tapas</span></li>
          <li><span class="time">21:00</span><span>Laatste avond: petje op / petje af &amp; gezelschapsspelletjes</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 5 &middot; Afsluiting</span>
        <h3>Laatste dag in Palam&oacute;s</h3>
        <ul>
          <li><span class="time">08:30</span><span>Opstaan, ontbijt &amp; opruimen huisjes</span></li>
          <li><span class="time">10:00</span><span>Uitchecken &mdash; daarna zwembad in</span></li>
          <li><span class="time">13:30</span><span>Lunchpakket</span></li>
          <li><span class="time">14:00</span><span>Activiteitenronde 4</span></li>
          <li><span class="time">17:00</span><span>Laatste gezamenlijk diner</span></li>
          <li><span class="time">18:00</span><span>Vertrek richting Nederland</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 6 &middot; Thuis</span>
        <h3>Terug op school</h3>
        <ul>
          <li><span class="time">10:00</span><span>Aankomst op school &mdash; welkom thuis!</span></li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:20px;font-size:13px;">Programma zoals gebruikt tijdens de reis &mdash; exacte tijden kunnen licht afwijken per groep en seizoen.</p>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Voorbereiding</span>
      <h2>Pak je koffer</h2>
      <p>Vergeet dit niet mee te nemen:</p>
    </div>
    <div class="pack-grid">
      <div class="pack-item"><span class="icon">&#129706;</span><span>Geldig paspoort of ID-kaart &amp; zorgpas</span></div>
      <div class="pack-item"><span class="icon">&#128085;</span><span>Kleding voor 4&ndash;5 dagen + 2 handdoeken</span></div>
      <div class="pack-item"><span class="icon">&#128095;</span><span>Sportkleding en sportschoenen</span></div>
      <div class="pack-item"><span class="icon">&#129701;</span><span>Toiletspullen (tandpasta, deo, shampoo)</span></div>
      <div class="pack-item"><span class="icon">&#129649;</span><span>Strandkleding, zwemkleding &amp; slippers</span></div>
      <div class="pack-item"><span class="icon">&#128374;&#65039;</span><span>Beach bag, zonnebril &amp; zonnebrand</span></div>
      <div class="pack-item"><span class="icon">&#128463;&#65039;</span><span>Eigen kussen voor bus &amp; camping</span></div>
      <div class="pack-item"><span class="icon">&#129386;</span><span>Eten &amp; drinken voor in de bus</span></div>
      <div class="pack-item"><span class="icon">&#127991;&#65039;</span><span>Label op je koffer met naam</span></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">De WOW Foodbox</span>
        <h2>Cook &middot; Eat &middot; Share &middot; Enjoy</h2>
        <p>Bij aankomst ontvangt ieder WOW-huisje een eigen WOW Foodbox, afgestemd op 3, 4 of 5 leerlingen. De box bevat de basis voor ontbijt, lunch en diner tijdens het verblijf, inclusief ingredi&euml;nten voor eenvoudige, lekkere maaltijden. We houden waar nodig rekening met vegetarische wensen, halal en allergie&euml;n of andere dieetwensen.</p>
        <div class="badge-row">
          <span class="badge">Cook</span>
          <span class="badge">Eat</span>
          <span class="badge">Share</span>
          <span class="badge">Enjoy</span>
        </div>
      </div>
      <div class="split-media">{IMG("foodbox-titlecard.jpg", "The WOW Food Box — School Recipes")}</div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">School Recipes</span>
      <h2>Snel, makkelijk en lekker &mdash; speciaal voor leerlingen</h2>
      <p>Bij de Foodbox horen onze School Recipes: geen ingewikkelde gerechten of lange boodschappenlijsten. Met de ingredi&euml;nten uit de box gaan leerlingen samen aan de slag &mdash; en bepalen ze zelf wat ze eten, wie kookt, wie de tafel dekt en wie opruimt.</p>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(5,1fr);">
      <div class="info-card"><span class="icon">&#129309;</span><h3>Samenwerken</h3><p>Verdeel de taken, kook samen en geniet samen.</p></div>
      <div class="info-card"><span class="icon">&#127793;</span><h3>Zelfstandigheid</h3><p>Leer plannen, koken, opruimen en verantwoordelijkheid nemen.</p></div>
      <div class="info-card"><span class="icon">&#128260;</span><h3>Flexibiliteit</h3><p>Pas gerechten aan naar eigen smaak en voorkeur.</p></div>
      <div class="info-card"><span class="icon">&#9878;&#65039;</span><h3>Bewust omgaan met eten</h3><p>Gebruik de voorraad slim en beperk verspilling.</p></div>
      <div class="info-card"><span class="icon">&#127881;</span><h3>Plezier</h3><p>Koken wordt een leuk onderdeel van de WOW Experience.</p></div>
    </div>
    <div class="founder-quote" style="margin-top:32px;">
      <span class="mark">&ldquo;</span>
      <p>Binnen duidelijke kaders krijgen leerlingen de vrijheid om hun eigen maaltijden te organiseren. De WOW Foodbox is meer dan eten tijdens een schoolreis &mdash; het is een actief onderdeel van de WOW-filosofie: zelfstandigheid, samenwerking, verantwoordelijkheid, verbinding en plezier.</p>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Afspraken</span>
      <h2>Zo zorgen we er samen voor dat iedereen een topweek heeft</h2>
    </div>
    <div class="compare-grid">
      <div class="compare-col self">
        <h3>Algemeen</h3>
        <ul>
          <li><span class="dot"></span>We gaan respectvol met elkaar om</li>
          <li><span class="dot"></span>We volgen de aanwijzingen van de leiding op</li>
          <li><span class="dot"></span>Alcohol en drugs zijn niet toegestaan</li>
          <li><span class="dot"></span>We zijn op de afgesproken tijden aanwezig</li>
          <li><span class="dot"></span>Laat de leiding weten waar je bent</li>
          <li><span class="dot"></span>De camping verlaat je niet zonder toestemming</li>
          <li><span class="dot"></span>Na 23:00 uur is het rustig op het terrein</li>
        </ul>
      </div>
      <div class="compare-col self">
        <h3>Verblijf &amp; eten</h3>
        <ul>
          <li><span class="dot"></span>We houden bus en huisje netjes</li>
          <li><span class="dot"></span>Controleer bij aankomst op schade, meld het</li>
          <li><span class="dot"></span>Geen bezoekers van buitenaf in de bungalow</li>
          <li><span class="dot"></span>Behandel campingpersoneel met respect</li>
          <li><span class="dot"></span>De chauffeur is de baas in de bus</li>
          <li><span class="dot"></span>Telefoons weg tijdens het eten</li>
          <li><span class="dot"></span>Na het eten helpt iedereen mee met opruimen</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid reverse">
      <div class="split-text">
        <span class="kicker">Veiligheid</span>
        <h2>Maximale beleving, duidelijke afspraken</h2>
        <p>Tijdens WOW Espana reizen professionele begeleiders mee, waaronder oprichter Milan zelf. Ouders blijven op de hoogte via een groepsapp. Er geldt een zero-tolerance beleid voor alcohol en drugs, en de reis is gedekt door VZR Garant financi&euml;le bescherming.</p>
        <a class="link-arrow" href="veiligheid.html">Lees meer over veiligheid bij WOW &rarr;</a>
      </div>
      <div class="split-media">{IMG("spain-instructeur-briefing.jpg", "WOW-instructeur geeft uitleg aan leerlingen voor de sportactiviteiten in Palam&oacute;s")}</div>
    </div>
  </div>
</section>

<section class="stories-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Fotogalerij</span>
      <h2>Sfeer uit Palam&oacute;s</h2>
    </div>
    <div class="gallery-grid">
      <div class="g1">{IMG("wow-hero-palamos.jpg", "WOW Espana sfeerfoto")}</div>
      {IMG("spain-groep-gear.jpg", "Leerlingen met SUP-, padel- en snorkelmateriaal in Palam&oacute;s")}
      {IMG("danique-sup-espana.jpg", "Danique met de WOW SUP-board tijdens WOW Espana")}
      {IMG("spain-barcelona-groep.jpg", "WOW groep bij het Columbusmonument tijdens de dagtrip naar Barcelona")}
      {IMG("spain-beachvolleybal.jpg", "Beachvolleybal tijdens WOW Espana")}
    </div>
  </div>
</section>

<section class="faq-section reveal">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="kicker">Veelgestelde vragen</span>
      <h2>WOW Espana &mdash; FAQ</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q"><span>Wat is de groepsgrootte voor WOW Espana?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Schoolreizen vari&euml;ren van 40 tot 160 leerlingen.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Is de reis geschikt voor niet-zwemmers?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Watersportactiviteiten worden begeleid door professionals en afgestemd op niveau. Neem contact op voor specifieke wensen of aandachtspunten.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Wat is inbegrepen in de prijs?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">De richtprijs is &euro;550 per leerling. Wat precies inbegrepen is, wordt samengesteld op basis van groep, programma en periode &mdash; we stellen een prijsindicatie samen na een kennismaking.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Hoe zit het met begeleiding en veiligheid?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Professionele begeleiders reizen mee, er is een groepsapp voor ouders, een zero-tolerance beleid voor alcohol/drugs en dekking via VZR Garant. Zie de veiligheidspagina voor meer details.</div></div></div>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW Espana")}</div>
  <div class="wrap final-content">
    <h2>De volgende schoolreis mag een WOW worden.</h2>
    <p>Ontdek wat WOW Espana voor jullie leerlingen kan betekenen.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("experience-spain.html", "WOW Espana — Palamós & Barcelona | WOW Experience Company",
     "WOW Espana: schoolreis naar Palamós aan de Costa Brava met SUP, snorkelen, padel en een dagtrip Barcelona.",
     "reizen.html", spain_body)

# =========================================================================
# WOW ITALY — Milaan / Venetie / Caorle (in ontwikkeling)
# =========================================================================
italy_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("italy-milaan-fontein.jpg", "WOW groep bij de fontein in Milaan")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="reizen.html">Reizen</a> &rarr; WOW Italia</div>
    <span class="kicker">&#127470;&#127481; WOW Italia &middot; De Sportiefste Eindexamenreis</span>
    <h1>Milaan &middot; Caorle &middot; Veneti&euml;</h1>
    <p class="hero-sub">Buongiorno, ciao tutti! Sport, cultuur en avontuur in Milaan, Caorle en Veneti&euml; &mdash; onvergetelijk met de WOW Famiglia.</p>
    <div class="hero-cta-row">
      <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <a class="btn btn-outline btn-lg" href="contact.html">Vraag informatie aan &rarr;</a>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">In &eacute;&eacute;n oogopslag</span>
      <h2>Alles wat je moet weten over de reis</h2>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(4,1fr);">
      <div class="info-card"><span class="icon">&#128205;</span><h3>Bestemming</h3><p>Milaan &middot; Caorle &middot; Veneti&euml; &mdash; Itali&euml;</p></div>
      <div class="info-card"><span class="icon">&#128652;</span><h3>Vertrek</h3><p>Zondag &mdash; 18:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127937;</span><h3>Terugkomst</h3><p>Zaterdag &mdash; &plusmn; 10:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127968;</span><h3>Verblijf</h3><p>4/5-persoons huisjes &mdash; 5&#9733; Villaggio San Francesco</p></div>
      <div class="info-card"><span class="icon">&#128653;</span><h3>Vervoer</h3><p>Luxe touringcars of dubbeldekkers</p></div>
      <div class="info-card"><span class="icon">&#128104;&#8205;&#127979;</span><h3>Begeleiding</h3><p>Docenten &amp; WOW team</p></div>
      <div class="info-card"><span class="icon">&#127869;&#65039;</span><h3>Eten</h3><p>Ontbijt &amp; lunch georganiseerd &middot; avond WOW box</p></div>
      <div class="info-card"><span class="icon">&#127919;</span><h3>Thema</h3><p>Sport &middot; Cultuur &middot; Fun &middot; Vrijheid</p></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">De gedachte achter WOW Italia</span>
        <h2>De WOW Italia Eindexamenreis</h2>
        <p>De laatste reis met je klasgenoten. Het afscheid van de middelbare school.</p>
        <p>Je eindexamens achter de rug. Jarenlang samen naar school, samen gelachen, gestrest, gefeest en herinneringen gemaakt. Nu is het tijd voor het laatste hoofdstuk: samen op reis en afscheid nemen van je middelbare schooltijd.</p>
        <p>Van de mode, cultuur en energie van Milaan naar de kanalen en historische straten van Veneti&euml; en vervolgens naar de zon, zee en het strand van Caorle. WOW Italia combineert het beste van Noord-Itali&euml; met sport, ontspanning en natuurlijk heel veel fun.</p>
        <p>Je ontdekt nieuwe plekken, beleeft Itali&euml; samen met je klasgenoten, sport, geniet van het strand en krijgt de vrijheid om er &eacute;cht een bijzondere reis van te maken. Met je eigen huisje, professionele begeleiding en een programma waarin alles voor je geregeld is.</p>
        <p>En natuurlijk is er de WOW Box. Samen met je vrienden bereid je op verschillende avonden je eigen maaltijd: lekker, makkelijk en gezellig. Geen standaard buffet, maar samen koken, eten en genieten in je eigen huisje.</p>
        <p>Dit is jullie laatste reis samen als klasgenoten en vrienden. Een afsluiting van een bijzondere periode en het begin van iets nieuws.</p>
        <p style="font-weight:700;">Sport. Cultuur. Strand. Fun.<br>Samen herinneringen maken.<br>JOIN THE WOW.</p>
        <div class="badge-row">
          <span class="badge">&euro;650 p.p.</span>
          <span class="badge">Geen verborgen kosten</span>
          <span class="badge">Milaan</span>
          <span class="badge">Caorle</span>
          <span class="badge">Veneti&euml;</span>
        </div>
      </div>
      <div class="split-media">{IMG("italy-venetie-groep.jpg", "WOW leerlingen in Venetie")}</div>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Stop 1 &amp; 3 &middot; Milaan &amp; Veneti&euml;</span>
      <h2>Twee steden, &eacute;&eacute;n onvergetelijke reis</h2>
    </div>
    <div class="split-grid" style="margin-bottom:40px;">
      <div class="split-text">
        <h3>La citt&agrave; della moda</h3>
        <p style="font-weight:700;">Milaan &mdash; stijl, cultuur &amp; vrijheid</p>
        <p>We starten onze reis in Milaan, de modestad van Itali&euml;. De indrukwekkende Duomo en het Castello Sforzesco laten meteen zien waarom Milaan zoveel meer is dan alleen mode.</p>
        <p>Daarna duiken jullie het centrum in. Van Gucci, Prada en Armani tot de leukste winkels voor ieder budget. Na de culturele highlights krijgen jullie de vrijheid om zelfstandig Milaan te ontdekken, samen met je klasgenoten.</p>
        <p>Even verdwalen in de stad, een terrasje pakken, shoppen of gewoon genieten van de Italiaanse sfeer. Milaan beleef je op je eigen manier.</p>
        <p>Na een late lunch stappen we weer in de bus en reizen we door naar Caorle.</p>
        <p style="font-weight:700;">Milaan: stijl, cultuur, vrijheid en de perfecte start van jullie WOW-reis.</p>
      </div>
      <div class="split-media">{IMG("italy-milaan-fontein.jpg", "WOW groep bij de fontein in Milaan")}</div>
    </div>
    <div class="split-grid reverse">
      <div class="split-text">
        <h3>Magisch &amp; mysterieus</h3>
        <p style="font-weight:700;">Veneti&euml; &mdash; een stad die je moet beleven</p>
        <p>Een hele dag Veneti&euml;. Een stad die eigenlijk niet uit te leggen is &mdash; je moet er rondlopen, verdwalen en haar zelf beleven.</p>
        <p>Smalle steegjes, verborgen pleinen, eeuwenoude gebouwen, eindeloze grachten en natuurlijk het beroemde Piazza San Marco. Tussendoor ontdek je de leukste winkels, proef je de sfeer en maak je samen met je klasgenoten herinneringen die je niet snel vergeet.</p>
        <p>Geen strak programma van begin tot eind. Jullie krijgen de vrijheid om Veneti&euml; op jullie eigen tempo te ontdekken.</p>
        <p>Samen op pad, een beetje verdwalen en vooral genieten.</p>
        <p style="font-weight:700;">Veneti&euml; is magisch. Veneti&euml; is mysterieus. Veneti&euml; vergeet je nooit.</p>
        <p style="font-weight:700;">Join the WOW.</p>
      </div>
      <div class="split-media">{IMG("italy-venetie-brug-groep.jpg", "WOW groep op een brug in Veneti&euml;")}</div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Stop 2 &middot; Caorle</span>
      <h2>Het Villaggio</h2>
    </div>
    <div class="split-grid reverse">
      <div class="split-text">
        <p>We verblijven op de luxe 5-sterren Camping Villaggio San Francesco aan de Adriatische kust &mdash; in gezellige 4/5-persoons huisjes. Bij aankomst krijg je de sleutels, laden we de bus uit en begin je het Villaggio te ontdekken.</p>
        <p>Het Villaggio is een heel dorp op zich: sportvelden, zwembaden, supermarkt en non-stop activiteiten. Dag 2 en dag 4 staat er een sportief programma op het rooster &mdash; jij kiest wat je leuk vindt.</p>
      </div>
      <div class="split-media">{IMG("italy-villaggio-groep.jpg", "WOW groep bij Villaggio San Francesco, Caorle")}</div>
    </div>
    <div class="info-grid" style="margin-top:46px;">
      <div class="info-card"><span class="icon">&#127940;</span><h3>Sport &amp; Spel</h3><p>Padellen, voetbal, volleybal, fitness en meer. Maak er een wedstrijd van met je klas.</p></div>
      <div class="info-card"><span class="icon">&#127940;&#65039;</span><h3>Zwembad &amp; Strand</h3><p>Chillen aan het zwembad, zonnen op het strand of een duik in de Adriatische Zee.</p></div>
      <div class="info-card"><span class="icon">&#127837;</span><h3>WOW Box</h3><p>Elke avond kook je samen met je huisgenoten uit de WOW box &mdash; en kies jij wat je eet.</p></div>
      <div class="info-card"><span class="icon">&#128722;</span><h3>Vrijheid</h3><p>Eigen tijd om te doen waar je zin in hebt: winkelen in de supermarkt, relaxen of een spelletje doen.</p></div>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Weekschema</span>
      <h2>Dag voor dag</h2>
    </div>
    <div class="day-grid">
      <div class="day-card">
        <span class="day-num">Dag 1 &middot; Vertrek</span>
        <h3>Op reis naar Itali&euml;</h3>
        <ul>
          <li><span class="time">17:30</span><span>Verzamelen op school (check ID/paspoort)</span></li>
          <li><span class="time">18:00</span><span>Vertrek richting Itali&euml; &mdash; neem eten &amp; drinken mee voor in de bus</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 2 &middot; Milaan &amp; Caorle</span>
        <h3>Van Milaan naar het Villaggio</h3>
        <ul>
          <li><span class="time">09:00</span><span>Aankomst Milaan &mdash; ontbijt &amp; opening van de dag</span></li>
          <li><span class="time">10:00</span><span>Culturele highlights: Duomo, Castello Sforzesco &amp; city walk</span></li>
          <li><span class="time">12:00</span><span>Vrij rondlopen in Milaan &mdash; shoppen, eten, ontdekken</span></li>
          <li><span class="time">14:30</span><span>Late lunch &amp; vertrek richting Caorle</span></li>
          <li><span class="time">17:30</span><span>Aankomst Villaggio San Francesco &mdash; sleutels ophalen, huisjes inrichten</span></li>
          <li><span class="time">19:00</span><span>Eerste avond: WOW box &mdash; samen koken met je huisgenoten</span></li>
          <li><span class="time">20:30</span><span>Avondprogramma &amp; Villaggio ontdekken</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 3 &middot; Sportdag</span>
        <h3>Sport &amp; vrije tijd</h3>
        <ul>
          <li><span class="time">08:30</span><span>Ontbijt georganiseerd door WOW team &amp; docenten</span></li>
          <li><span class="time">10:00</span><span>Sportprogramma keuzeronde 1 &mdash; padel, voetbal, volleybal of fitness</span></li>
          <li><span class="time">13:00</span><span>Lunch &mdash; georganiseerd door WOW team</span></li>
          <li><span class="time">14:00</span><span>Vrije tijd: strand, zwembad of activiteiten naar keuze</span></li>
          <li><span class="time">16:00</span><span>Sportprogramma keuzeronde 2</span></li>
          <li><span class="time">19:00</span><span>WOW box &mdash; kooktijd! Kies zelf wat je eet</span></li>
          <li><span class="time">21:00</span><span>Avondprogramma</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 4 &middot; Veneti&euml;</span>
        <h3>Dagtrip Veneti&euml;</h3>
        <ul>
          <li><span class="time">08:30</span><span>Ontbijt &amp; vertrekklaar maken</span></li>
          <li><span class="time">09:00</span><span>Vertrek naar Veneti&euml;</span></li>
          <li><span class="time">10:30</span><span>Dag Veneti&euml;: San Marco, grachten, steegjes, winkels &amp; beleving</span></li>
          <li><span class="time">17:00</span><span>Terug richting Caorle</span></li>
          <li><span class="time">19:00</span><span>WOW box &mdash; kooktijd!</span></li>
          <li><span class="time">21:00</span><span>Avondprogramma: petje op / petje af &amp; gezelschapsspelletjes</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 5 &middot; Sportdag</span>
        <h3>Laatste sportdag</h3>
        <ul>
          <li><span class="time">08:30</span><span>Ontbijt georganiseerd door WOW team &amp; docenten</span></li>
          <li><span class="time">10:00</span><span>Sportprogramma keuzeronde 3 &mdash; padel, voetbal, volleybal of fitness</span></li>
          <li><span class="time">13:00</span><span>Lunch &mdash; georganiseerd door WOW team</span></li>
          <li><span class="time">14:00</span><span>Vrije tijd: strand, zwembad of ontspannen</span></li>
          <li><span class="time">16:00</span><span>Sportprogramma keuzeronde 4</span></li>
          <li><span class="time">19:00</span><span>Laatste diner samen &mdash; WOW box</span></li>
          <li><span class="time">21:00</span><span>Laatste avondprogramma &amp; herinneringen ophalen</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 6 &middot; Laatste dag</span>
        <h3>Arrivederci Itali&euml;</h3>
        <ul>
          <li><span class="time">08:30</span><span>Ontbijt &amp; laatste zonnestralen</span></li>
          <li><span class="time">10:00</span><span>Opruimen huisjes &mdash; alles netjes achterlaten</span></li>
          <li><span class="time">11:00</span><span>Spullen in de bus &amp; uitchecken</span></li>
          <li><span class="time">11:30</span><span>Vrije tijd &mdash; zwembad, strand of Villaggio geniet nog even</span></li>
          <li><span class="time">13:00</span><span>Laatste lunch samen</span></li>
          <li><span class="time">16:00</span><span>Arrivederci Itali&euml;! Vertrek richting Nederland</span></li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 7 &middot; Thuis</span>
        <h3>Welkom thuis, WOW Famiglia!</h3>
        <ul>
          <li><span class="time">&plusmn;10:00</span><span>Aankomst op school &mdash; welkom thuis!</span></li>
        </ul>
      </div>
    </div>
    <p class="muted" style="margin-top:20px;font-size:13px;">Programma zoals gebruikt tijdens de reis &mdash; exacte tijden kunnen licht afwijken per groep en seizoen.</p>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Voorbereiding</span>
      <h2>Pak je koffer</h2>
      <p>Vergeet dit niet mee te nemen:</p>
    </div>
    <div class="pack-grid">
      <div class="pack-item"><span class="icon">&#129706;</span><span>Geldig paspoort of ID-kaart &amp; zorgpas</span></div>
      <div class="pack-item"><span class="icon">&#128085;</span><span>Kleding voor 4&ndash;5 dagen + 2 handdoeken</span></div>
      <div class="pack-item"><span class="icon">&#128095;</span><span>Sportkleding en sportschoenen</span></div>
      <div class="pack-item"><span class="icon">&#129701;</span><span>Toiletspullen (tandpasta, deo, shampoo)</span></div>
      <div class="pack-item"><span class="icon">&#129649;</span><span>Strandkleding, zwemkleding &amp; slippers</span></div>
      <div class="pack-item"><span class="icon">&#128374;&#65039;</span><span>Beach bag, zonnebril &amp; zonnebrand</span></div>
      <div class="pack-item"><span class="icon">&#128463;&#65039;</span><span>Eigen kussen voor in de bus</span></div>
      <div class="pack-item"><span class="icon">&#129386;</span><span>Eten &amp; drinken voor in de bus</span></div>
      <div class="pack-item"><span class="icon">&#127991;&#65039;</span><span>Label op je koffer met naam</span></div>
      <div class="pack-item"><span class="icon">&#128182;</span><span>Zakgeld voor Milaan &amp; Veneti&euml;</span></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">De WOW Foodbox</span>
        <h2>Cook &middot; Eat &middot; Share &middot; Enjoy</h2>
        <p>Bij aankomst ontvangt ieder WOW-huisje een eigen WOW Foodbox, afgestemd op 3, 4 of 5 leerlingen. De box bevat de basis voor ontbijt, lunch en diner tijdens het verblijf, inclusief ingredi&euml;nten voor eenvoudige, lekkere maaltijden. We houden waar nodig rekening met vegetarische wensen, halal en allergie&euml;n of andere dieetwensen.</p>
        <div class="badge-row">
          <span class="badge">Cook</span>
          <span class="badge">Eat</span>
          <span class="badge">Share</span>
          <span class="badge">Enjoy</span>
        </div>
      </div>
      <div class="split-media">{IMG("foodbox-titlecard.jpg", "The WOW Food Box — School Recipes")}</div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">School Recipes</span>
      <h2>Snel, makkelijk en lekker &mdash; speciaal voor leerlingen</h2>
      <p>Bij de Foodbox horen onze School Recipes: geen ingewikkelde gerechten of lange boodschappenlijsten. Met de ingredi&euml;nten uit de box gaan leerlingen samen aan de slag &mdash; en bepalen ze zelf wat ze eten, wie kookt, wie de tafel dekt en wie opruimt.</p>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(5,1fr);">
      <div class="info-card"><span class="icon">&#129309;</span><h3>Samenwerken</h3><p>Verdeel de taken, kook samen en geniet samen.</p></div>
      <div class="info-card"><span class="icon">&#127793;</span><h3>Zelfstandigheid</h3><p>Leer plannen, koken, opruimen en verantwoordelijkheid nemen.</p></div>
      <div class="info-card"><span class="icon">&#128260;</span><h3>Flexibiliteit</h3><p>Pas gerechten aan naar eigen smaak en voorkeur.</p></div>
      <div class="info-card"><span class="icon">&#9878;&#65039;</span><h3>Bewust omgaan met eten</h3><p>Gebruik de voorraad slim en beperk verspilling.</p></div>
      <div class="info-card"><span class="icon">&#127881;</span><h3>Plezier</h3><p>Koken wordt een leuk onderdeel van de WOW Experience.</p></div>
    </div>
    <div class="founder-quote" style="margin-top:32px;">
      <span class="mark">&ldquo;</span>
      <p>Binnen duidelijke kaders krijgen leerlingen de vrijheid om hun eigen maaltijden te organiseren. De WOW Foodbox is meer dan eten tijdens een schoolreis &mdash; het is een actief onderdeel van de WOW-filosofie: zelfstandigheid, samenwerking, verantwoordelijkheid, verbinding en plezier.</p>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Afspraken</span>
      <h2>Zo zorgen we er samen voor dat iedereen een topweek heeft</h2>
    </div>
    <div class="compare-grid">
      <div class="compare-col self">
        <h3>Algemeen</h3>
        <ul>
          <li><span class="dot"></span>We gaan respectvol met elkaar om</li>
          <li><span class="dot"></span>We volgen de aanwijzingen van de leiding op</li>
          <li><span class="dot"></span>Alcohol en drugs zijn niet toegestaan</li>
          <li><span class="dot"></span>We zijn op de afgesproken tijden aanwezig</li>
          <li><span class="dot"></span>Laat de leiding weten waar je bent</li>
          <li><span class="dot"></span>Het Villaggio verlaat je niet zonder toestemming</li>
          <li><span class="dot"></span>Na 23:00 uur is het rustig op het terrein</li>
        </ul>
      </div>
      <div class="compare-col self">
        <h3>Verblijf &amp; eten</h3>
        <ul>
          <li><span class="dot"></span>We houden bus en huisje netjes</li>
          <li><span class="dot"></span>Controleer bij aankomst op schade, meld het</li>
          <li><span class="dot"></span>Geen bezoekers van buitenaf in het huisje</li>
          <li><span class="dot"></span>Behandel campingpersoneel met respect</li>
          <li><span class="dot"></span>De chauffeur is de baas in de bus</li>
          <li><span class="dot"></span>Telefoons weg tijdens het eten</li>
          <li><span class="dot"></span>Na het eten helpt iedereen mee met opruimen</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Wat je kunt verwachten</span>
      <h2>Net als bij elke WOW Experience</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127939;</span><h3>Sport</h3><p>Strandsport en groepsactiviteiten, passend bij de Italiaanse kust.</p></div>
      <div class="info-card"><span class="icon">&#127961;</span><h3>Cultuur</h3><p>De kanalen van Veneti&euml;, de sfeer van Milaan en de Italiaanse levensstijl.</p></div>
      <div class="info-card"><span class="icon">&#127958;</span><h3>Strand</h3><p>Ontspanning en groepsmomenten aan de kust bij Caorle.</p></div>
      <div class="info-card"><span class="icon">&#128737;&#65039;</span><h3>Veiligheid</h3><p>Dezelfde professionele organisatie en veiligheidsstandaarden als bij alle WOW-reizen.</p></div>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="wrap final-content">
    <h2>Join the WOW Famiglia.</h2>
    <p>Ontdek wat WOW Italia voor jullie leerlingen kan betekenen.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("experience-italy.html", "WOW Italia — Milaan, Caorle & Venetië | WOW Experience Company",
     "WOW Italia: sport, cultuur en strand in Milaan, Caorle en Venetië. 6-daagse schoolreis met dagtrip Venetië en verblijf op 5★ Villaggio San Francesco.",
     "reizen.html", italy_body)


# =========================================================================
# WOW IN THE SNOW — Zell am See & Kaprun
# =========================================================================
snow_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("snow-goggles-groep.jpg", "WOW groep met skibril tijdens WOW in the Snow")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="reizen.html">Reizen</a> &rarr; WOW in the Snow</div>
    <span class="kicker">&#127956;&#65039; WOW in the Snow</span>
    <h1>Zell am See &amp; Kaprun</h1>
    <p class="hero-sub">Ski, snowboard, bergen en sneeuw &mdash; een week die je nooit meer vergeet. Welkom in Zell am See &amp; Kaprun, in het hart van de Oostenrijkse Alpen.</p>
    <div class="hero-cta-row">
      <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <a class="btn btn-outline btn-lg" href="contact.html">Vraag informatie aan &rarr;</a>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">In &eacute;&eacute;n oogopslag</span>
      <h2>Alles wat je moet weten over de reis</h2>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(4,1fr);">
      <div class="info-card"><span class="icon">&#128205;</span><h3>Bestemming</h3><p>Zell am See / Kaprun &mdash; Oostenrijk</p></div>
      <div class="info-card"><span class="icon">&#128652;</span><h3>Vertrek</h3><p>Dag 1 &mdash; 18:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127937;</span><h3>Terugkomst</h3><p>Dag 5 &mdash; &plusmn; 10:00 uur</p></div>
      <div class="info-card"><span class="icon">&#127976;</span><h3>Verblijf</h3><p>Kamers van 2, 3 of 4 personen</p></div>
      <div class="info-card"><span class="icon">&#128653;</span><h3>Vervoer</h3><p>Luxe touringcars of dubbeldekkers</p></div>
      <div class="info-card"><span class="icon">&#127935;</span><h3>Programma</h3><p>Ski- &amp; snowboardlessen + vrij rijden</p></div>
      <div class="info-card"><span class="icon">&#128105;&#8205;&#127979;</span><h3>Begeleiding</h3><p>Docenten &amp; WOW team</p></div>
      <div class="info-card"><span class="icon">&#127956;&#65039;</span><h3>Bergen</h3><p>Schmittenh&ouml;he &amp; Kitzsteinhorn gletsjer</p></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">De Reis</span>
        <h2>Jouw WOW in the Snow in de Alpen</h2>
        <p>De WOW In the Snow-reis brengt je naar Zell am See en Kaprun, midden in het indrukwekkende hart van de Oostenrijkse Alpen.</p>
        <p>We vertrekken &rsquo;s avonds met een luxe touringcar of dubbeldekker en rijden comfortabel door de nacht richting de bergen. Terwijl jij onderweg al kunt genieten van de sfeer met je vrienden, komen de besneeuwde toppen steeds dichterbij.</p>
        <p>We verblijven in Villa Lukashansl, waar je slaapt in comfortabele kamers van 2, 3 of 4 personen. Een fijne eigen accommodatie waar we samen verblijven en waar iedere ochtend een lekker ontbijt voor je klaarstaat.</p>
        <p>Natuurlijk is alles goed geregeld. De skipas en lessen zijn inbegrepen, zodat jij je nergens zorgen over hoeft te maken. Het enige wat jij hoeft te doen, is genieten van de sneeuw, de bergen en een onvergetelijke week met je vrienden.</p>
        <p>Het skigebied van Zell am See en de Kitzsteinhorn-gletsjer in Kaprun bieden pistes voor ieder niveau. Of je nu voor het eerst op ski&rsquo;s of een snowboard staat, of al jaren ervaring hebt: hier vind je altijd een uitdaging die bij jou past.</p>
        <p style="font-weight:700;">Sneeuw. Bergen. Vrienden. Sport. Fun.<br>Dit is niet zomaar een skireis.<br>Dit is jouw WOW In the Snow.</p>
        <div class="badge-row">
          <span class="badge">&euro;650 p.p.</span>
          <span class="badge">Geen verborgen kosten</span>
          <span class="badge">6 dagen</span>
          <span class="badge">Max. 74 deelnemers</span>
          <span class="badge">4-daagse skipas</span>
        </div>
      </div>
      <div class="split-media">{IMG("snow-lesson-groep.jpg", "WOW instructeur begeleidt leerlingen tijdens een snowboardles bij WOW in the Snow")}</div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Ski- &amp; Snowboardles</span>
      <h2>Professionele begeleiding op de piste</h2>
      <p>Voor beginners &eacute;n gevorderden</p>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127935;</span><h3>Ski&euml;n</h3><p>Van je eerste glij-beweging tot hoge snelheid op de blauwe en rode pistes. Onze gecertificeerde skileraren begeleiden jou op jouw niveau. Elke dag les in kleine groepen.</p></div>
      <div class="info-card"><span class="icon">&#127938;</span><h3>Snowboarden</h3><p>Liever een board onder je voeten? Kies voor snowboardles en leer de basics of verbeter je techniek. Freeriden, carven of jumps &mdash; de piste is jouw speelplaats.</p></div>
      <div class="info-card"><span class="icon">&#128994;</span><h3>Beginners</h3><p>Nog nooit op de latten gestaan? Geen probleem. We starten rustig op de groene en blauwe pistes en bouwen stap voor stap op. Na een paar dagen sta je er verbaasd van hoe snel je leert.</p></div>
      <div class="info-card"><span class="icon">&#128308;</span><h3>Gevorderden</h3><p>Al ervaring? Dan duiken we de rode en zwarte pistes op. Met honderden kilometers aan pistes in Zell am See en de gletsjer in Kaprun is er altijd een nieuwe uitdaging.</p></div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid reverse">
      <div class="split-text">
        <span class="kicker">In de praktijk</span>
        <h2>Persoonlijke begeleiding. Steeds een stapje verder.</h2>
        <p>Onze instructeurs staan dicht bij de groep. We geven persoonlijke aandacht, duidelijke instructies en passen het tempo aan op wat jij nodig hebt. Zo bouw je stap voor stap vertrouwen op.</p>
        <p>Van de eerste bochtjes en het remmen tot steeds langere en mooiere afdalingen. Je zult merken dat je iedere dag beter wordt.</p>
        <p>En dan komt misschien wel het mooiste moment. Gaat het &eacute;cht lekker en ben je er klaar voor? Dan mag je, natuurlijk altijd in overleg met onze begeleiding, samen met je vrienden zelfstandig de grote piste op.</p>
        <p>Hoe vet is dat? Zelf je afdaling kiezen. Samen met je vrienden naar beneden. En ondertussen weten je ouders dat wij in de buurt zijn en altijd een oogje in het zeil houden.</p>
        <p>WOW Exclusive is er trouwens niet alleen voor kinderen die nog moeten leren ski&euml;n. Ook als je al goed kunt ski&euml;n en graag een keer zonder je ouders op wintersport wilt, ben je bij WOW aan het juiste adres.</p>
        <p>Je krijgt de vrijheid om samen met je vrienden te genieten van de bergen, terwijl wij zorgen voor de begeleiding, structuur en veiligheid die daarbij horen.</p>
        <p style="font-weight:700;">Meer vrijheid. Meer vertrouwen. Meer avontuur.<br>Dat is WOW Exclusive.</p>
      </div>
      <div class="split-media">{IMG("snow-instructie-groep.jpg", "WOW instructeur geeft snowboardles aan leerlingen tijdens WOW in the Snow")}</div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-media">{IMG("snow-danique-piste.jpg", "Danique op de piste tijdens WOW in the Snow")}</div>
      <div class="split-text">
        <span class="kicker">Sfeer op de piste</span>
        <h2>Genieten van elke afdaling</h2>
        <p>Van de eerste voorzichtige bochtjes tot vol vertrouwen de piste af &mdash; bij WOW in the Snow draait het om plezier maken, vertrouwen opbouwen en samen genieten van de sneeuw.</p>
        <p>Plezier maken is verplicht. Gezellig doen mag gewoon. En dan komt dat moment&hellip; ineens lukt die bocht, die afdaling of die sprong waar je eerst nog over twijfelde. Dat gevoel? Gewoon te gaaf.</p>
        <p>Bij WOW in the Snow gaat het niet alleen om leren ski&euml;n of snowboarden. Het gaat om groeien, vertrouwen krijgen en samen herinneringen maken die je niet snel vergeet.</p>
      </div>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Meer dan ski&euml;n</span>
      <h2>Wat gaan we nog meer doen?</h2>
      <p>De avonden en vrije momenten zijn net zo leuk als de piste.</p>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127956;&#65039;</span><h3>Kitzsteinhorn</h3><p>De gletsjer van Kaprun op ruim 3.000 meter hoogte &mdash; indrukwekkend uitzicht en sneeuwzekere pistes.</p></div>
      <div class="info-card"><span class="icon">&#127749;</span><h3>Schmittenh&ouml;he</h3><p>Uitzicht op meer dan 30 bergtoppen vanuit Zell am See &mdash; een van de mooiste panorama&rsquo;s van de Alpen.</p></div>
      <div class="info-card"><span class="icon">&#127829;</span><h3>Apr&egrave;s-ski</h3><p>Na een dag op de piste gezellig bijkomen met je klas &mdash; eten, lachen en herinneringen ophalen.</p></div>
      <div class="info-card"><span class="icon">&#127918;</span><h3>Avondprogramma</h3><p>Elke avond een WOW-activiteit &mdash; van gezelschapsspelletjes tot een quiz of filmavond met de groep.</p></div>
      <div class="info-card"><span class="icon">&#127960;&#65039;</span><h3>Zell am See</h3><p>Het bergmeerdorpje Zell am See heeft leuke winkels, restaurants en een unieke sfeer &mdash; ideaal voor een avondwandeling.</p></div>
      <div class="info-card"><span class="icon">&#128248;</span><h3>Herinneringen</h3><p>Foto&rsquo;s op de top, sneeuwballen gooien, samen vallen en opstaan &mdash; dit zijn de momenten die je bijblijven.</p></div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Programma &amp; prijs 2026</span>
      <h2>Concreet en compleet geregeld</h2>
      <p>Geen verborgen kosten: onderstaande prijzen zijn inclusief vervoer, verblijf, maaltijden, skipas, materiaal en verzekering.</p>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(2,1fr);">
      <div class="price-card">
        <p>Prijs per deelnemer</p>
        <div class="amount">&euro;650</div>
        <p>Incl. vervoer, alle maaltijden, 4-daagse skipas, materiaal en verzekering</p>
      </div>
      <div class="info-card">
        <span class="icon">&#128652;</span><h3>Vertrekpunten</h3><p>Luxe touringcar vanaf Den Hoorn, Den Haag, Utrecht of Amsterdam.</p>
      </div>
    </div>
  </div>
</section>

<section class="split-section reveal" style="background:#0a0a0a;color:#fff;">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker" style="color:#e6432f;">Los boeken &middot; voor leerlingen</span>
      <h2 style="color:#fff;">WOW in the Snow Exclusive</h2>
      <p style="color:#cfcfcf;">Ga je niet met je klas mee, maar wil je toch die onvergetelijke sneeuwweek beleven? WOW in the Snow Exclusive is er speciaal voor individuele leerlingen &mdash; zelfde bestemming, dezelfde WOW-organisatie en begeleiding, gewoon los te boeken in de kerstvakantie.</p>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(3,1fr);">
      <div class="price-card">
        <p>Prijs per leerling</p>
        <div class="amount">&euro;850</div>
        <p>Incl. vervoer, alle maaltijden, 5-daagse skipas, materiaal en verzekering</p>
      </div>
      <div class="info-card" style="background:#171717;border-color:#2a2a2a;">
        <span class="icon">&#128197;</span><span class="badge" style="color:#0a0a0a;">WOW Exclusive Christmas</span><h3 style="color:#fff;">Data</h3><p style="color:#cfcfcf;">18 t/m 24 december 2026 &middot; Kaprun &amp; Zell am See, Oostenrijk.</p>
      </div>
      <div class="info-card" style="background:#171717;border-color:#2a2a2a;">
        <span class="icon">&#127956;</span><h3 style="color:#fff;">Bestemming</h3><p style="color:#cfcfcf;">Kaprun &amp; Zell am See &mdash; dezelfde Alpen-ervaring als WOW in the Snow, nu los te boeken.</p>
      </div>
    </div>
    <div style="margin-top:32px;">
      <a class="btn btn-lg" href="aanmelden-snow-exclusive.html">Meld je aan voor WOW Exclusive &rarr;</a>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Inbegrepen</span>
      <h2>Alles geregeld, niets te regelen</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127958;</span><h3>Accommodatie</h3><p>Villa Lukashansl, kamers voor 2, 3 of 4 personen.</p></div>
      <div class="info-card"><span class="icon">&#127869;&#65039;</span><h3>Maaltijden</h3><p>Ontbijt, lunch en diner inbegrepen tijdens de hele reis.</p></div>
      <div class="info-card"><span class="icon">&#9970;</span><h3>Ski &amp; snowboard</h3><p>4-daagse skipas voor scholen, materiaalhuur of eigen materiaal, en instructie door gecertificeerde leraren.</p></div>
      <div class="info-card"><span class="icon">&#127939;</span><h3>Activiteiten</h3><p>Ski&euml;n, snowboarden, apr&egrave;s-ski spelletjes en vrije tijd met de groep.</p></div>
      <div class="info-card"><span class="icon">&#128737;&#65039;</span><h3>Veiligheid</h3><p>Ervaren mentoren, gecertificeerde instructeurs, veilige accommodatie en duidelijke afspraken.</p></div>
      <div class="info-card"><span class="icon">&#128737;</span><h3>Verzekering</h3><p>Wintersport reisverzekering inbegrepen voor alle deelnemers.</p></div>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Weekschema</span>
      <h2>Dag voor dag</h2>
    </div>
    <div class="day-grid">
      <div class="day-card">
        <span class="day-num">Dag 1 &middot; Vertrek</span>
        <h3>Vertrek richting de Alpen</h3>
        <ul>
          <li><span class="time">17:30</span> Verzamelen op school (check ID/Paspoort &amp; skipas)</li>
          <li><span class="time">18:00</span> Vertrek richting Oostenrijk &mdash; neem eten &amp; drinken mee voor in de bus</li>
          <li><span class="time">Nacht</span> Rijden door de nacht richting de Alpen &#10052;&#65039;</li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 2</span>
        <h3>Aankomst &amp; eerste piste</h3>
        <ul>
          <li><span class="time">08:00</span> Aankomst Zell am See &mdash; inchecken &amp; kamers betrekken</li>
          <li><span class="time">09:30</span> Ski- &amp; snowboardverhuur &mdash; uitrusting ophalen en passen</li>
          <li><span class="time">11:00</span> Eerste keer de piste op! Niveau-indeling &amp; eerste les</li>
          <li><span class="time">13:00</span> Lunchpauze op de berg</li>
          <li><span class="time">14:00</span> Middagsessie &mdash; les of vrij rijden</li>
          <li><span class="time">16:30</span> Terug naar het verblijf &mdash; douchen &amp; bijkomen</li>
          <li><span class="time">18:30</span> Diner samen</li>
          <li><span class="time">20:00</span> Avondprogramma</li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 3</span>
        <h3>Skidag</h3>
        <ul>
          <li><span class="time">08:00</span> Ontbijt</li>
          <li><span class="time">09:00</span> Naar de piste &mdash; les of vrij rijden op Schmittenh&ouml;he</li>
          <li><span class="time">13:00</span> Lunchpauze op de berg</li>
          <li><span class="time">14:00</span> Middagsessie &mdash; pistes naar keuze</li>
          <li><span class="time">16:30</span> Terug naar het verblijf</li>
          <li><span class="time">18:30</span> Diner samen</li>
          <li><span class="time">20:00</span> Avondprogramma &amp; vrije tijd</li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 4</span>
        <h3>Gletsjer Kaprun</h3>
        <ul>
          <li><span class="time">08:00</span> Ontbijt</li>
          <li><span class="time">09:00</span> Vertrek naar Kaprun &mdash; Kitzsteinhorn gletsjer (3.000m+)</li>
          <li><span class="time">10:00</span> Ski&euml;n &amp; snowboarden op de gletsjer &mdash; unieke ervaring!</li>
          <li><span class="time">13:00</span> Lunchpauze met uitzicht over de Alpen</li>
          <li><span class="time">14:00</span> Middagsessie op de gletsjer</li>
          <li><span class="time">16:30</span> Afdalen &amp; terug naar het verblijf</li>
          <li><span class="time">18:30</span> Diner samen</li>
          <li><span class="time">20:00</span> Laatste avondprogramma: petje op / petje af &amp; terugblik op de week</li>
        </ul>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 5 &middot; Thuis</span>
        <h3>Laatste skidag &amp; vertrek</h3>
        <ul>
          <li><span class="time">08:00</span> Ontbijt &amp; kamers opruimen</li>
          <li><span class="time">09:00</span> Laatste keer de piste op &mdash; geniet er maximaal van!</li>
          <li><span class="time">13:00</span> Lunchpauze op de berg</li>
          <li><span class="time">14:00</span> Laatste skirun &mdash; daarna ski-uitrusting inleveren</li>
          <li><span class="time">15:30</span> Uitchecken &mdash; koffers in de bus</li>
          <li><span class="time">17:00</span> Auf Wiedersehen, &Ouml;sterreich! Vertrek richting Nederland &#127956;&#65039;</li>
          <li><span class="time">&plusmn; 10:00</span> Aankomst op school &mdash; welkom thuis! &#10052;&#65039;&#127881;</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Voorbereiding</span>
      <h2>Pak je koffer</h2>
      <p>Wintersport vraagt om de juiste spullen &mdash; check deze lijst goed:</p>
    </div>
    <div class="pack-grid">
      <div class="pack-item"><span class="icon">&#129706;</span> Geldig paspoort of ID-kaart &amp; zorgpas</div>
      <div class="pack-item"><span class="icon">&#129509;</span> Waterdichte ski- of snowboardjas &amp; broek</div>
      <div class="pack-item"><span class="icon">&#129508;</span> Warme handschoenen &amp; muts of helm</div>
      <div class="pack-item"><span class="icon">&#128374;&#65039;</span> Skibril (UV-bescherming essentieel)</div>
      <div class="pack-item"><span class="icon">&#129507;</span> Thermisch ondergoed (boven &amp; onder)</div>
      <div class="pack-item"><span class="icon">&#128095;</span> Stevige laarzen voor buiten de piste</div>
      <div class="pack-item"><span class="icon">&#129524;</span> Zonnebrand factor 50+ (berg-UV!)</div>
      <div class="pack-item"><span class="icon">&#129701;</span> Toiletspullen (tandpasta, deo, shampoo)</div>
      <div class="pack-item"><span class="icon">&#128085;</span> Kleding voor 4 avonden &amp; 2 handdoeken</div>
      <div class="pack-item"><span class="icon">&#128719;&#65039;</span> Eigen kussen voor in de bus</div>
      <div class="pack-item"><span class="icon">&#129386;</span> Eten &amp; drinken voor in de bus</div>
      <div class="pack-item"><span class="icon">&#127991;&#65039;</span> Label op je koffer met naam</div>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Afspraken</span>
      <h2>Op de piste &eacute;n daarbuiten</h2>
      <p>Zo zorgen we voor een veilige en topweek</p>
    </div>
    <div class="compare-grid">
      <div class="compare-col self">
        <h3>Op de piste</h3>
        <ul>
          <li><span class="dot"></span>Rijden altijd in groepen &mdash; nooit alleen op de piste</li>
          <li><span class="dot"></span>Helmplicht &mdash; een helm is verplicht voor iedereen</li>
          <li><span class="dot"></span>Volg de aanwijzingen van de skileraar op</li>
          <li><span class="dot"></span>Blijf binnen het afgesproken pistengebied</li>
          <li><span class="dot"></span>Bij slecht weer of mist: terug naar de basis</li>
          <li><span class="dot"></span>Meld je altijd af bij de begeleiding als je stopt</li>
        </ul>
      </div>
      <div class="compare-col self">
        <h3>Verblijf &amp; Algemeen</h3>
        <ul>
          <li><span class="dot"></span>We gaan respectvol met elkaar om</li>
          <li><span class="dot"></span>Alcohol en andere ongein zijn niet toegestaan</li>
          <li><span class="dot"></span>We houden de kamer netjes en schoon</li>
          <li><span class="dot"></span>Na 23:00 uur is het rustig op de gang</li>
          <li><span class="dot"></span>De chauffeur is de baas in de bus</li>
          <li><span class="dot"></span>Laat de leiding altijd weten waar je bent</li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="faq-section reveal">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="kicker">Veelgestelde vragen</span>
      <h2>WOW in the Snow &mdash; FAQ</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item"><div class="faq-q"><span>Is de reis geschikt voor beginners?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Ja. Zell am See/Kaprun is beginnersvriendelijk en instructie wordt gegeven op elk niveau, van eerste keer op ski's tot gevorderd.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Is materiaal inbegrepen?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Ja, materiaalhuur is inbegrepen in de prijs, met de optie om eigen materiaal mee te nemen.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Hoeveel deelnemers kunnen mee?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Maximaal 74 deelnemers per editie.</div></div></div>
      <div class="faq-item"><div class="faq-q"><span>Wat gebeurt er bij noodgevallen of medische bijzonderheden?</span><span class="plus">+</span></div><div class="faq-a"><div class="faq-a-inner">Ervaren mentoren en gecertificeerde instructeurs zijn continu aanwezig, met duidelijke noodprocedures. Zie de veiligheidspagina voor meer informatie.</div></div></div>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="wrap final-content">
    <h2>Op naar de bergen?</h2>
    <p>Ontdek wat WOW in the Snow voor jullie leerlingen kan betekenen.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("experience-snow.html", "WOW in the Snow — Zell am See & Kaprun | WOW Experience Company",
     "WOW in the Snow: wintersportreis naar Zell am See & Kaprun, Oostenrijk. Ski, snowboard en groepsbeleving in de bergen.",
     "reizen.html", snow_body)

# =========================================================================
# WOW IN THE SNOW EXCLUSIVE — aanmeldformulier (individueel, december)
# =========================================================================
snow_exclusive_form_body = f"""
<section class="hero-compact" style="min-height:40vh;">
  <div class="hero-media">{IMG("snow-goggles-groep.jpg", "WOW groep met skibril tijdens WOW in the Snow")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="experience-snow.html">WOW in the Snow</a> &rarr; Aanmelden Exclusive</div>
    <span class="kicker">WOW in the Snow Exclusive &middot; 18&ndash;24 december 2026</span>
    <h1>Meld je aan voor WOW Exclusive</h1>
    <p class="hero-sub">Vul onderstaand formulier in en wij nemen binnen enkele werkdagen contact met je op om de aanmelding af te ronden.</p>
  </div>
</section>

<section class="contact-section reveal">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info-card">
        <h3>WOW in the Snow Exclusive</h3>
        <p>Een individuele wintersportweek voor leerlingen &mdash; zelfde bestemming en WOW-organisatie als WOW in the Snow, los te boeken in de kerstvakantie.</p>
        <div class="contact-info-row"><div class="icon">&#128197;</div><div><strong>Data</strong><span>18 t/m 24 december 2026</span></div></div>
        <div class="contact-info-row"><div class="icon">&#127956;</div><div><strong>Bestemming</strong><span>Kaprun &amp; Zell am See, Oostenrijk</span></div></div>
        <div class="contact-info-row"><div class="icon">&#128176;</div><div><strong>Prijs</strong><span>&euro;850 per leerling, incl. vervoer, verblijf, maaltijden, skipas, materiaal en verzekering</span></div></div>
        <div class="contact-info-row"><div class="icon">&#128231;</div><div><strong>Vragen?</strong><span><a href="contact.html" style="color:#fff;">Neem contact op</a></span></div></div>
      </div>

      <div>
        <form id="snow-exclusive-form" class="form-grid lead-form" novalidate>
          <input type="hidden" name="bestemming" value="WOW in the Snow Exclusive — december 2026 (individueel)">
          <div class="field full"><label for="se-naam">Naam en achternaam *</label><input id="se-naam" name="naam" type="text" required></div>
          <div class="field"><label for="se-geboortedatum">Geboortedatum *</label><input id="se-geboortedatum" name="geboortedatum" type="date" required></div>
          <div class="field"><label for="se-school">School *</label><input id="se-school" name="school" type="text" required></div>
          <div class="field"><label for="se-email">E-mailadres *</label><input id="se-email" name="email" type="email" required></div>
          <div class="field"><label for="se-email-ouders">E-mailadres ouders *</label><input id="se-email-ouders" name="email_ouders" type="email" required></div>
          <div class="field"><label for="se-telefoon">Telefoonnummer *</label><input id="se-telefoon" name="telefoon" type="tel" required></div>
          <div class="field"><label for="se-samen-met">Ik meld me aan met</label><input id="se-samen-met" name="samen_met" type="text" placeholder="Naam vriend(in) &mdash; optioneel, voor als jullie samen op de kamer willen"></div>
          <div class="field full">
            <button type="submit" class="btn btn-block btn-lg">Meld je aan &rarr;</button>
            <p class="form-note">Door dit formulier te versturen ga je akkoord dat WOW Reizen contact met je (en je ouders) opneemt over deze aanmelding.</p>
          </div>
        </form>
        <div class="form-success">
          <div class="check">&#10003;</div>
          <h3>Bedankt voor je aanmelding.</h3>
          <p>Je aanmelding voor WOW in the Snow Exclusive is binnen. Het WOW-team neemt binnen enkele werkdagen contact met je op.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""
page("aanmelden-snow-exclusive.html", "Aanmelden WOW in the Snow Exclusive | WOW — The Experience Company",
     "Meld je aan voor WOW in the Snow Exclusive: 18 t/m 24 december 2026, Kaprun & Zell am See. Individuele wintersportreis voor leerlingen.",
     "reizen.html", snow_exclusive_form_body, sticky=False)

# =========================================================================
# WOW LISBOA SUPER SURF — Lissabon, Portugal (in ontwikkeling)
# =========================================================================
lisboa_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("lisboa-surf-groep2.jpg", "WOW groep na hun surfles bij Foz do Lizandro, Ericeira")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; <a href="reizen.html">Reizen</a> &rarr; WOW Lisboa Super Surf</div>
    <span class="kicker">&#127477;&#127481; WOW Lisboa Super Surf &middot; Ericeira &middot; Lissabon &middot; Portugal</span>
    <h1>Ericeira &amp; Lissabon</h1>
    <p class="hero-sub">Bem-vindo estudantes! Jij gaat mee op een megagave, sportieve en culturele reis naar Ericeira &amp; Lissabon in Portugal. Surfen op de golven van de Atlantische Oceaan, het authentieke surfstadje Ericeira ontdekken en een complete dag Lissabon beleven.</p>
    <p style="color:#e6432f;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:13px;margin-top:14px;">Surf &middot; Culture &middot; Freedom &middot; Connection</p>
    <div class="hero-cta-row">
      <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
      <a class="btn btn-outline btn-lg" href="contact.html">Vraag informatie aan &rarr;</a>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">Meer dan een surftrip</span>
        <h2>WOW Lisboa Super Surf</h2>
        <p style="color:#e6432f;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:13px;">Surf. Explore. Chill. Grow.</p>
        <p>Dit wordt geen standaard schoolreis. Dit wordt vijf dagen WOW. Surfen op de golven van de Atlantische Oceaan, sporten op het strand, Ericeira ontdekken, een volle dag Lissabon beleven, chillen met je vrienden en nieuwe mensen leren kennen.</p>
        <p>WOW Lisboa Super Surf draait natuurlijk om surfen. Maar deze reis gaat over veel meer. Misschien sta je voor het eerst op een surfboard. Misschien pak jij die golf waarvan je dacht: no way. Misschien help je een klasgenoot die het spannend vindt. Of ontdek je Lissabon samen met je vrienden en bepaal je zelf waar jullie naartoe gaan.</p>
        <p>Nieuwe plek. Nieuwe mensen. Nieuwe uitdagingen. Je krijgt vrijheid &eacute;n verantwoordelijkheid. Je probeert, valt, staat weer op en gaat opnieuw. Je ontdekt wat je kunt, krijgt meer zelfvertrouwen en leert samenwerken en zelfstandig keuzes maken.</p>
        <p>En ondertussen? Heel veel plezier. Surfen, sporten, lachen, chillen, nieuwe vrienden maken, grenzen verleggen en samen herinneringen cre&euml;ren die je nooit meer vergeet.</p>
        <p>Bij WOW geloven we dat sommige van de mooiste lessen niet uit een boek komen. Je moet ze beleven.</p>
        <p>En soms moet je daarvoor gewoon die golf pakken.</p>
        <p style="font-weight:700;">WELCOME TO PORTUGAL. WELCOME TO ERICEIRA. JOIN THE WOW.</p>
        <div class="badge-row">
          <span class="badge">Persoonlijke groei</span>
          <span class="badge">Zelfvertrouwen</span>
          <span class="badge">Weerbaarheid</span>
          <span class="badge">Zelfstandigheid</span>
          <span class="badge">Verantwoordelijkheid</span>
          <span class="badge">Verbinding</span>
        </div>
      </div>
      <div class="split-media">{IMG("lisboa-surf-briefing.jpg", "WOW groep krijgt surfbriefing bij Foz do Lizandro, Ericeira")}</div>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-media">{IMG("founder-portrait-portugal.jpg", "Surfen bij Praia da Foz do Lizandro, Ericeira")}</div>
      <div class="split-text">
        <span class="kicker">Ericeira &mdash; Surf Capital</span>
        <h2>Een van de bekendste surfbestemmingen van Europa</h2>
        <p>Hier draait alles om de oceaan, surfen, sport en het relaxte Portugese leven. Een groot deel van onze activiteiten vindt plaats rond Praia da Foz do Lizandro. Onder professionele begeleiding gaan we het water in.</p>
        <p>Nog nooit gesurft? Geen probleem &mdash; je leert stap voor stap de basis en probeert je eerste echte golf te pakken. Heb je al ervaring? Dan dagen we je uit om jezelf verder te ontwikkelen. Het gaat bij WOW niet om wie de beste surfer is. Het gaat om proberen, vallen, opstaan, lachen en elkaar helpen &mdash; totdat dat ene moment komt waarop je op je board staat en denkt: WOW, ik doe het gewoon.</p>
      </div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Sport &middot; Play &middot; Chill</span>
      <h2>Niet alleen op het surfboard komen we in beweging</h2>
      <p>Afhankelijk van het programma, het weer en de omstandigheden kunnen deze activiteiten onderdeel zijn van jouw WOW Experience &mdash; soms fanatiek, soms gewoon voor de lol.</p>
    </div>
    <div class="badge-row" style="justify-content:center;">
      <span class="badge">Surfen</span>
      <span class="badge">SUP</span>
      <span class="badge">Bodyboarden</span>
      <span class="badge">Beachvolleybal</span>
      <span class="badge">Beachvoetbal</span>
      <span class="badge">Beach Games</span>
      <span class="badge">Wandelen</span>
      <span class="badge">Sport Challenges</span>
      <span class="badge">WOW Games</span>
    </div>
    <p class="lead center" style="margin-top:32px;font-weight:700;">Surf. Sport. Play. Relax. Have fun.</p>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">A WOW Day in Lisboa</span>
        <h2>Een complete dag Lissabon</h2>
        <p>Portugal is natuurlijk veel meer dan alleen surfen. Daarom nemen we jullie tijdens deze reis mee naar Lissabon &mdash; een complete dag waarin cultuur, ontdekken, vrijheid en verantwoordelijkheid samenkomen. We wandelen door de stad, ontdekken bijzondere plekken en ervaren de sfeer van &eacute;&eacute;n van de gaafste hoofdsteden van Europa.</p>
        <p>Daarnaast krijg je binnen duidelijke afspraken ruimte om samen met je vrienden de stad te ontdekken. Want bij WOW hoort vrijheid. Maar vrijheid betekent ook: verantwoordelijkheid nemen.</p>
        <div class="badge-row">
          <span class="badge">Bel&eacute;m</span>
          <span class="badge">Torre de Bel&eacute;m</span>
          <span class="badge">Mosteiro dos Jer&oacute;nimos</span>
          <span class="badge">De Taag</span>
          <span class="badge">Pra&ccedil;a do Com&eacute;rcio</span>
          <span class="badge">Baixa &amp; Chiado</span>
        </div>
      </div>
      <div class="split-media">{IMG("lisboa-belem-groep.jpg", "WOW groep bij de Torre de Belém, Lissabon")}</div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Your WOW Experience</span>
      <h2>Vijf belangrijke onderdelen</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127940;</span><h3>Sport</h3><p>Jezelf fysiek uitdagen, nieuwe activiteiten proberen en ontdekken hoeveel je kunt.</p></div>
      <div class="info-card"><span class="icon">&#127961;</span><h3>Cultuur</h3><p>Portugal, Ericeira en Lissabon niet alleen bezoeken, maar echt beleven.</p></div>
      <div class="info-card"><span class="icon">&#129309;</span><h3>Verbinding</h3><p>Samen ervaringen opdoen, elkaar helpen en je klasgenoten op een andere manier leren kennen.</p></div>
      <div class="info-card"><span class="icon">&#128330;&#65039;</span><h3>Vrijheid</h3><p>Ruimte krijgen om zelf keuzes te maken, met je vrienden op pad te gaan en zelfstandiger te worden.</p></div>
      <div class="info-card"><span class="icon">&#127793;</span><h3>Persoonlijke ontwikkeling</h3><p>Uit je comfortzone stappen, uitdagingen aangaan en ontdekken hoeveel er eigenlijk in je zit.</p></div>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Weekschema</span>
      <h2>Jouw 5-daagse WOW Experience</h2>
    </div>
    <div class="day-grid">
      <div class="day-card">
        <span class="day-num">Dag 1 &middot; Hello Portugal</span>
        <h3>Aankomst in Ericeira</h3>
        <ul>
          <li>Verzamelen op de luchthaven</li>
          <li>Vlucht naar Lissabon &amp; transfer naar Ericeira</li>
          <li>Aankomst en check-in accommodatie</li>
          <li>WOW Welcome &amp; accommodatie ontdekken</li>
          <li>Kamers verdelen, diner en gezamenlijke avond</li>
        </ul>
        <p style="margin-top:14px;font-style:italic;color:#666;">De eerste avond staat in het teken van aankomen, elkaar vinden en kennismaken met onze omgeving. Welcome to the WOW.</p>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 2 &middot; First Waves</span>
        <h3>Je eerste surfles</h3>
        <ul>
          <li>Ontbijt &amp; lunchpakket maken</li>
          <li>Wandeling richting Praia da Foz do Lizandro</li>
          <li>Professionele surfles</li>
          <li>Lunch op het strand, beach &amp; chill</li>
          <li>Ericeira ontdekken, diner en WOW avondprogramma</li>
        </ul>
        <p style="margin-top:14px;font-style:italic;color:#666;">Wetsuit aan, board onder je arm, en richting de Atlantische Oceaan. Your first waves. Your first WOW.</p>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 3 &middot; Surf &amp; Beach</span>
        <h3>Meer golven, meer uitdaging</h3>
        <ul>
          <li>Ontbijt &amp; lunchpakket maken</li>
          <li>Vertrek richting surfschool &mdash; Surf Experience</li>
          <li>Lunch op het strand &amp; Beach Games</li>
          <li>Bodyboarden / beachvolleybal / beachvoetbal</li>
          <li>Vrije tijd met je vrienden, diner en WOW avondprogramma</li>
        </ul>
        <p style="margin-top:14px;font-style:italic;color:#666;">Meer vertrouwen, meer golven, meer uitdaging &mdash; en vooral heel veel plezier samen. Challenge yourself. Push your limits.</p>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 4 &middot; A WOW Day in Lisboa</span>
        <h3>Dagtrip Lissabon</h3>
        <ul>
          <li>Ontbijt &amp; vertrek naar Lissabon</li>
          <li>Bel&eacute;m, Torre de Bel&eacute;m &amp; wandeling langs de Taag</li>
          <li>Pra&ccedil;a do Com&eacute;rcio, Baixa &amp; Chiado</li>
          <li>WOW City Challenge &amp; culturele ontdekkingstocht</li>
          <li>Vrije ontdekkingstijd in groepjes, terug naar Ericeira, diner</li>
        </ul>
        <p style="margin-top:14px;font-style:italic;color:#666;">Van surfboards en stranden naar &eacute;&eacute;n van de mooiste steden van Europa. Explore. Discover. Experience Lisboa.</p>
      </div>
      <div class="day-card">
        <span class="day-num">Dag 5 &middot; At&eacute; Logo Portugal</span>
        <h3>Laatste surf &amp; terugreis</h3>
        <ul>
          <li>Ontbijt, kamers opruimen en check-out</li>
          <li>Vertrek richting strand &mdash; laatste Surf / SUP Experience</li>
          <li>Beach &amp; chill, lunch en laatste vrije tijd in Ericeira</li>
          <li>Gezamenlijke afsluiting</li>
          <li>Transfer naar Lissabon Airport &amp; vlucht naar Nederland</li>
        </ul>
        <p style="margin-top:14px;font-style:italic;color:#666;">Nog &eacute;&eacute;n keer het water in, nog &eacute;&eacute;n keer genieten van Ericeira. One last wave. One big WOW.</p>
      </div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head left">
      <span class="kicker">Voorbereiding</span>
      <h2>WOW Packing List</h2>
      <p>Je reist licht. Neem vooral mee wat je echt nodig hebt en controleer vooraf de actuele bagageregels van de luchtvaartmaatschappij.</p>
    </div>
    <div class="pack-grid">
      <div class="pack-item"><span class="icon">&#129706;</span> Geldig paspoort of ID-kaart &amp; zorgpas</div>
      <div class="pack-item"><span class="icon">&#128085;</span> Kleding voor overdag &amp; voor de avonden</div>
      <div class="pack-item"><span class="icon">&#129649;</span> Zwemkleding voor onder je wetsuit</div>
      <div class="pack-item"><span class="icon">&#128719;&#65039;</span> 1 of 2 handdoeken &amp; toiletartikelen</div>
      <div class="pack-item"><span class="icon">&#128095;</span> Comfortabele schoenen &amp; slippers</div>
      <div class="pack-item"><span class="icon">&#127890;</span> Kleine rugzak voor activiteiten &amp; Lissabon</div>
      <div class="pack-item"><span class="icon">&#128167;</span> Hervulbare waterfles</div>
      <div class="pack-item"><span class="icon">&#128374;&#65039;</span> Zonnebril &amp; pet of hoedje</div>
      <div class="pack-item"><span class="icon">&#129524;</span> Zonnebrand (min. factor 30) &amp; lippenbalsem met SPF</div>
      <div class="pack-item"><span class="icon">&#128241;</span> Telefoon + oplader/powerbank</div>
      <div class="pack-item"><span class="icon">&#128182;</span> Zakgeld</div>
      <div class="pack-item"><span class="icon">&#128138;</span> Eventuele medicijnen &amp; medicijnverklaring</div>
      <div class="pack-item"><span class="icon">&#127183;</span> UNO, kaarten of andere kleine spelletjes</div>
      <div class="pack-item"><span class="icon">&#127477;&#127481;</span> Heel veel zin in Portugal</div>
    </div>
    <p style="margin-top:24px;font-size:14px;color:#666;max-width:700px;"><strong>Belangrijk:</strong> zijn er di&euml;etwensen, voedselallergie&euml;n, medicijngebruik of andere bijzonderheden? Zorg dan dat deze v&oacute;&oacute;r vertrek bij de reisleiding bekend zijn.</p>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">Afspraken</span>
        <h2>Veiligheid = WOW Standard</h2>
        <p>Een geweldige reis kan alleen bestaan wanneer de basis goed geregeld is. Daarom staat veiligheid bij WOW altijd voorop. We werken met duidelijke afspraken, betrokken begeleiding en professionele lokale partners en instructeurs.</p>
        <p>Tijdens activiteiten luisteren we naar de instructeurs en de WOW-begeleiding. We letten op elkaar. We respecteren elkaar. We helpen elkaar. En we geven iedereen de ruimte om zichzelf te zijn.</p>
      </div>
      <div class="split-media">
        <div class="founder-quote" style="height:100%;display:flex;flex-direction:column;justify-content:center;">
          <span class="mark">&ldquo;</span>
          <p style="font-size:clamp(17px,2vw,20px);">Vrijheid krijg je wanneer je laat zien dat je verantwoordelijkheid aankunt.</p>
        </div>
      </div>
    </div>
    <p class="lead center" style="margin-top:36px;font-weight:700;">Alcohol, drugs en andere ongein horen niet thuis binnen onze WOW Experience. We willen een positieve en veilige omgeving cre&euml;ren waarin iedereen kan sporten, ontdekken, groeien, lachen en genieten.</p>
  </div>
</section>

<section class="effect-section reveal">
  <div class="wrap">
    <span class="kicker" style="text-align:center;display:block;">Waarom WOW Lisboa Super Surf?</span>
    <div class="effect-headline">Omdat je over een paar jaar niet meer weet wat je tijdens het vierde lesuur hebt gedaan.<br>Maar je <span class="coral">eerste golf</span> vergeet je niet.</div>
    <div class="effect-story">
      <p>Samen met je vrienden door Lissabon lopen. Die klasgenoot die na tien pogingen eindelijk op zijn surfboard stond. Samen lachen op het strand. Dat moment waarop je iets deed waarvan je eerst dacht dat je het niet kon.</p>
      <p>Dat is waarom wij reizen. Niet alleen om ergens naartoe te gaan, maar om iets mee te maken. Om nieuwe mensen te leren kennen, grenzen te verleggen, zelfstandiger te worden, zelfvertrouwen op te bouwen en verantwoordelijkheid te leren nemen.</p>
      <p class="payoff">En om samen verhalen te cre&euml;ren die jaren later nog steeds beginnen met: &ldquo;Weet je nog, in Portugal&hellip;?&rdquo;</p>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="wrap final-content">
    <h2>Join the WOW.</h2>
    <p>Niet alleen waar je naartoe gaat. Maar wie je onderweg wordt.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("experience-lisboa.html", "WOW Lisboa Super Surf — Ericeira & Lissabon | WOW Experience Company",
     "WOW Lisboa Super Surf: 5-daagse surfreis naar Ericeira met een dagtrip Lissabon. Surfen, SUP, bodyboarden en strandsport aan de Portugese Atlantische kust.",
     "reizen.html", lisboa_body)

# =========================================================================
# WAAROM WOW
# =========================================================================
waarom_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "Waarom WOW")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; Waarom WOW</div>
    <span class="kicker">Waarom WOW</span>
    <h1>Jullie de leerlingen. Wij de organisatie.</h1>
    <p class="hero-sub">WOW komt uit het onderwijs. We kennen leerlingen, we begrijpen docenten en we weten hoeveel werk een goede schoolreis kost &mdash; en hoeveel impact een geweldige schoolreis kan hebben.</p>
  </div>
</section>

<section class="effect-section reveal">
  <div class="wrap">
    <span class="kicker" style="text-align:center;display:block;">Het WOW-statement</span>
    <div class="effect-headline">Ik accepteer geen middelmatige schoolreis.<br><span class="coral">Voor geen enkele school.</span></div>
    <div class="effect-story">
      <p>Een schoolreis is niet zomaar een paar dagen weg.</p>
      <p>Het is een vormende ervaring. Een paar dagen waarin leerlingen groeien, nieuwe verbindingen aangaan, verantwoordelijkheid nemen en ontdekken dat ze vaak veel meer kunnen dan ze zelf denken.</p>
      <p class="payoff">Maar dat gebeurt alleen als alles klopt.</p>
    </div>
  </div>
</section>

<section class="split-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">Persoonlijk betrokken</span>
        <h2>Als docent, vader en coach weet ik hoeveel deze fase ertoe doet</h2>
        <p>Scholieren zijn volop bezig met hun identiteit, hun grenzen en hun plek binnen een groep. Daarom organiseer ik met WOW geen standaard schoolreizen. Ik wil ervaringen cre&euml;ren die leerlingen sterker, zelfstandiger, weerbaarder en zelfverzekerder maken.</p>
        <p>Ik ben persoonlijk betrokken bij iedere reis. Ik bezoek de locaties, test activiteiten, controleer veiligheid en logistiek en werk alleen met partners waarin ik vertrouwen heb.</p>
        <div class="badge-row">
          <span class="badge">Surfen</span>
          <span class="badge">Suppen</span>
          <span class="badge">Hiken</span>
          <span class="badge">Samenwerken</span>
          <span class="badge">Grenzen verleggen</span>
        </div>
        <p style="margin-top:22px;font-weight:700;">En altijd binnen een veilige omgeving waarin leerlingen worden gezien.</p>
      </div>
      <div class="split-media">{IMG("founder-surf-test.jpg", "Milan test persoonlijk de activiteiten en locaties van WOW")}</div>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">WOW is een onderwijsleerplatform</span>
      <h2>Drie werelden komen samen</h2>
      <p>Een platform waar leerlingen, scholen en toekomstige sportprofessionals elkaar versterken.</p>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#127793;</span><h3>Leerlingen</h3><p>Ontwikkelen zich door ervaringen die persoonlijke groei, verbinding, zelfstandigheid en verantwoordelijkheid stimuleren.</p></div>
      <div class="info-card"><span class="icon">&#127979;&#65039;</span><h3>Scholen &amp; docenten</h3><p>Worden professioneel ontzorgd bij de organisatie en uitvoering van buitenlandse schoolreizen.</p></div>
      <div class="info-card"><span class="icon">&#127891;</span><h3>Studenten</h3><p>Studenten uit sport- en onderwijsopleidingen krijgen een unieke stageplek waar ze in de praktijk leren begeleiden, organiseren en verantwoordelijkheid dragen.</p></div>
    </div>
    <p class="lead center" style="margin-top:36px;font-weight:700;">Leerlingen groeien. Docenten worden ontzorgd. Studenten krijgen kansen.</p>
    <p class="lead center" style="font-weight:800;color:var(--coral);">Een echte win-win-win.</p>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="founder-quote" style="max-width:820px;">
      <span class="mark">&ldquo;</span>
      <p>Mijn doel is niet dat leerlingen na afloop alleen zeggen: &ldquo;Wat was dit een gave schoolreis.&rdquo; Ik wil dat ze jaren later nog weten wat ze daar hebben ontdekt over zichzelf. Dat is mijn missie met WOW &mdash; The Experience Company.</p>
    </div>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">01 &middot; Ontzorgen</span>
      <h2>Wij regelen. Jullie begeleiden.</h2>
      <p>WOW neemt zoveel mogelijk organisatie uit handen, van eerste idee tot de terugreis.</p>
    </div>
    <div class="flow-diagram">
      <span class="flow-pair"><span class="flow-step">Vervoer</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Accommodatie</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Activiteiten</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Planning</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Partners</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Veiligheid</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-pair"><span class="flow-step">Communicatie</span><span class="flow-arrow">&rarr;</span></span>
      <span class="flow-step">Experience</span>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#128652;</span><h3>Vervoer &amp; accommodatie</h3><p>Van touringcar tot verblijf: volledig geregeld en vooraf ge&iuml;nspecteerd.</p></div>
      <div class="info-card"><span class="icon">&#128221;</span><h3>Planning &amp; draaiboek</h3><p>Een compleet programma en draaiboek, afgestemd op jullie school.</p></div>
      <div class="info-card"><span class="icon">&#128172;</span><h3>Communicatie</h3><p>Heldere communicatie naar docenten, leerlingen &eacute;n ouders, voor en tijdens de reis.</p></div>
    </div>
    <p class="lead" style="text-align:center;margin-top:36px;font-weight:700;">Minder organiseren. Minder werkdruk. Meer aandacht voor leerlingen.</p>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">02 &middot; Onderwijs &amp; leerplatform</span>
      <h2>De schoolreis als leeromgeving</h2>
      <p>Leren gaat verder dan het klaslokaal. WOW bouwt een brug tussen middelbaar onderwijs, sportopleidingen en praktijkervaring.</p>
    </div>
    <p style="max-width:760px;margin:0 auto 10px;text-align:center;">WOW werkt waar mogelijk samen met studenten van relevante sport- en onderwijsopleidingen (denk aan HALO/ALO, Sportkunde, Sport &amp; Bewegen, Outdoor en Leisure). Afhankelijk van opleiding, stageafspraken en bevoegdheden kunnen zij ondersteunen bij sportactiviteiten, groepsbegeleiding, organisatie en de persoonlijke ontwikkeling van leerlingen &mdash; altijd aanvullend binnen een professionele structuur, nooit als vervanging van gekwalificeerde professionals waar specifieke bevoegdheden noodzakelijk zijn.</p>
    <div class="flow-vertical">
      <div class="flow-step">Sportstudent</div><div class="flow-arrow">&darr;</div>
      <div class="flow-step">Praktijkervaring</div><div class="flow-arrow">&darr;</div>
      <div class="flow-step">Ondersteuning WOW Experience</div><div class="flow-arrow">&darr;</div>
      <div class="flow-step">Meer aandacht voor leerlingen</div><div class="flow-arrow">&darr;</div>
      <div class="flow-step">Persoonlijke ontwikkeling</div>
    </div>
    <p class="center" style="margin-top:36px;font-weight:700;">WOW verbindt onderwijs, praktijkervaring en schoolreizen.</p>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">03 &middot; Kosten beheersen</span>
      <h2>Meer WOW uit het beschikbare budget</h2>
      <p>Maximale kwaliteit en beleving binnen een verantwoord schoolbudget &mdash; door directe samenwerking met lokale partners, vaste bestemmingen, effici&euml;nte groepsplanning en het onderwijs- en leerplatform.</p>
    </div>
    <div class="compare-grid">
      <div class="compare-col self">
        <h3>Zelf organiseren</h3>
        <ul>
          <li><span class="dot"></span>Losse leveranciers</li>
          <li><span class="dot"></span>Veel co&ouml;rdinatie</li>
          <li><span class="dot"></span>Veel docenturen</li>
          <li><span class="dot"></span>Veel regelwerk</li>
          <li><span class="dot"></span>Verspreide verantwoordelijkheden</li>
        </ul>
      </div>
      <div class="compare-col wow">
        <h3>Met WOW</h3>
        <ul>
          <li><span class="dot"></span>&Eacute;&eacute;n aanspreekpunt</li>
          <li><span class="dot"></span>&Eacute;&eacute;n organisatie</li>
          <li><span class="dot"></span>Vaste partners</li>
          <li><span class="dot"></span>Effici&euml;nte planning</li>
          <li><span class="dot"></span>Onderwijskennis &amp; professionele structuur</li>
        </ul>
      </div>
    </div>
    <p class="lead center" style="margin-top:36px;font-weight:700;">Minder regelen. Meer beleven. Meer impact.</p>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <span class="kicker">Good Practice &middot; Evaluatierapport WOW schoolreis 2026</span>
      <h2>Een reis vol vrijheid &eacute;n groei. Onvergetelijke herinneringen.</h2>
      <p>Na afloop van de reis hebben alle leerlingen een uitgebreide evaluatie ingevuld. De resultaten laten een prachtig beeld zien van hoe de reis is ervaren. De algemene conclusie is overduidelijk: leerlingen hebben een geweldige week gehad.</p>
      <div class="badge-row" style="justify-content:center;">
        <span class="badge">104 leerlingen</span>
        <span class="badge">7 studenten</span>
        <span class="badge">7 docenten</span>
      </div>
    </div>
    <div class="info-grid" style="grid-template-columns:repeat(4,1fr);">
      <div class="price-card"><div class="amount">9.2</div><p>Groepssfeer</p></div>
      <div class="price-card"><div class="amount">9.4</div><p>Vrijheid &amp; beleving</p></div>
      <div class="price-card"><div class="amount">8.8</div><p>Activiteiten</p></div>
      <div class="price-card"><div class="amount">9.1</div><p>Begeleiding</p></div>
    </div>
    <div class="testi-card" style="max-width:760px;margin:32px auto 0;">
      <div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p>&ldquo;Onze beste schoolreis tot nu toe!! Een fantastische, goed georganiseerde reis met hele gave activiteiten, veel keuze en vrijheid. Begeleid door gave studenten van de sportacademie HALO. Mega gave herinneringen.&rdquo;</p>
      <div class="testi-who"><div class="testi-avatar">&#9733;</div><div><strong>Uit de evaluatie</strong><span>Leerling &middot; WOW schoolreis 2026</span></div></div>
    </div>
    <div class="badge-row" style="justify-content:center;margin-top:28px;">
      <span class="badge">Gezellig</span><span class="badge">Ontspannen</span><span class="badge">Vrij</span><span class="badge">Goed georganiseerd</span><span class="badge">Onvergetelijk</span>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW")}</div>
  <div class="wrap final-content">
    <h2>De volgende schoolreis mag een WOW worden.</h2>
    <p>Ontdek wat we voor jullie leerlingen kunnen cre&euml;ren.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("waarom-wow.html", "Waarom WOW | WOW — The Experience Company",
     "Waarom scholen kiezen voor WOW: ontzorgen, onderwijs & leerplatform, en slim omgaan met het schoolbudget.",
     "waarom-wow.html", waarom_body)


# =========================================================================
# VEILIGHEID
# =========================================================================
veiligheid_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "Veiligheid bij WOW")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; Veiligheid</div>
    <span class="kicker">Veiligheid &amp; vertrouwen</span>
    <h1>Vrijheid door goede afspraken.</h1>
    <p class="hero-sub">Avontuur krijgt pas waarde als de basis klopt. Veiligheid is geen vinkje &mdash; het zit in de volledige organisatie van een WOW Experience.</p>
  </div>
</section>

<section class="usp-section reveal">
  <div class="wrap">
    <div class="section-head" style="max-width:820px;">
      <span class="kicker">WOW &amp; Veiligheid</span>
      <h2>Bij WOW staat veiligheid altijd op nummer &eacute;&eacute;n.</h2>
    </div>
    <div style="max-width:820px;margin:0 auto;">
      <p>Wij willen leerlingen uitdagen om nieuwe dingen te proberen, grenzen te verleggen, zelfstandiger te worden en vooral samen een fantastische tijd te beleven. Maar dat kan alleen wanneer leerlingen, ouders &eacute;n scholen erop kunnen vertrouwen dat de basis goed geregeld is.</p>
      <p>Daarom is veiligheid bij WOW geen los onderdeel van de reis. Het zit in alles wat we doen.</p>
      <p>We selecteren onze bestemmingen, accommodaties, vervoerders en activiteiten zorgvuldig en werken met betrouwbare en professionele partners. Voor iedere reis maken we duidelijke afspraken over begeleiding, verantwoordelijkheden, vrije tijd, communicatie en handelen bij calamiteiten.</p>
      <p>Tijdens de reis werken we met een betrokken begeleidingsteam van docenten, WOW-begeleiders en waar mogelijk studenten van de HALO en Sport &amp; Bewegen. Hierdoor cre&euml;ren we extra zichtbaarheid, persoonlijke aandacht en korte lijnen met leerlingen.</p>
      <p>We werken met duidelijke regels en heldere kaders. Leerlingen krijgen vrijheid en verantwoordelijkheid, maar altijd passend bij hun leeftijd en binnen afspraken die vooraf samen met de school worden vastgesteld. Alcohol, drugs en gedrag dat de veiligheid van anderen in gevaar brengt, accepteren we niet.</p>
      <p>Daarnaast besteden we aandacht aan EHBO/BHV, noodcontacten, medische bijzonderheden, aanwezigheid en bereikbaarheid. De WOW-organisatie is tijdens de reis 24/7 bereikbaar en bij activiteiten werken we met passende veiligheidsmaterialen en professionele instructeurs waar dat nodig is.</p>
      <p>Maar veiligheid gaat voor ons verder dan alleen fysieke veiligheid.</p>
      <p>Een leerling moet zich ook sociaal en emotioneel veilig voelen. Iedereen hoort erbij. We hebben aandacht voor groepsdynamiek, leerlingen die extra ondersteuning nodig hebben en jongeren die bepaalde activiteiten spannend vinden. Door keuzevrijheid en persoonlijke begeleiding kan iedere leerling op zijn of haar eigen niveau deelnemen.</p>
      <p style="font-weight:700;">Veiligheid geeft vertrouwen.<br>Vertrouwen geeft vrijheid.<br>En vanuit die vrijheid ontstaat groei.</p>
      <p style="font-weight:700;">Dat is WOW.</p>
      <p style="color:#e6432f;font-weight:800;letter-spacing:1px;text-transform:uppercase;font-size:13px;margin-top:22px;">Safe &middot; Structured &middot; Unforgettable</p>
      <p style="font-weight:700;">Join the WOW.</p>
    </div>
  </div>
</section>

<section class="usp-section alt reveal">
  <div class="wrap">
    <div class="section-head">
      <h2 style="font-size:clamp(22px,3vw,30px);">Maximale beleving. Duidelijke afspraken. Professionele verantwoordelijkheid.</h2>
      <p>Goede voorbereiding creëert juist meer ruimte om te beleven &mdash; dat is het uitgangspunt achter alles wat WOW regelt.</p>
    </div>
    <div class="safety-grid">
      <div class="safety-card"><span class="icon">&#128100;</span><h3>Professionele begeleiding</h3><p>Ervaren begeleiders reizen mee op elke WOW Experience, inclusief het WOW-team zelf.</p></div>
      <div class="safety-card"><span class="icon">&#9989;</span><h3>Duidelijke afspraken</h3><p>Heldere gedragsregels en verwachtingen, vooraf gecommuniceerd naar school, ouders en leerlingen.</p></div>
      <div class="safety-card"><span class="icon">&#128203;</span><h3>Risicoanalyse</h3><p>Activiteiten en locaties worden vooraf beoordeeld op risico's en zorgvuldig geselecteerd.</p></div>
      <div class="safety-card"><span class="icon">&#128154;</span><h3>EHBO/BHV</h3><p>Begeleiding met kennis van eerste hulp, aanwezig gedurende de hele reis.</p></div>
      <div class="safety-card"><span class="icon">&#129309;</span><h3>Betrouwbare lokale partners</h3><p>Accommodaties en activiteitenpartners zijn persoonlijk bezocht en getest.</p></div>
      <div class="safety-card"><span class="icon">&#128172;</span><h3>Oudercommunicatie</h3><p>Een groepsapp houdt ouders op de hoogte tijdens de reis.</p></div>
      <div class="safety-card"><span class="icon">&#128683;</span><h3>Alcohol- en drugsbeleid</h3><p>Zero-tolerance beleid, helder gecommuniceerd voorafgaand aan iedere reis.</p></div>
      <div class="safety-card"><span class="icon">&#127973;</span><h3>Medische bijzonderheden</h3><p>Allergie&euml;n en medische gegevens worden vooraf uitgevraagd en zorgvuldig behandeld.</p></div>
      <div class="safety-card"><span class="icon">&#128737;&#65039;</span><h3>Noodprocedures</h3><p>Duidelijke noodprocedures en verantwoordelijkheden, bekend bij alle begeleiders.</p></div>
    </div>
  </div>
</section>

<section class="split-section alt reveal">
  <div class="wrap">
    <div class="safety-banner">
      <div>
        <h2>Financi&euml;le bescherming via VZR Garant</h2>
        <p>WOW-reizen zijn gedekt door VZR Garant financi&euml;le bescherming, en reizigers worden voorzien van reisverzekering passend bij de Experience (inclusief wintersportdekking voor WOW in the Snow).</p>
      </div>
      <div>
        <h2>Voorbereiding van begeleiders</h2>
        <p>Begeleiders worden voorbereid op hun rol, met heldere verantwoordelijkheden en verwachtingen &mdash; zodat leerlingen kunnen ontdekken binnen een veilige structuur.</p>
      </div>
    </div>
    <div class="section-head">
      <span class="kicker">Wat WOW regelt, van begin tot eind</span>
      <h2>Voorbereiding, tijdens de reis, en erna</h2>
    </div>
    <div class="info-grid">
      <div class="info-card"><span class="icon">&#128203;</span><h3>Voor vertrek</h3><p>Risicoanalyse, oudercommunicatie, verzameling medische gegevens en allergie&euml;n, en heldere gedragsregels.</p></div>
      <div class="info-card"><span class="icon">&#9992;&#65039;</span><h3>Tijdens de reis</h3><p>Professionele begeleiding, EHBO/BHV, veilig vervoer en zorgvuldig geselecteerde activiteiten en accommodatie.</p></div>
      <div class="info-card"><span class="icon">&#128172;</span><h3>Communicatie</h3><p>Doorlopende afstemming met school en ouders via de groepsapp, en heldere noodprocedures indien nodig.</p></div>
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="wrap final-content">
    <h2>Vragen over veiligheid?</h2>
    <p>We lichten graag toe hoe WOW dit voor jullie school organiseert.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("veiligheid.html", "Veiligheid & Vertrouwen | WOW — The Experience Company",
     "Veiligheid bij WOW: professionele begeleiding, risicoanalyse, EHBO/BHV, oudercommunicatie en VZR Garant financiële bescherming.",
     "veiligheid.html", veiligheid_body)

# =========================================================================
# OVER WOW
# =========================================================================
over_body = f"""
<section class="hero-compact">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "Over WOW")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; Over WOW</div>
    <span class="kicker">Over WOW</span>
    <h1>Niet organiseren vanachter een bureau.</h1>
    <p class="hero-sub">Maar zelf weten wat leerlingen straks gaan meemaken.</p>
  </div>
</section>

<section class="founder-section reveal">
  <div class="wrap">
    <div class="split-grid">
      <div class="split-text">
        <span class="kicker">Het verhaal achter WOW</span>
        <h2>Wie is WOW</h2>
        <p style="font-weight:700;">Milan Worisek &mdash; docent, coach en oprichter.</p>
        <p>Ik ben Milan Worisek, docent Lichamelijke Opvoeding en coach. Al jarenlang begeleid ik leerlingen, niet alleen op school, maar ook tijdens reizen.</p>
        <p>Daarnaast begeleid ik Sport &amp; Bewegen-studenten en HALO-studenten in hun opleiding, ontwikkeling en professionele groei. Het begeleiden van jonge mensen, hen verantwoordelijkheid geven en zien groeien, is een belangrijk onderdeel van wie ik ben als docent en coach.</p>
        <p>In de afgelopen jaren heb ik meer dan 1.000 leerlingen op reis begeleid. Vanuit mijn ervaring als docent, begeleider, coach, sportman en organisator heb ik WOW Reizen opgericht.</p>
        <p>Want ik geloof dat een schoolreis veel meer kan zijn dan alleen vervoer en een hotel. Het moet een ervaring zijn waarin leerlingen nieuwe dingen ontdekken, zelfstandiger worden, verantwoordelijkheid nemen en samen herinneringen maken die hen nog lang bijblijven.</p>
        <p>Samen met mijn co-organisator Danique Ewbank Verdonk bouw ik WOW uit tot wat wij noemen: de beste schoolreis 2.0. Een reis waarin leerlingen de vrijheid en autonomie krijgen om te ontdekken en te genieten, terwijl wij achter de schermen zorgen voor structuur, duidelijke afspraken en doordachte veiligheid. Zo ontstaat er vertrouwen voor leerlingen, scholen &eacute;n ouders.</p>
        <p style="font-weight:700;">Ik bedenk WOW niet alleen vanachter een bureau.</p>
      </div>
      <div class="split-media">{IMG("milan-portrait-wow-tshirt.jpg", "Milan Worisek, oprichter WOW Reizen")}</div>
    </div>

    <div class="founder-quote">
      <span class="mark">&ldquo;</span>
      <p>Ik wil leerlingen nooit iets laten beleven wat ik zelf niet eerst heb ervaren.</p>
    </div>

    <div class="founder-timeline">
      <div class="timeline-card"><div class="role">Docent &amp; coach</div><p>Jarenlange ervaring in het lichamelijk opvoeding-onderwijs en het begeleiden van groepen leerlingen.</p></div>
      <div class="timeline-card"><div class="role">Reisorganisator</div><p>Meer dan 1000 leerlingen begeleid op schoolreizen, met sport en avontuur als rode draad.</p></div>
      <div class="timeline-card"><div class="role">Oprichter WOW Reizen</div><p>WOW Reizen opgericht om onderwijskennis, sport en persoonlijke groei samen te brengen in &eacute;&eacute;n Experience.</p></div>
    </div>

    <div class="section-head" style="margin-top:70px;">
      <span class="kicker">Persoonlijk getest</span>
      <h2>Zelf op de plek, voordat leerlingen er komen</h2>
      <p>Bestemmingen, accommodaties en lokale partners worden door het WOW-team zelf bezocht: van SUP-sessies en surfen tot skien en wandelen &mdash; om te weten wat leerlingen straks gaan beleven.</p>
    </div>
    <div class="founder-gallery" style="grid-template-columns:repeat(auto-fit,minmax(160px,1fr));">
      {IMG("founder-sup-group.jpg", "Milan met leerlingen en SUP, padel en bodyboard materiaal in Palamós")}
      {IMG("founder-surf-test.jpg", "WOW — surfen testen")}
      {IMG("founder-sup-solo.jpg", "Milan met de WOW SUP-board bij La Fosca, Palamós")}
      {IMG("founder-milan-sup-paddle.jpg", "Milan met de WOW SUP-board en peddel")}
      {IMG("danique-sup-espana.jpg", "Danique met de WOW SUP-board tijdens WOW Espana")}
    </div>
  </div>
</section>

<section class="final-cta reveal">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "WOW")}</div>
  <div class="wrap final-content">
    <h2>Maak kennis met het team achter WOW.</h2>
    <p>We denken graag mee over de beste Experience voor jullie leerlingen.</p>
    <a class="btn btn-lg" href="{CALENDLY}" target="_blank" rel="noopener">Plan een kennismaking &rarr;</a>
  </div>
</section>
"""
page("over-wow.html", "Over WOW | WOW — The Experience Company",
     "Het verhaal achter WOW Reizen: opgericht door Milan Worisek, docent en coach, vanuit jarenlange ervaring in het onderwijs.",
     "over-wow.html", over_body)


# =========================================================================
# CONTACT
# =========================================================================
faq_categories = [
    ("all", "Alles"),
    ("algemeen", "Algemeen"),
    ("veiligheid", "Veiligheid"),
    ("praktisch", "Praktisch"),
]

faq_items = [
    ("algemeen", "Voor welke leeftijd zijn WOW-reizen bedoeld?", "WOW-reizen zijn ontwikkeld voor scholieren in het voortgezet onderwijs, doorgaans in de leeftijd van 13 tot 19 jaar."),
    ("algemeen", "Wat is de minimale en maximale groepsgrootte?", "Dit verschilt per Experience: WOW Espana schoolreizen vanaf 40 tot 160 leerlingen, WOW in the Snow tot 74 deelnemers. Neem contact op voor maatwerk."),
    ("praktisch", "Wat kost een WOW-reis?", "Richtprijzen per leerling: WOW Espana &euro;550, WOW Italia &euro;650, WOW in the Snow &euro;650, WOW Lisboa Super Surf &euro;800. Deze prijzen zijn compleet &mdash; geen verborgen kosten. De uiteindelijke prijs hangt af van programma, periode en groepsgrootte; voor schoolreizen op maat stellen we een prijsindicatie samen na een kennismaking."),
    ("veiligheid", "Hoe is de begeleiding tijdens de reis geregeld?", "Professionele begeleiders reizen mee op elke WOW-reis, inclusief leden van het WOW-team zelf. Zie de veiligheidspagina voor alle details."),
    ("algemeen", "Worden sportstudenten ingezet tijdens de reis?", "Waar mogelijk werkt WOW samen met studenten van relevante sport- en onderwijsopleidingen, die ondersteunen binnen een professionele structuur. Zij vervangen nooit gekwalificeerde professionals waar specifieke bevoegdheden nodig zijn."),
    ("praktisch", "Zijn de reizen verzekerd?", "Ja. WOW-reizen zijn gedekt door VZR Garant financi&euml;le bescherming en reizigers krijgen een passende reisverzekering, inclusief wintersportdekking voor WOW in the Snow."),
    ("praktisch", "Hoe gaat WOW om met dieetwensen en allergie&euml;n?", "Dieetwensen, allergie&euml;n en medische bijzonderheden worden voorafgaand aan de reis uitgevraagd en meegenomen in de organisatie."),
    ("veiligheid", "Wat is het beleid rondom alcohol en drugs?", "WOW hanteert een zero-tolerance beleid voor alcohol en drugs tijdens alle reizen, helder gecommuniceerd naar leerlingen en ouders vooraf."),
    ("veiligheid", "Hoe blijven ouders op de hoogte tijdens de reis?", "Via een groepsapp worden ouders doorlopend op de hoogte gehouden van het programma en eventuele bijzonderheden."),
    ("praktisch", "Kan het programma op maat gemaakt worden voor onze school?", "Ja. Na een kennismakingsgesprek stellen we een Experience samen die past bij jullie leerlingen, onderwijsniveau en wensen."),
    ("praktisch", "Hoe zit het met annuleren of wijzigen?", "Annulerings- en wijzigingsvoorwaarden worden per boeking gedeeld en zijn afgestemd op de geldende reisvoorwaarden. Vraag hiernaar tijdens de kennismaking."),
    ("praktisch", "Wat gebeurt er na het invullen van het contactformulier?", "Je ontvangt een bevestiging en het WOW-team neemt binnen enkele werkdagen contact op om een kennismaking in te plannen."),
]

def faq_html(items):
    out = []
    for cat, q, a in items:
        out.append(f'''<div class="faq-item" data-cat="{cat}">
        <div class="faq-q"><span>{q}</span><span class="plus">+</span></div>
        <div class="faq-a"><div class="faq-a-inner">{a}</div></div>
      </div>''')
    return "\n      ".join(out)

faq_cat_buttons = "\n      ".join(
    f'<button class="faq-cat-btn{" active" if key=="all" else ""}" data-cat="{key}">{label}</button>'
    for key, label in faq_categories
)

contact_body = f"""
<section class="hero-compact" style="min-height:44vh;">
  <div class="hero-media">{IMG("wow-hero-palamos.jpg", "Contact WOW")}</div>
  <div class="wrap hero-content">
    <div class="breadcrumb"><a href="index.html">Home</a> &rarr; Contact</div>
    <span class="kicker">Klaar voor jullie WOW?</span>
    <h1>Vertel ons wat jullie zoeken.</h1>
    <p class="hero-sub">Wij laten zien wat er mogelijk is. Vul het formulier in of plan direct een gratis kennismaking.</p>
  </div>
</section>

<section class="contact-section reveal">
  <div class="wrap">
    <div class="contact-grid">
      <div class="contact-info-card">
        <h3>Liever direct plannen?</h3>
        <p>Plan een gratis kennismaking van 30 minuten &mdash; we bespreken jullie school, leerlingen en wensen.</p>
        <a class="btn btn-block" href="{CALENDLY}" target="_blank" rel="noopener">Plan mijn kennismaking &rarr;</a>
        <div class="contact-info-row"><div class="icon">&#128197;</div><div><strong>Kennismaking</strong><span>30 minuten, via Calendly</span></div></div>
        <div class="contact-info-row"><div class="icon">&#128247;</div><div><strong>Instagram</strong><span><a href="{INSTAGRAM}" target="_blank" rel="noopener" style="color:#fff;">@wowreizen</a></span></div></div>
        <div class="contact-info-row"><div class="icon">&#127968;</div><div><strong>WOW Reizen</strong><span>Sport, Cultuur en Plezier.</span></div></div>
      </div>

      <div>
        <form id="lead-form" class="form-grid lead-form" novalidate>
          <div class="field full"><label for="school">Schoolnaam *</label><input id="school" name="school" type="text" required></div>
          <div class="field"><label for="naam">Naam *</label><input id="naam" name="naam" type="text" required></div>
          <div class="field"><label for="functie">Functie *</label><input id="functie" name="functie" type="text" placeholder="Bijv. teamleider, LO-docent" required></div>
          <div class="field"><label for="email">E-mail *</label><input id="email" name="email" type="email" required></div>
          <div class="field"><label for="telefoon">Telefoonnummer *</label><input id="telefoon" name="telefoon" type="tel" required></div>
          <div class="field"><label for="aantal">Aantal leerlingen</label><input id="aantal" name="aantal_leerlingen" type="number" min="1"></div>
          <div class="field">
            <label for="niveau">Onderwijsniveau</label>
            <select id="niveau" name="onderwijsniveau">
              <option value="">Kies een niveau</option>
              <option>VMBO</option><option>HAVO</option><option>VWO</option><option>Gemengd</option><option>Anders</option>
            </select>
          </div>
          <div class="field">
            <label for="bestemming">Gewenste bestemming</label>
            <select id="bestemming" name="bestemming">
              <option value="">Nog niet zeker</option>
              <option>WOW Espana &mdash; Palam&oacute;s &amp; Barcelona</option>
              <option>WOW Italia &mdash; Milaan / Veneti&euml; / Caorle</option>
              <option>WOW in the Snow &mdash; Zell am See</option>
              <option>WOW in the Snow Exclusive &mdash; december 2026 (individueel)</option>
              <option>WOW Lisboa Super Surf &mdash; Lissabon</option>
            </select>
          </div>
          <div class="field"><label for="periode">Gewenste reisperiode</label><input id="periode" name="reisperiode" type="text" placeholder="Bijv. voorjaar 2027"></div>
          <div class="field"><label for="budget">Indicatief budget per leerling</label><input id="budget" name="budget" type="text" placeholder="Bijv. &euro;300&ndash;&euro;400"></div>
          <div class="field full"><label for="wensen">Aanvullende wensen</label><textarea id="wensen" name="wensen" placeholder="Vertel ons meer over wat jullie zoeken..."></textarea></div>
          <div class="field full">
            <button type="submit" class="btn btn-block btn-lg">Plan mijn kennismaking &rarr;</button>
            <p class="form-note">Door dit formulier te versturen ga je akkoord dat WOW Reizen contact met je opneemt over deze aanvraag.</p>
          </div>
        </form>
        <div class="form-success">
          <div class="check">&#10003;</div>
          <h3>Bedankt.</h3>
          <p>Jullie eerste stap naar WOW is gezet. Het WOW-team neemt binnen enkele werkdagen contact op.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="faq-section reveal">
  <div class="wrap-narrow">
    <div class="section-head">
      <span class="kicker">Veelgestelde vragen</span>
      <h2>Alles wat je wilt weten</h2>
    </div>
    <div class="faq-cats">
      {faq_cat_buttons}
    </div>
    <div class="faq-list">
      {faq_html(faq_items)}
    </div>
  </div>
</section>
"""
page("contact.html", "Contact | WOW — The Experience Company",
     "Neem contact op met WOW Reizen: plan een gratis kennismaking of vraag informatie aan via het contactformulier.",
     "contact.html", contact_body, sticky=False)

print("All pages built.")
